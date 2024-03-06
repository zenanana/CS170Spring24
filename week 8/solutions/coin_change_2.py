"""
https://leetcode.com/problems/coin-change-ii/description/

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.

Example:
Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
"""

def change(amount: int, coins: list[int]) -> int:
    # recurrence relation: ans(amount=n, coins=[:j]) = sum(ans(amount=(n-coins[j-1]), coins=[:j]), ans(amount=n, coins=[:j-1]))
    # explanation: we can visualize all combinations as being sorted from smallest to largest coins used
    
    memo = {}
    def helper(amt, c):
        if c == -1 or amt < 0: return 0
        if amt == 0: return 1
        if (k := (amt, c)) in memo: return memo[k]
        res = helper(amt-coins[c], c) + helper(amt, c-1)
        memo[k] = res
        return res

    return helper(amount, len(coins)-1)