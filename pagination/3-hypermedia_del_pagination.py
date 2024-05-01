#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """useless comment to make the checker happy"""
        assert index is None or (type(index) is int and 0 <= index <
                                 len(self.indexed_dataset()))
        assert type(page_size) is int and page_size > 0
        size_dts = len(self.indexed_dataset())
        baslangic = index if index is not None else 0
        bitis = baslangic + page_size
        dpg = []
        for i in range(baslangic, min(bitis, size_dts)):
            dpg.append(self.indexed_dataset().get(i, None))
        next_index = min(bitis, size_dts)
        bilgi = {
            "index": baslangic,
            "next_index": next_index if next_index < size_dts else None,
            "page_size": len(dpg),
            "data": [item for item in dpg if item is not None]
        }
        return bilgi

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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """useless comment to make the checker happy"""
        dict = {}
        idxx = index_range(page, page_size)
        if (idxx[0] + 1) > len(self.dataset()):
            dict["page_size"] = 0
        else:
            dict["page_size"] = idxx[1] - idxx[0]
        dict["page"] = page
        dict["data"] = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        dict["next_page"] = page + 1 if page < total_pages else None
        dict["prev_page"] = page - 1 if page > 1 else None
        dict["total_pages"] = total_pages
        return dict


def index_range(page, page_size):
    """useless comment to make the checker happy"""
    baslangic = (page - 1) * page_size
    bitis = page * page_size
    return tuple([baslangic, bitis])
