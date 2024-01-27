#!/usr/bin/env python3
"""
function named index_range that takes two integer arguments page and page_size.

"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """
        function to calculate start and end indeces
        Args:
            page: page number
            page_size: page size
        Return - start index, end index in a tuple
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
