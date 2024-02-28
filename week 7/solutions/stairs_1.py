"""
https://leetcode.com/problems/climbing-stairs/description/

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

E.g.
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""

class Solution:
    def topDown(self, n: int) -> int:
        memo = [-1 for _ in range(n + 1)]
    
        def helper(x):
            if memo[x] != -1: return memo[x]
            if x <= 1: return 1
            ways = helper(x-1) + helper(x-2)
            memo[x] = ways
            return ways

        return helper(n)
    
    def bottomUp(self, n: int) -> int:
        if n <= 1: return 1
        dp = [0 for _ in range(n)]
        dp[0] = 1
        dp[1] = 2

        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[-1]
