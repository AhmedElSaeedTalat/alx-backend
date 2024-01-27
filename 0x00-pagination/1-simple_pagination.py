#!/usr/bin/env python3
"""
Main file
"""
from typing import Tuple
import csv
from typing import List


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
        """
            function to paginate data set, index_range is used to determine
            indices. and return a list with the elements
            Args:
                page: page number
                page_size: page size
            Return - list with the right elements
        """
        assert type(page) is int and type(page_size) is int, "AssertionError \
raised when page and/or page_size are not ints"
        assert page > -1 and page_size > -1, "AssertionError raised with \
negative values"
        assert page != 0 and page_size != 0, "AssertionError raised with 0"
        if self.__dataset is None:
            self.dataset()
        indices = index_range(page, page_size)
        start_index = indices[0]
        last_index = indices[1]
        return self.__dataset[start_index:last_index]
