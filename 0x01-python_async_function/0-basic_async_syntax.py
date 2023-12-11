#!/usr/bin/env python3
'''
An asynchronous coroutine that takes in an
integer argument (max_delay, with a default
value of 10) named wait_random
'''

import asyncio
from random import uniform

async def wait_random(max_delay: int = 10) -> float:
    '''
    Waits for a random delay between 0 and max_delay
    (inclusive and float value) seconds and eventually
    returns it.
    
    Parameters:
        max_delay (int): Maximum delay in seconds (default is 10).

    Returns:
        float: Random delay between 0 and max_delay.
    '''
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

if __name__ == '__main__':
    # Example usage
    print(asyncio.run(wait_random()))  # Run with default max_delay (10 seconds)
    print(asyncio.run(wait_random(5)))  # Run with max_delay of 5 seconds
    print(asyncio.run(wait_random(15)))  # Run with max_delay of 15 seconds

