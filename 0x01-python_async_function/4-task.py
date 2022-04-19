#!/usr/bin/env python3
'''
4. Tasks
'''

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Async routine that spawn task_wait_random n times
    with the specified max_delay
    '''
    lst: List[float] = []
    i: int = 0
    while i < n:
        lst.append(await task_wait_random(max_delay))
        i += 1

    return sorted(lst)
