#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
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
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """ to update indices and return dataset"""
        assert index > 0 and index < len(self.__dataset), "AssertionError \
raised when out of range"
        if index is None:
            index = 0
        data = self.__dataset
        data = [value for item, value in self.__indexed_dataset.items()]
        data_dict = {}
        data_dict['index'] = index
        last_index = index + page_size
        data = data[index:last_index]
        data_dict['data'] = data
        data_dict['page_size'] = page_size
        data_dict['next_index'] = index + page_size
        return data_dict
