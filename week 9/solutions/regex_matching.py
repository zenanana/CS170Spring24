"""
https://leetcode.com/problems/regular-expression-matching/description/

Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Constraints:
1 <= s.length <= 20
1 <= p.length <= 20
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.
"""
from functools import lru_cache

def top_down(s: str, p: str) -> bool:
    n, m = len(s), len(p)

    @lru_cache(None)
    def helper(i, j):
        if i == -1 and j == -1: return True
        if i == -2 or j == -1: return False
        
        s_c, p_c = s[i], p[j]

        res = False
        if p_c == '.': res = res or helper(i-1, j-1)
        elif p_c == '*':
            p_cc = p[j-1]
            if p_cc == s_c or p_cc == '.': res = res or helper(i-1, j-2) or helper(i-1, j)
            res = res or helper(i, j-2)
        elif p_c == s_c: res = res or helper(i-1, j-1)
        elif p_c != s_c: return False

        return res
    
    return helper(n-1, m-1)