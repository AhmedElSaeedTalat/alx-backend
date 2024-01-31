#!/usr/bin/env python3
""" FIFOCache lifo caching algorithm """
from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    """ lfucache algorithm class """
    def __init__(self):
        """ initialise class """
        super().__init__()
        self.cache_data = OrderedDict()
        self.count = OrderedDict()

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
            self.count[key] += 1
            self.cache_data[key] = item
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            minumum_num = min(self.count.values())
            for k, v in self.count.items():
                if v == minumum_num:
                    key_toDelete = k
                    break
            del self.cache_data[key_toDelete]
            del self.count[key_toDelete]
            print('DISCARD:', key_toDelete)
        self.count[key] = 0
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
            self.count[key] += 1
            return self.cache_data[key]
        return None
