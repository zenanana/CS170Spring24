"""
https://leetcode.com/problems/word-ladder/description/
"""

import queue
def ladderLength(beginWord: str, endWord: str, wordList: list[str]) -> int:
    # processing input
    word_set = set(wordList)

    # bfs
    q = queue.Queue()
    q.put(beginWord)
    visited = set([beginWord])
    depth = 0
    
    while not q.empty():
        depth += 1
        for _ in range(q.qsize()):
            curr_w = q.get()
            if curr_w == endWord: return depth
            for i in range(len(curr_w)):
                for j in range(26):
                    next_w = curr_w[:i] + chr(ord('a')+j) + curr_w[i+1:]
                    if next_w in word_set and next_w not in visited:
                        q.put(next_w)
                        visited.add(next_w)


    return 0
