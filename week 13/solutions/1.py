"""
https://leetcode.com/problems/find-median-from-data-stream/description/
"""


from heapq import heappush, heappushpop

class MedianFinder:

    def __init__(self):
        self.small = [] # max heap
        self.large = [] # min heap
        

    def addNum(self, num: int) -> None:
        if len(self.small) < len(self.large):
            # new num goes into self.small
            heappush(self.small, -heappushpop(self.large, num))
        else:
            # new num goes into self.large
            heappush(self.large, -heappushpop(self.small, -num))
        

    def findMedian(self) -> float:
        if len(self.small) < len(self.large):
            return self.large[0]
        else:
            return (self.large[0] + (-self.small[0]))/2