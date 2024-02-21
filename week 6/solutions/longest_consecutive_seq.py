"""
https://leetcode.com/problems/longest-consecutive-sequence/

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.
"""

class Union:
    def __init__(self):
        self.id = {}
        self.size = {}

    def add(self, p):
        if p in self.id: return None
        self.id[p] = p
        self.size[p] = 1
    
    def root(self, p):
        if p not in self.id: return None
        while self.id[p] != self.id[self.id[p]]:
            self.id[p] = self.id[self.id[p]]
        return self.id[p]
    
    def unite(self, p, q):
        i, j = self.root(p), self.root(q)
        if i is None or j is None or i == j: return -1
        if self.size[i] > self.size[j]:
            i, j = j, i # making sure i is the smaller set so i goes onto j
        self.id[i] = j
        self.size[j] += self.size[i]
        return self.size[j]

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        u = Union()
        res = 0
        for num in nums:
            u.add(num)
            streak = max(u.unite(num, num-1), u.unite(num, num+1))
            res = max(res, streak)
        return res
