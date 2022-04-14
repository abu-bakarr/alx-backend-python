#!/usr/bin/env python3
'''
    functions
'''

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
        This Function that make a function to multiplies a float argument
        and returns callable function that multiplies
    '''
    def f(n: float):
        '''
            This Function accepts and input n and then multiplies the input
            And then result of multiplies
        '''
        return n * multiplier

    return f
