"""
https://leetcode.com/problems/merge-intervals/description/

Given an array of intervals where intervals[i] = [start_i, end_i], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

E.g.
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
"""

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals = sorted(intervals, key=lambda interval: interval[0])
        output = []
        currInterval = intervals[0]
        for i in range(1, len(intervals)):
            nextInterval = intervals[i]
            if currInterval[1] >= nextInterval[0]:
                # curr: [    ]
                # next:   [ ]  ]
                # extend current interval
                if nextInterval[1] >= currInterval[1]:
                    # curr: [   ]
                    # next:   [   ]
                    currInterval[1] = nextInterval[1]
                else:
                    # curr: [    ]
                    # next:   []
                    continue
            elif nextInterval[0] > currInterval[1]:
                # curr: [   ]
                # next:       [   ]
                # append current interval
                output.append(currInterval)
                currInterval = nextInterval
        output.append(currInterval)
        return output
    
    def alternative(self, intervals: list[list[int]]) -> list[list[int]]:
        # sort
        intervals.sort()

        # run through
        def overlaps(int1, int2):
            return max(int1[0], int2[0]) <= min(int1[1], int2[1])
            
        i = 0
        n = len(intervals)
        res = []
        while i < n:
            base = intervals[i]
            i += 1
            while i < n and overlaps(base, intervals[i]):
                base = [min(base[0], intervals[i][0]), max(base[1], intervals[i][1])]
                i += 1
            res.append(base)
        return res

