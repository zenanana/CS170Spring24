"""
https://leetcode.com/problems/design-hit-counter
https://leetcode.ca/all/362.html

Design a hit counter which counts the number of hits received in the past 5 minutes (i.e., the past 300 seconds).

Your system should accept a timestamp parameter (in seconds granularity), and you may assume that calls are being made to the system in chronological order (i.e., timestamp is monotonically increasing). Several hits may arrive roughly at the same time.

Implement the HitCounter class:

- HitCounter() Initializes the object of the hit counter system.
-void hit(int timestamp) Records a hit that happened at timestamp (in seconds). Several hits may happen at the same timestamp.
- int getHits(int timestamp) Returns the number of hits in the past 5 minutes from timestamp (i.e., the past 300 seconds).
"""

from collections import deque

class HitCounter:
    def __init__(self):
        self.queue = deque()
        self.total = 0

    def hit(self, timestamp: int) -> None:
        self.queue.append(timestamp)
        self.total += 1
        
    def getHits(self, timestamp: int) -> int:
        while self.queue and self.queue[0] <= timestamp - 300:
            self.queue.popleft()
            self.total -= 1
        return self.total
    

"""Follow-up: What if the number of hits per second could be huge? Does your design scale? Try to find a solution that can be implemented in a more efficient way (both space and time)."""

class HitCounter:

    def __init__(self):
        self.timestamps = [-301 for _ in range(300)]
        self.hits = [0 for _ in range(300)]

    def hit(self, timestamp: int) -> None:
        mod_ts = timestamp % 300
        if timestamp - self.timestamps[mod_ts] >= 300:
            self.timestamps[mod_ts] = timestamp
            self.hits[mod_ts] = 1
        else:
            self.hits[mod_ts] += 1
        
    def getHits(self, timestamp: int) -> int:
        total = 0
        for i, v in enumerate(self.hits):
            if timestamp - self.timestamps[i] < 300:
                total += v
        return total
    




    