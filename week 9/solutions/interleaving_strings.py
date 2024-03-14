"""
https://leetcode.com/problems/interleaving-string/description/

Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where s and t are divided into n and m 
substrings
 respectively, such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...

Example:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Explanation: One way to obtain s3 is:
Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".
Interleaving the two splits, we get "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".
Since s3 can be obtained by interleaving s1 and s2, we return true.
"""

def top_down(s1: str, s2: str, s3: str) -> bool:
    n, m = len(s1), len(s2)

    # edge cases
    if n == 0 and m == 0 and len(s3) == 0: return True
    if n == 0 and m == 0 and len(s3) > 0: return False
    if n + m != len(s3): return False

    memo = {}
    def helper(i, j):
        if i == -1 and j == -1: return True
        if (k := (i, j)) in memo: return memo[k]

        res = False
        if i >= 0:
            if s1[i] == s3[i+j+1]: res = res or helper(i-1, j)
        if j >= 0:
            if s2[j] == s3[i+j+1]: res = res or helper(i, j-1)
        memo[k] = res

        return res

    
    return helper(n-1, m-1)

def bottom_up(s1: str, s2: str, s3: str) -> bool:
    n, m = len(s1), len(s2)

    # edge cases
    if n == 0 and m == 0 and len(s3) == 0: return True
    if n == 0 and m == 0 and len(s3) > 0: return False
    if n + m != len(s3): return False

    dp = [[False for _ in range(m+1)] for _ in range(n+1)]
    dp[0][0] = True

    for i in range(n+1):
        for j in range(m+1):
            if j-1 >= 0 and dp[i][j-1] and s3[i+j-1] == s2[j-1]: dp[i][j] = True
            if i-1 >= 0 and dp[i-1][j] and s3[i+j-1] == s1[i-1]: dp[i][j] = True

    return dp[-1][-1]