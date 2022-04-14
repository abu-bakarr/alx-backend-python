#!/usr/bin/env python3
'''
    safe first element
'''

from typing import Sequence, Any, Union


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''
       This Function accpets a list and then check if then the input list has and elements that
       if if has an element it returns the first index else it returns None
    '''
    if lst:
        return lst[0]
    else:
        return None
