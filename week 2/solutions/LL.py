""" BOILERPLATE START """
class Node:
    def __init__(self, data) :
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

def insert(head, data):
    if head == None:
        head = Node(data)
    else:
        head.next = insert(head.next, data)
    return head

def printList(head):
    print_str = ""
    while head != None:
        print_str += str(head.data) + " "
        head = head.next
    print(print_str)

ll = LinkedList()
for i in range(9, -1, -1):
    ll.head = insert(ll.head, i)

printList(ll.head)
""" BOILERPLATE END """


# Problem 1: Write a function that takes in a linked list and returns the length of the linked list.
def length(head):
    if head == None:
        return 0
    else:
        return 1 + length(head.next)

# Problem 2: Write a function that takes in a linked list and an integer k and returns the kth node from the end of the linked list. Use the length function you wrote above.
# what should you be clarifying?
def kthFromEnd(head, k):
    n = length(head)
    for i in range(n - k):
        head = head.next
    return head

# Problem 2.1: What is the runtime of your solution? How many passes does it make over the linked list? Can you do better?


# Problem 3: Optimize Problem 2
def kthFromEndOptimized(head, k):
    lag = head
    for _ in range(k):
        head = head.next
    while head != None:
        head = head.next
        lag = lag.next
    return lag

# Optional: Both 2 and 3 are about O(2n). Is there a preferable solution between the two if you know k is small? Why?
# Ans: 3 is better because it only makes one pass over the linked list. Traversing a LL is expensive because you have to follow the pointers that are not in cache and at vastly different locations in memory. 3 keeps two pointers (lag & head) that are k distance apart, meaning it is likely that each time lag updates, it will already be in cache.

# Optional (Whiteboarding exercise): Implement an LRU cache (https://leetcode.com/problems/lru-cache/description/). 
# LRUCache(int capacity): initialize the cache with positive size capacity
# int get(int key): return the value of the key if the key exists, otherwise return -1
# void put(int key, int value): update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
# Ans: Break this down into two main components. 1) get() method needs to be fast. 2) put() method should also be fast.
# 1) get() method: Fast direct access with hashmap
# 2) put() method: Fast eviction and update with doubly linked list (heap is overkill, using an element just means putting it at the end of the list as it is the most recently used)
# Join these together -> hashmap of doubly linked list nodes