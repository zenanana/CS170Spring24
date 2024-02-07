"""
https://leetcode.com/problems/rotting-oranges/description/
"""

import queue

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        n, m = len(grid), len(grid[0])     

        q = queue.Queue()
        num_rotten = 0
        num_oranges = 0
        num_mins = -1

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0: continue
                if grid[i][j] == 2: 
                    q.put((i, j))
                    grid[i][j] = 0
                num_oranges += 1

        if num_rotten == num_oranges: return 0

        while not q.empty():
            for _ in range(q.qsize()):
                rotten = q.get()
                i, j = rotten
                
                if i < 0 or i >= n or j < 0 or j >= m: continue

                for delta_i, delta_j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    x, y = i + delta_i, j + delta_j
                    if x < 0 or x >= n or y < 0 or y >= m or grid[x][y] != 1: continue
                    q.put((x, y))
                    grid[x][y] = 2

                num_rotten += 1
            num_mins += 1

    
        if num_rotten != num_oranges: return -1
        return num_mins