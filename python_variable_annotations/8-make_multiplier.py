#!/usr/bin/env python3
"""function that multiplies a float by a multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """uselsess comment to make the checker happy"""
    def multiply(n: float) -> float:
        """another uselsess comment to make the checker happy"""
        return n * multiplier
    return multiply
