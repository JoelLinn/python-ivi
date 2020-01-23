"""

Python Interchangeable Virtual Instrument Library

Copyright (c) 2013-2020 Alex Forencich

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

from .. import ivi
from .. import dcpwr
from .. import scpi

TrackingType = set(['floating'])
TriggerSourceMapping = {
        'immediate': 'imm',
        'bus': 'bus'}

class bkprecisionBaseDCPwr(scpi.dcpwr.Base, scpi.dcpwr.Trigger, scpi.dcpwr.SoftwareTrigger,
                scpi.dcpwr.Measurement):
    "B&K Precision generic IVI DC power supply driver"
    
    def __init__(self, *args, **kwargs):
        self.__dict__.setdefault('_instrument_id', '')

        super(bkprecisionBaseDCPwr, self).__init__(*args, **kwargs)

        self._output_count = 0

        self._output_spec = []

        self._identity_description = "B&K Precision generic IVI DC power supply driver"
        self._identity_identifier = ""
        self._identity_revision = ""
        self._identity_vendor = ""
        self._identity_instrument_manufacturer = "B&K Precision"
        self._identity_instrument_model = ""
        self._identity_instrument_firmware_revision = ""
        self._identity_specification_major_version = 1
        self._identity_specification_minor_version = 0
        self._identity_supported_instrument_models = []

        self._init_outputs()

    def _utility_self_test(self):
        code = 0
        message = "No Response"
        if not self._driver_operation_simulate:
            self._write("*TST?")
            # wait for test to complete
            message = self._read()
            if message != "0":
                code = -1
        return (code, message)
