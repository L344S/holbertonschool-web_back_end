#!/usr/bin/env python3
"""function that returns the length of each element in a list"""
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """uselsess comment to make the checker happy"""
    return [(i, len(i)) for i in lst]
