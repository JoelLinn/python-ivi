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

from .bkprecision9130B import *

class bkprecision9132B(bkprecision9130B):
    "B&K Precision series IVI DC power supply driver"
    
    def __init__(self, *args, **kwargs):
        self.__dict__.setdefault('_instrument_id', '')
        
        super(bkprecision9132B, self).__init__(*args, **kwargs)
        
        self._output_count = 3
        
        self._output_spec = [
            {
                'range': {
                    'P30V': (60.0, 3.0)
                },
                'ovp_max': 61.0,
                'ocp_max': 3.1,
                'voltage_max': 60.0,
                'current_max': 3.0
            },
            {
                'range': {
                    'P30V': (60.0, 3.0)
                },
                'ovp_max': 61.0,
                'ocp_max': 3.1,
                'voltage_max': 60.0,
                'current_max': 3.0
            },
            {
                'range': {
                    'P5V': (5.0, 3.0)
                },
                'ovp_max': 5.0,
                'ocp_max': 3.0,
                'voltage_max': 5.0,
                'current_max': 3.0
            }
        ]
        
        self._identity_description = "B&K Precision 9132B IVI DC power supply driver"
        self._identity_specification_major_version = 1
        self._identity_specification_minor_version = 0
        self._identity_supported_instrument_models = ['9132B']
        
        self._init_outputs()
        
    
    
