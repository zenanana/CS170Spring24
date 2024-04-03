"""
https://leetcode.com/problems/knight-dialer/description/

We have a chess knight and a phone pad. The knight can only stand on a numeric cell.

Given an integer n, return how many distinct phone numbers of length n we can dial.

You are allowed to place the knight on any numeric cell initially and then you should perform n - 1 jumps to dial a number of length n. All jumps should be valid knight jumps.

As the answer may be very large, return the answer modulo 10^9 + 7.

Example 1:
    Input: n = 1
    Output: 10
    Explanation: We need to dial a number of length 1, so placing the knight over any numeric cell of the 10 cells is sufficient.

Example 2:
    Input: n = 2
    Output: 20
    Explanation: All the valid number we can dial are [04, 06, 16, 18, 27, 29, 34, 38, 40, 43, 49, 60, 61, 67, 72, 76, 81, 83, 92, 94]
"""


"""
## HELPER
mod = 10**9 + 7
pad_mapping = dict()
pad_mapping[0] = [4,6]
pad_mapping[1] = [6,8]
pad_mapping[2] = [7,9]
pad_mapping[3] = [4,8]
pad_mapping[4] = [3,9,0]
pad_mapping[5] = []
pad_mapping[6] = [1,7,0]
pad_mapping[7] = [2,6]
pad_mapping[8] = [1,3]
pad_mapping[9] = [2,4]
"""