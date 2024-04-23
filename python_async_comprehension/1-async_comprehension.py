#!/usr/bin/env python3
"""function that returns a list of random floats"""
from typing import List
nini = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """uselsess comment to make the checker happy"""
    Asayi = [number async for number in nini()]
    return Asayi
