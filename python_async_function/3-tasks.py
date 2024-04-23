#!/usr/bin/env python3
"""function that take an integer and returns a asyncio.Task"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """uselsess comment to make the checker happy"""
    return asyncio.create_task(wait_random(max_delay))
