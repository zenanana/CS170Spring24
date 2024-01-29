# LRU/LFU cache are classic coding questions. They appear in interviews all the time. They may seem like extremely loaded questions, but if you follow the process of breaking problems down into smaller components, they should be more manageable.
import helpers

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

"""
Problem 1.2: How can we ensure we perform the LRU eviction policy efficiently?
"""





"""
Problem 2 (LFU Cache): Design an LFU cache. Assume accesses are given in the form of a `key: int`, and a positive `value: int`. The following methods/functions should be fully implemented:
- init(capacity: int): initializes the cache with a set capacity
- get(key: int): returns the value of the key
- put(key: int, value: int): updates the value of the key if it exists, else inserts the key and value into the cache

Hint: Try breaking the question/requirements into smaller components again!
Hint: It is possible to have the `get` and `put` operations done in O(logn) time
"""


"""
Problem 2.1 (LFU Cache): Optimize the LFU cache code such that `get` and `put` operations are constant time.

Hint: Expand on the implementation of LRU cache!
"""
