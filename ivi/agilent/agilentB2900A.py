"""

Python Interchangeable Virtual Instrument Library

Copyright (c) 2012-2020 Alex Forencich

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

"""

from .. import extra
from .. import ivi
from .. import scpi

class agilentB2900A(
        scpi.dcpwr.Base,
        scpi.dcpwr.Measurement):
    "Agilent/Keysight generic IVI DC power supply driver"
    
    def __init__(self, *args, **kwargs):
        self.__dict__.setdefault('_instrument_id', '')

        super().__init__(*args, **kwargs)
        
        self._add_property('outputs[].mode',
                        self._get_output_mode,
                        self._set_output_mode,
                        None,
                        ivi.Doc("""
                        Select source output mode.
                        
                        Values
                        
                        * 'current' - Select current source mode.
                        * 'voltage' - Select voltage source mode.
                        """))
        
        self._output_count = 0
        
        self._output_spec = []

        self._identity_description = "Agilent/Keysight generic IVI DC power supply driver"
        self._identity_identifier = ""
        self._identity_revision = ""
        self._identity_vendor = ""
        self._identity_instrument_manufacturer = "Agilent"
        self._identity_instrument_model = ""
        self._identity_instrument_firmware_revision = ""
        self._identity_specification_major_version = 1
        self._identity_specification_minor_version = 0
        self._identity_supported_instrument_models = []

        self._init_outputs()

    def _init_outputs(self):
        try:
            super()._init_outputs()
        except AttributeError:
            pass
        
        self._output_mode = list()
        for i in range(self._output_count):
            self._output_mode.append('voltage')

    def _set_output_current_limit(self, index, value):
        super()._set_output_current_limit(index, value)
        if not self._driver_operation_simulate:
            self._write("sense:current:protection:level %.6f" % value)

    def _set_output_voltage_level(self, index, value):
        super()._set_output_voltage_level(index, value)
        if not self._driver_operation_simulate:
            self._write("sense:voltage:protection:level %.6f" % value)

    def _get_output_mode(self, index):
        index = ivi.get_index(self._output_name, index)
        if not self._driver_operation_simulate and not self._get_cache_valid(index=index):
            if self._output_count > 1:
                self._write("instrument:nselect %d" % (index+1))
            _value = self._ask("source:function:mode?")
            if _value == 'VOLT':
                self._output_mode[index] = 'voltage'
            elif _value == 'CURR':
                self._output_mode[index] = 'current'
            else:
                raise ivi.ValueNotSupportedException()
            self._set_cache_valid(index=index)        
        return self._output_mode[index]

    def _set_output_mode(self, index, value):
        index = ivi.get_index(self._output_name, index)
        if value == 'voltage':
            _value = 'VOLT'
        elif value == 'current':
            _value = 'CURR'
        else:
            raise ivi.ValueNotSupportedException()
        if not self._driver_operation_simulate:
            if self._output_count > 1:
                self._write("instrument:nselect %d" % (index+1))
            self._write("source:function:mode %s" % _value)
        self._output_mode[index] = value
        self._set_cache_valid(index=index)

