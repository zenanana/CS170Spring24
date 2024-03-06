"""
https://leetcode.com/problems/house-robber-ii/description/

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example:
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
"""

def rob(self, houses: list[int]) -> int:
    if len(houses) == 1: return houses[0]
    
    def top_down(nums: list[int]) -> int:
        n = len(nums)
        memo = [-1 for _ in range(n)]

        def helper(n):
            if n <= -1: return 0
            if memo[n] != -1: return memo[n]

            memo[n] = max(helper(n-1), helper(n-2) + nums[n])
            return memo[n]

        return helper(n-1)

    return max(top_down(houses[1:]), top_down(houses[:-1]))