#!/usr/bin/python3
""" 0-main """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ base cache class """
    def put(self, key, item):
        """
            assign to the dictionary cache_data the item value for the key
            Args:
                @key: key
                @item: item
        """
        if key is None or item is None:
            return
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
