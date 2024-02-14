"""
https://leetcode.com/problems/alien-dictionary/description/

There is a foreign language language which uses the latin alphabet, but the order among letters is not "a", "b", "c" ... "z" as in English.

You receive a list of non-empty strings words from the dictionary, where the words are sorted lexicographically based on the rules of this new language.

Derive the order of letters in this language. If the order is invalid, return an empty string. If there are multiple valid order of letters, return any of them.

A string a is lexicographically smaller than a string b if either of the following is true:
- The first letter where they differ is smaller in a than in b.
- There is no index i such that a[i] != b[i] and a.length < b.length.

Example 1:
    Input: ["z","o"]
    Output: "zo"

Example 2:
    Input: ["hrn","hrf","er","enn","rfnn"]
    Output: "hernf"
"""

import queue
def foreignDictionary(words: list[str]) -> str:
    # process input
    adj = {char: set() for word in words for char in word}
    inorders = {char: 0 for word in words for char in word}
    n = len(words)
    for i in range(n-1):
        word_1, word_2 = words[i], words[i+1]
        m = min(len(word_1), len(word_2))
        if len(word_1) > len(word_2) and word_1[:m] == word_2[:m]:
            return ""
        
        for j in range(m):
            if word_1[j] != word_2[j]:
                if word_2[j] not in adj[word_1[j]]:
                    inorders[word_2[j]] += 1
                adj[word_1[j]].add(word_2[j])
                break

    # topological sort
    top_order = []
    q = queue.Queue()
    for u in inorders:
        if inorders[u] == 0: 
            q.put(u)
    while not q.empty():
        u = q.get()
        top_order.append(u)
        for v in adj[u]:
            inorders[v] -= 1
            if inorders[v] == 0: q.put(v)
    
    if len(top_order) != len(inorders): return ""

    return "".join(top_order)