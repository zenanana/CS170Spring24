"""
https://leetcode.com/problems/dungeon-game/description/
"""

from functools import lru_cache
def calculateMinimumHP(dungeon: list[list[int]]) -> int:
    m, n = len(dungeon), len(dungeon[0])

    @lru_cache(None)
    def dp(x, y):
        if x == (m-1) and y == (n-1):
            if dungeon[x][y] >= 0: return 1
            else: return -dungeon[x][y] + 1

        health_needed = float('inf')
        if x < (m-1):
            # can go downwards
            health_needed = min(health_needed, dp(x+1, y) - dungeon[x][y])
        if y < (n-1):
            # can go rightwards
            health_needed = min(health_needed, dp(x, y+1) - dungeon[x][y])
        if health_needed <= 0: health_needed = 1

        return health_needed

    return dp(0, 0)