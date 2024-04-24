"""
https://leetcode.com/problems/snapshot-array/description/

1146. Snapshot Array
"""

from bisect import bisect_right

class SnapshotArray:

    def __init__(self, length: int):
        self.S = [[(-1, 0)] for _ in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.S[index].append((self.snap_id, val))

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1


    def get(self, index: int, snap_id: int) -> int:
        i = bisect_right(self.S[index], (snap_id, float("inf"))) - 1
        return self.S[index][i][1]
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)