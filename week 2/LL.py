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

# printList(ll.head)
""" BOILERPLATE END """


# Problem 1: Given a linked list, write a function that returns the length of the linked list.





# Problem 2: Given a linked list and an integer k, write a function that returns the kth node from the end of the linked list. Use the length function you wrote above.
# what should you be clarifying?





# Problem 2.1: What is the runtime of your solution? How many passes does it make over the linked list? Can you do better?




# Problem 3: Optimize Problem 2





# Optional: Both 2 and 3 are about O(2n). Is there a preferable solution between the two if you know k is small? Why?



# Optional (Whiteboarding exercise): Implement an LRU cache (https://leetcode.com/problems/lru-cache/description/). 
# LRUCache(int capacity): initialize the cache with positive size capacity
# int get(int key): return the value of the key if the key exists, otherwise return -1
# void put(int key, int value): update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.