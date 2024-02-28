"""
https://leetcode.com/problems/insert-interval/description/

You are given an array of non-overlapping intervals intervals where intervals[i] = [start_i, end_i] represent the start and the end of the ith interval and intervals is sorted in ascending order by start_i. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by start_i and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

E.g.
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
"""

class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        res = []
        for i in intervals:
            if i[1] < newInterval[0]:
                res.append(i)
            elif newInterval[1] < i[0]:
                res.append(newInterval)
                newInterval = i
            else:
                newInterval = [min(i[0], newInterval[0]), max(i[1], newInterval[1])]
        res.append(newInterval)
        return res