#!/usr/bin/env python3
""" baseCaching module"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """fifo Cache defines a FIFO caching system"""

    def __init__(self):
        """Initialization"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """cache a key-value pair"""
        if key is None or item is None:
            pass
        else:
            leng = len(self.cache_data)
            if leng >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                print("DISCARD: {}".format(self.order[0]))
                del self.cache_data[self.order[0]]
                del self.order[0]
            self.order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """return the value linked to a given key"""
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
