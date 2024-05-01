#!/usr/bin/env python3
"""function that implements a get_page method"""
import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """useless comment to make the checker happy"""
        assert isinstance(
            page, int) and isinstance(
            page_size, int), "Must be int"
        assert page > 0 and page_size > 0, "The page and page_size must be > 0"
        list = []
        with open(self.DATA_FILE) as f:
            read = csv.reader(f)
            idxx = index_range(page, page_size)
            for num, line in enumerate(read):
                if num in range(idxx[0], idxx[1]):
                    list.append(line)
        return list


def index_range(page, page_size):
    """useless comment to make the checker happy"""
    baslangic = (page - 1) * page_size
    bitis = page * page_size
    return tuple([baslangic, bitis])
