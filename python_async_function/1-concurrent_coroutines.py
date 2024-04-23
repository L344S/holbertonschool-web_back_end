#!/usr/bin/env python3
"""function that takes in 2 int arguments and returns a list of floats"""
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """uselsess comment to make the checker happy"""
    delays = []
    for _ in range(n):
        notdelay = await wait_random(max_delay)
        delays.append(notdelay)
    return sorted(delays)
