#!/usr/bin/env python3
"""define the Server that paginates a database of popular baby names"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """takes 2 integer arguments and returns a tuple of size two"""
    st, end = 0, 0
    for i in range(page):
        st = end
        end += page_size
    return (st, end)


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
        """takes 2 integer arguments and returns requested page"""
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        dataset = self.dataset()
        data_length = len(dataset)
        try:
            idx = index_range(page, page_size)
            return dataset[idx[0]:idx[1]]
        except IndexError:
            return []
