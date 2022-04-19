#!/usr/bin/env python3
'''
 Measure the runtime
'''

import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''
    Function that measures the total execution time for wait_n
    '''
    start: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    end: float = time.time()
    total_time: float = end - start
    result = total_time/n

    return result if n else 0
