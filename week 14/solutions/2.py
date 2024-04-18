"""
https://leetcode.com/problems/sliding-window-maximum/

239. Sliding Window Maximum
"""

from collections import deque
def maxSlidingWindow(nums: list[int], k: int) -> list[int]:
    res = []

    dq = deque() # stores indices of elements in nums
    for i, n in enumerate(nums):
        while dq and nums[dq[-1]] < n:
            dq.pop()
        dq.append(i)

        if dq[0] <= i - k:
            dq.popleft()
        
        if i >= k - 1:
            res.append(nums[dq[0]])
        
    return res