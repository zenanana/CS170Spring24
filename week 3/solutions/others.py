"""
https://leetcode.com/problems/sum-of-subarray-minimums/
Problem 1: Given an array of integers, find the sum of min(b), where b ranges over every contiguous subarray of arr
Example: arr = [3, 1, 2, 4]
Contiguous subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4].
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
output = 17
"""

def sumSubarrayMins(arr):
    res = 0
    stack = [] # non-decreasing
    arr = [float('-inf')] + arr + [float('-inf')]
    for i, e in enumerate(arr):
        while stack and arr[stack[-1]] > e:
            curr = stack.pop()
            res += arr[curr] * ((i - curr) * (curr - stack[-1]))
        stack.append(i)
    return res