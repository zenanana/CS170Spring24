"""
https://leetcode.com/problems/course-schedule-ii/description/
"""
import collections
import queue

class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        indegrees = [0 for i in range(numCourses)]
        adj = collections.defaultdict(list)
        for prereq in prerequisites:
            indegrees[prereq[0]] += 1
            adj[prereq[1]].append(prereq[0])
        
        top_sort = []
        q = queue.Queue()
        
        for v, indegree in enumerate(indegrees):
            if indegree == 0: q.put(v)


        while not q.empty():
            v = q.get()
            for u in adj[v]:
                indegrees[u] -= 1
                if indegrees[u] == 0: q.put(u)
            top_sort.append(v)

        if len(top_sort) != numCourses: return []
        return top_sort

        
