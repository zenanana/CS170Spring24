"""
https://leetcode.com/problems/trapping-rain-water/description/

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""


def trap(height: list[int]) -> int:
    n = len(height)
    l, r = 0, n-1
    l_max, r_max = 0, 0

    trapped = 0
    while l != r:
        l_max, r_max = max(l_max, height[l]), max(r_max, height[r])
        if height[l] < height[r]:
            trapped += max(0, min(l_max, r_max) - height[l])
            l += 1
        else:
            trapped += max(0, min(l_max, r_max) - height[r])
            r -= 1
    return trapped



