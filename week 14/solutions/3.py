"""
https://leetcode.com/problems/range-addition/description/

370. Range Addition
"""


def getModifiedArray(length: int, updates: list[list[int]]) -> list[int]:
    changes = [0 for _ in range(length + 1)]

    for update in updates:
        start_idx, end_idx, delta = update
        changes[start_idx] += delta
        changes[end_idx+1] -= delta
    
    res = [0 for _ in range(length)]
    running_sum = 0
    for i in range(length):
        running_sum += changes[i]
        res[i] = running_sum

    return res