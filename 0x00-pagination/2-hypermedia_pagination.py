#!/usr/bin/env python3
"""class with methods to create simple pagination"""
import csv
from typing import List
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names"""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Reads from csv file and returns the dataset.
        Returns:
            List[List]: The dataset.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    @staticmethod
    def assert_positive_integer_type(value: int) -> None:
        """asserts that the value is a positive int"""
        assert type(value) is int and value > 0

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """returns a page of the dataset"""
        self.assert_positive_integer_type(page)
        self.assert_positive_integer_type(page_size)
        dataset = self.dataset()
        st, end = index_range(page, page_size)
        try:
            data = dataset[st:end]
        except IndexError:
            data = []
        return data

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """returns a page of the dataset"""
        tot_page = len(self.dataset()) // page_size + 1
        data = self.get_page(page, page_size)
        inf = {
            "page": page,
            "page_size": page_size if page_size <= len(data) else len(data),
            "total_pages": tot_page,
            "data": data,
            "prev_page": page - 1 if page > 1 else None,
            "next_page": page + 1 if page + 1 <= tot_page else None
        }
        return inf
