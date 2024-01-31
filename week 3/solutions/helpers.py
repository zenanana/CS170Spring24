class Node:
    def __init__(self, key, val, freq=1):
        self.key = key
        self.val = val
        self.freq = freq
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def len(self):
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
        return count

    def moveToHead(self, node) -> None:
        if node == self.head: return
        elif node == self.tail:
            self.tail = node.prev
            self.tail.next = None
            node.prev = None
            node.next = self.head
            self.head.prev = node
            self.head = node
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            node.prev = None
            node.next = self.head
            self.head.prev = node
            self.head = node
    
    def insertAtHead(self, node) -> None:
        if self.head is None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def removeFromTail(self) -> None:
        if self.head is None: return
        elif self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
    
    def removeFromHead(self) -> None:
        if self.head is None: return
        elif self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
    