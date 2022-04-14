#!/usr/bin/env python3
'''
    to KV
'''

from typing import Union, Tuple
import math


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''
        This Function accepts str and int or float arguments and then returns a
        tuple with the str and te square of int/float as åthe result
    '''

    return (k, math.pow(v, 2))
