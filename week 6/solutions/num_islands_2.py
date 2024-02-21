"""
https://leetcode.com/problems/number-of-islands-ii/description/

A 2d grid map of m rows and n columns is initially filled with water. We may perform an addLand operation which turns the water at position (row, col) into a land. Given a list of positions to operate, count the number of islands after each addLand operation. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

E.g. 
Input: m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]
Output: [1, 1, 2, 3]

0 0 0 
0 0 0
0 0 0

1 0 0
0 0 0   Number of islands = 1
0 0 0

1 1 0
0 0 0   Number of islands = 1
0 0 0

1 1 0
0 0 1   Number of islands = 2
0 0 0

1 1 0
0 0 1   Number of islands = 3
0 1 0
"""


class Union:
    def __init__(self):
        self.id = {}
        self.size = {}
        self.count = 0
    
    def add(self, p):
        if p not in self.id:
            self.id[p] = p
            self.size[p] = 1
            self.count += 1
    
    def root(self, p):
        if p not in self.id: return
        # path compression
        while self.id[p] != self.id[self.id[p]]:
            self.id[p] = self.id[self.id[p]]
        return self.id[p]

    def unite(self, p, q):
        i, j = self.root(p), self.root(q)
        if not i or not j or i == j: return
        # weighted union
        if self.size[i] > self.size[j]:
            i, j = j, i
        self.id[i] = j
        self.size[j] += self.size[i]
        self.count -= 1
    

class Solution:
    def numIslands2(self, m: int, n: int, positions: list[list[int]]) -> list[int]:
        u = Union()
        ret = []
        for p_x, p_y in positions:
            u.add((p_x, p_y))
            for d_x, d_y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                n_x, n_y = p_x + d_x, p_y + d_y
                if n_x < 0 or n_x >= m or n_y < 0 or n_y >= n: continue
                u.unite((n_x, n_y), (p_x, p_y))
            ret.append(u.count)
        return ret