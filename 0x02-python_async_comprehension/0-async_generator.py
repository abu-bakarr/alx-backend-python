#!/usr/bin/env python3
'''
 Async Generator
'''

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''
    Coroutine that loop 10 times, each time asynchronously wait 1 second,
    then yield a random number between 0 and 10.
    '''
    remaining: int = 11

    while True:
        remaining -= 1

        if not remaining:
            break

        yield random.uniform(0, 10)
        await asyncio.sleep(1)
