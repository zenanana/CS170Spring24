# LRU/LFU cache are classic coding questions. They appear in interviews all the time. They may seem like extremely loaded questions, but if you follow the process of breaking problems down into smaller components, they should be more manageable.
import helpers
import heapq
import collections

""" 
Problem 1 (LRU Cache): Design an LRU Cache. Assume accesses are given in the form of a `key: int`, and a positive `value: int`. The following methods/functions should be fully implemented:
- init(capacity: int): initializes the cache with a set capacity
- get(key: int): returns the value of the key
- put(key: int, value: int): updates the value of the key if it exists, else inserts the key and value into the cache

Hint: Break the question/requirements into smaller components! What is the point of a cache? What must we do for evictions if we follow LRU policy?
"""

"""
Problem 1.1: How can we ensure we have efficient cache operations?
"""
# Ans: Hashmap

"""
Problem 1.2: How can we ensure we perform the LRU eviction policy efficiently?
"""
# Ans: DLL

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.freq = helpers.DLL()
    
    def get(self, key):
        if key not in self.cache: return -1
        node = self.cache[key]
        self.freq.moveToHead(node)
        return node.val

    def put(self, key, value):
        if key not in self.cache:
            if len(self.cache) == self.capacity:
                del self.cache[self.freq.tail.key]
                self.freq.removeFromTail()
            newNode = helpers.Node(key, value)
            self.freq.insertAtHead(newNode)
            self.cache[key] = newNode
        else:
            self.cache[key].val = value
            self.freq.moveToHead(self.cache[key])

# Unit Tests
# capacity: 3
# ops: [put(1, 1), put(2, 2), put(3, 3), put(4, 4), get(4), get(3), get(2), get(1), put(5, 5), get(1), get(2), get(3), get(4), get(5)]
# output: [None, None, None, None, 4, 3, 2, -1, None, -1, 2, 3, -1, 5]
            
# test_lru_cache = LRUCache(3)
# print(test_lru_cache.put(1, 1))
# print(test_lru_cache.put(2, 2))
# print(test_lru_cache.put(3, 3))
# print(test_lru_cache.put(4, 4))
# print(test_lru_cache.get(4))
# print(test_lru_cache.get(3))
# print(test_lru_cache.get(2))
# print(test_lru_cache.get(1))
# print(test_lru_cache.put(5, 5))
# print(test_lru_cache.get(1))
# print(test_lru_cache.get(2))
# print(test_lru_cache.get(3))
# print(test_lru_cache.get(4))
# print(test_lru_cache.get(5))




"""
Problem 2 (LFU Cache): Design an LFU cache. Assume accesses are given in the form of a `key: int`, and a positive `value: int`. The following methods/functions should be fully implemented:
- init(capacity: int): initializes the cache with a set capacity
- get(key: int): returns the value of the key
- put(key: int, value: int): updates the value of the key if it exists, else inserts the key and value into the cache

Hint: Try breaking the question/requirements into smaller components again!
Hint: It is possible to have the `get` and `put` operations done in O(logn) time
"""
class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.freq = []

    def get(self, key):
        if key not in self.cache: return -1
        node = self.cache[key]
        node[0] += 1
        heapq.heapify(self.freq)
        return node[2]

    def put(self, key, value):
        if key not in self.cache:
            if len(self.cache) == self.capacity:
                evicted_node = heapq.heappop(self.freq)
                del self.cache[evicted_node[1]]
            node = [1, key, value]
            self.cache[key] = node
            heapq.heappush(self.freq, node)
        else:
            node = self.cache[key]
            node[0] += 1
            node[2] = value
            heapq.heapify(self.freq)

# test_lfu_cache = LFUCache(3)
# print(test_lfu_cache.get(0))
# print(test_lfu_cache.put(1, 1))
# print(test_lfu_cache.put(2, 2))
# print(test_lfu_cache.put(3, 3))
# print(test_lfu_cache.get(2))
# print(test_lfu_cache.get(3))
# print(test_lfu_cache.put(4, 4))
# print(test_lfu_cache.get(1))
# print(test_lfu_cache.get(4))
# print(test_lfu_cache.put(5, 5))
# print(test_lfu_cache.get(2))



"""
Problem 2.1 (LFU Cache): Optimize the LFU cache code such that `get` and `put` operations are constant time.

Hint: Expand on the implementation of LRU cache!
"""
class LFUCache2:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.freq = collections.defaultdict(helpers.DLL)
        self.min_freq = 0

    def get(self, key):
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.freq[node.freq].moveToHead(node)
        self.freq[node.freq].removeFromHead()

        node.freq += 1
        self.freq[node.freq].insertAtHead(node)

        if self.freq[self.min_freq].len() == 0:
            self.min_freq += 1
        
        return node.val
    
    def put(self, key, value):
        if key not in self.cache:
            if len(self.cache) == self.capacity:
                evicted_node = self.freq[self.min_freq].tail
                self.freq[self.min_freq].removeFromTail()
                del self.cache[evicted_node.key]
            node = helpers.Node(key, value)
            self.freq[1].insertAtHead(node)
            self.cache[key] = node
            self.min_freq = 1
        else:
            node = self.cache[key]
            node.val = value
            self.get(key)
            
# test_lfu_cache_2 = LFUCache2(3)
# print(test_lfu_cache_2.get(0))
# print(test_lfu_cache_2.put(1, 1))
# print(test_lfu_cache_2.put(2, 2))
# print(test_lfu_cache_2.put(3, 3))
# print(test_lfu_cache_2.get(2))
# print(test_lfu_cache_2.get(3))
# print(test_lfu_cache_2.put(4, 4))
# print(test_lfu_cache_2.get(1))
# print(test_lfu_cache_2.get(4))
# print(test_lfu_cache_2.put(5, 5))
# print(test_lfu_cache_2.get(2))

