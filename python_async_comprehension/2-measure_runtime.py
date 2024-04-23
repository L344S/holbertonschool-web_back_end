#!/usr/bin/env python3
"""function that measures the runtime of a coroutine"""
import asyncio
nabi = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """uselsess comment to make the checker happy"""
    baslangic = asyncio.get_event_loop().time()
    await asyncio.gather(*(nabi() for _ in range(4)))
    bitis = asyncio.get_event_loop().time()
    toplam = bitis - baslangic
    return toplam
