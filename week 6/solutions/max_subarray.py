"""
https://leetcode.com/problems/maximum-subarray/description/

Given an integer array nums, find the contiguous subarray with the largest sum, and return its sum.
"""

def maxSubArray(nums: list[int]) -> int:
    curr_max, ret_max = 0, -float("inf")
    for num in nums:
        curr_max += num
        ret_max = max(ret_max, curr_max)
        if curr_max < 0: curr_max = 0
    return ret_max