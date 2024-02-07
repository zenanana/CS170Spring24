"""
Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

e.g. grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
] -> 1

e.g. grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
] -> 3
"""

def num_islands(grid):
    islands = 0
    n, m = len(grid), len(grid[0])
    
    def search_island(i, j):
        if i < 0 or i >= n or j < 0 or j >= m: return
        if grid[i][j] == "0": return
        grid[i][j] = "0"
        
        for delta_i, delta_j in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            search_island(i + delta_i, j + delta_j)
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "1":
                islands += 1
                search_island(i, j)
    
    return islands

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(num_islands(grid)) # 3
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print(num_islands(grid)) # 1