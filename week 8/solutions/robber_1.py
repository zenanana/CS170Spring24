"""
https://leetcode.com/problems/house-robber/description/

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
"""

def bottom_up(nums: list[int]) -> int:
    # recursive relation: ans(house_i) = max(ans(house_i-1), ans(house_i-2) + nums[house_i])
    # explanation: max we can rob up to and including house_i is the max of (rob house_i and max till house_i-2) and (don't rob house_i and max till house_i-1)
    n = len(nums)
    dp = [0 for _ in range(n+2)]
    
    for i in range(2, n+2):
        nums_i = i - 2
        dp[i] = max(dp[i-2] + nums[nums_i], dp[i-1])
    
    return dp[-1]


def top_down(nums: list[int]) -> int:
    n = len(nums)
    memo = [-1 for _ in range(n)]

    def helper(n):
        if n <= -1: return 0
        if memo[n] != -1: return memo[n]

        memo[n] = max(helper(n-1), helper(n-2) + nums[n])
        return memo[n]
    
    return helper(n-1)