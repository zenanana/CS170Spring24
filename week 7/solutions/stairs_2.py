"""
https://leetcode.com/problems/min-cost-climbing-stairs/description/

You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor (top means index n).

E.g.
Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1. Pay 15 and climb two steps to reach the top. The total cost is 15.
"""

class Solution:
    def topDown(self, cost: list[int]) -> int:
        n = len(cost)
        memo = [-1 for _ in range(n+1)]

        def helper(x):
            if x <= 1: return 0
            if memo[x] != -1: return memo[x]
            min_cost = min(helper(x-1) + cost[x-1], helper(x-2) + cost[x-2])
            memo[x] = min_cost
            return min_cost

        return helper(n)
    
    def bottomUp(self, cost: list[int]) -> int:
        n = len(cost)
        dp = [0 for i in range(n+1)]

        for i in range(2, n+1):
            dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])

        return dp[n]
