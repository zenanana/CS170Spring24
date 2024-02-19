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