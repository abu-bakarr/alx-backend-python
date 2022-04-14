#!/usr/bin/env python3
'''
    sum of mixed list
'''

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''
        This Function accepts  sum mixed list arguments
        and then returns the sum of the  result in a float data type
    '''

    return sum(mxd_lst)
