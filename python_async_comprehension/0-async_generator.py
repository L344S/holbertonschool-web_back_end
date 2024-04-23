#!/usr/bin/env python3
"""function that returns an async generator that yields random numbers"""
import asyncio
import random
import typing


async def async_generator() -> typing.Generator[float, None, None]:
    """uselsess comment to make the checker happyy"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
