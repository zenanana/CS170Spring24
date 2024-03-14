"""
https://leetcode.com/problems/edit-distance/description/

Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:
- Insert a character
- Delete a character
- Replace a character
 

Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Constraints:
- 0 <= word1.length, word2.length <= 500
- word1 and word2 consist of lowercase English letters.
"""


from functools import lru_cache

def minDistance(s1: str, s2: str) -> int:
    @lru_cache(None)
    def dp(i, j):
        if i == 0: return j
        if j == 0: return i
        if s1[i-1] == s2[j-1]: return dp(i-1, j-1)
        return min(dp(i-1, j), dp(i, j-1), dp(i-1, j-1)) + 1
    
    return dp(len(s1), len(s2))



