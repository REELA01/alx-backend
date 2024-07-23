#!/usr/bin/env python3
""" baseCaching module"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """fifo cache defines a FIFO caching system"""

    def __init__(self):
        """initialization"""
        super().__init__()
        self.usage = []
        self.frequency = {}

    def put(self, key, item):
        """cache a key-value pair"""
        if key is None or item is None:
            pass
        else:
            leng = len(self.cache_data)
            if leng >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                lfu = min(self.frequency.values())
                lfu_kys = []
                for k, v in self.frequency.items():
                    if v == lfu:
                        lfu_kys.append(k)
                if len(lfu_kys) > 1:
                    lru_lfu = {}
                    for k in lfu_kys:
                        lru_lfu[k] = self.usage.index(k)
                    discard = min(lru_lfu.values())
                    discard = self.usage[discard]
                else:
                    discard = lfu_kys[0]
                print("DISCARD: {}".format(discard))
                del self.cache_data[discard]
                del self.usage[self.usage.index(discard)]
                del self.frequency[discard]
            if key in self.frequency:
                self.frequency[key] += 1
            else:
                self.frequency[key] = 1
            if key in self.usage:
                del self.usage[self.usage.index(key)]
            self.usage.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """return the value linked to a given key"""
        if key is not None and key in self.cache_data.keys():
            del self.usage[self.usage.index(key)]
            self.usage.append(key)
            self.frequency[key] += 1
            return self.cache_data[key]
        return None
