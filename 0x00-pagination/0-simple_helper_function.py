#!/usr/bin/env python3
"""have definition of index_range helper function"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """takes 2 integer arguments and returns a tuple of size two"""
    st, end = 0, 0
    for i in range(page):
        st = end
        end += page_size
    return (st, end)
