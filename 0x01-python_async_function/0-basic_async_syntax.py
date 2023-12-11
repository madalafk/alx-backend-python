#!/usr/bin/env python3
'''
an asynchronous coroutine that takes in an
integer argument (max_delay, with a default
value of 10) named wait_random
'''

import asyncio
from random import uniform

async def wait_random(max_delay: int = 10) -> float:
    '''
    waits for a random delay between 0 and max_delay
    (included and float value) seconds and eventually
    returns it.
    '''
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


if __name__ == '__main__':
    print(asyncio.run(wait_random()))
    print(asyncio.run(wait_random(5)))
    print(asyncio.run(wait_random(15)))
