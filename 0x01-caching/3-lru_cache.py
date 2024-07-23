/usr/bin/env python3
""" baseCaching module"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """fifo cache define a FIFO caching systes"""
    def __init__(self):
        """initialization"""
        super().__init__()
        self.usage = []

    def put(self, key, item):
        """cache a key-value pair"""
        if key is None or item is None:
            pass
        else:
            leng = len(self.cache_data)
            if leng >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                print("DISCARD: {}".format(self.usage[0]))
                del self.cache_data[self.usage[0]]
                del self.usage[0]
            if key in self.usage:
                del self.usage[self.usage.index(key)]
            self.usage.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """return the value linked to a given key"""
        if key is not None and key in self.cache_data.keys():
            del self.usage[self.usage.index(key)]
            self.usage.append(key)
            return self.cache_data[key]
        return None
