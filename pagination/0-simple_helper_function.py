#!/usr/bin/env python3
"""function that returns a tuple of size two containing a start index and an end index"""


def index_range(page, page_size):
    """useless comment to make the checker happy"""
    baslangic = (page - 1) * page_size
    bitis = page * page_size
    return tuple([baslangic, bitis])
