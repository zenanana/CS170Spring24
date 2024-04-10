"""
https://leetcode.com/problems/minimum-costs-using-the-train-line/description/
"""

from functools import lru_cache

class Solution:
    def minimumCosts(self, regular: list[int], express: list[int], expressCost: int) -> list[int]:
        n = len(regular)

        @lru_cache(None)
        def dp(i: int, reg: bool):
            if i == -1 and reg: return 0
            if i == -1 and not reg: return expressCost

            if reg:
                a = dp(i-1, False) + express[i] # come from prev expr and then transfer from expr to reg
                b = dp(i-1, True) + regular[i] # come from prev reg
                return min(a, b)
            else:
                a = dp(i-1, True) + regular[i] + expressCost # come from prev reg and then transfer from reg to expr
                b = dp(i-1, False) + express[i] # come from prev expr
                return min(a, b)
            
        res = [0 for _ in range(n)]
        r, e = 0, expressCost
        for i in range(0, n):
            r_new = min(r + regular[i], e + express[i])
            e_new = min(r + regular[i] + expressCost, e + express[i])
            r, e = r_new, e_new
            res[i] = min(r, e)

        return res