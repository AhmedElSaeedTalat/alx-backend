#!/usr/bin/env python3
""" FIFOCache lifo caching algorithm """
from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """ mrucache algorithm class """
    def __init__(self):
        """ initialise class """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
            put key and item in cach_data
            Args:
                key: key passed
                item: value for the key
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
            self.cache_data.move_to_end(key)
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            data_list = list(self.cache_data.items())
            last_pair = data_list[-1]
            last_key = last_pair[0]
            del self.cache_data[last_key]
            print('DISCARD:', last_key)
        self.cache_data[key] = item

    def get(self, key):
        """
            get the value of the key
            Args:
                @key: key passed
            Return - value of the key
        """
        if key is None:
            return None
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
        return None
