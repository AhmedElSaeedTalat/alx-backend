#!/usr/bin/env python3
""" FIFOCache fifo caching algorithm """
from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """ fifo cach class """
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
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            first_key = next(iter(self.cache_data))
            del self.cache_data[first_key]
            print('DISCARD:', first_key)
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
            return self.cache_data[key]
        return None
