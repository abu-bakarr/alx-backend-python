#!/usr/bin/env python3
'''
 Concurrent coroutine
'''


import asyncio
# import bisect
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Async routine that has wait_random n times with the specified 
    '''
    lst: List[float] = []
    i: int = 0
    while i < n:
        lst.append(await wait_random(max_delay))
        i += 1

    return sorted(lst)
