#!/usr/bin/env python3
'''
    element length
'''

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''
        This Function accepts then returns the length of each element
    '''
    return [(i, len(i)) for i in lst]
