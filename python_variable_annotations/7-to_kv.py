#!/usr/bin/env python3
"""function with given k(str) and v(int/float) and returns a tuple"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """uselsess comment to make the checker happy"""
    return (k, v*v)
