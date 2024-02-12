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
