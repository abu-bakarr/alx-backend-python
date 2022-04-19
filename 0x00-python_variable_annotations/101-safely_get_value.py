#!/usr/bin/env python3
'''
    Safely get values
'''

from typing import Mapping, Union, Sequence, Any, TypeVar


def safely_get_value(dct: Mapping, key: Any, default: Union[TypeVar('T'), None] = None) -> Union[Any, TypeVar('T')]:
    '''This Function get a dictionary akey of any'''

    if key in dct:
        return dct[key]
    else:
        return default
