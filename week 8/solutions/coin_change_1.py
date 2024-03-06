"""
https://leetcode.com/problems/coin-change/description/

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
"""

def top_down(coins: list[int], amount: int) -> int:
    # recursive relation: ans(amount=n) = 1 + min(amount(amount=(n-coins[i])))
    memo = [-1 for _ in range(amount+1)]
    memo[0] = 0

    def helper(amt):
        if memo[amt] != -1: return memo[amt]
        res = float("inf")
        for coin in coins:
            if amt - coin < 0: continue
            res = min(res, 1 + helper(amt - coin))
        memo[amt] = res
        return res
    
    return -1 if (res := helper(amount)) == float('inf') else res

def bottom_up(coins: list[int], amount: int) -> int:
    # recursive relation: ans(amount=n) = 1 + min(amount(amount=(n-coins[i])))
    n = amount
    dp = [float("inf") for _ in range(n+1)]
    dp[0] = 0

    for i in range(1, n+1):
        for coin in coins:
            if (i - coin) < 0: continue
            dp[i] = min(dp[i], 1+dp[i-coin])

    return -1 if (res := dp[-1]) == float("inf") else res