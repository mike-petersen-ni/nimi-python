# -*- coding: utf-8 -*-
# This file is generated from NI-DCPower API metadata version 22.0.0d131
config = {
    'api_version': '22.0.0d131',
    'c_function_prefix': 'niDCPower_',
    'close_function': 'close',
    'context_manager_name': {
        'abort_function': 'AbortWithChannels',
        'initiate_function': 'InitiateWithChannels',
        'task': 'acquisition'
    },
    'custom_types': [
        {
            'ctypes_type': 'struct_NIComplexNumber',
            'file_name': 'ni_complex_number',
            'python_name': 'NIComplexNumber'
        },
        {
            'ctypes_type': 'struct_NILCRLoadCompensationSpot',
            'file_name': 'ni_lcr_load_compensation_spot',
            'python_name': 'NILCRLoadCompensationSpot'
        },
        {
            'ctypes_type': 'struct_NILCRMeasurement',
            'file_name': 'ni_lcr_measurement',
            'python_name': 'NILCRMeasurement'
        }
    ],
    'driver_name': 'NI-DCPower',
    'extra_errors_used': [
        'InvalidRepeatedCapabilityError',
        'SelfTestError'
    ],
    'init_function': 'FancyInitialize',
    'library_info': {
        'Linux': {
            '64bit': {
                'name': 'nidcpower',
                'type': 'cdll'
            }
        },
        'Windows': {
            '32bit': {
                'name': 'nidcpower_32.dll',
                'type': 'windll'
            },
            '64bit': {
                'name': 'nidcpower_64.dll',
                'type': 'cdll'
            }
        }
    },
    'metadata_version': '2.0',
    'module_name': 'nidcpower',
    'repeated_capabilities': [
        {
            'prefix': '',
            'python_name': 'channels'
        },
        {
            'prefix': '',
            'python_name': 'instruments'
        }
    ],
    'session_class_description': 'An NI-DCPower session to an NI programmable power supply or source measure unit.',
    'session_handle_parameter_name': 'vi',
    'uses_nitclk': False
}
