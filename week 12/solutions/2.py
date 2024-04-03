"""
https://leetcode.com/problems/binary-tree-maximum-path-sum/description/

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.
"""

def maxPathSum(root) -> int:
    res = -float('inf')
    def maxSum(node):
        nonlocal res
        if node is None: return 0

        max_left = max(maxSum(node.left), 0)
        max_right = max(maxSum(node.right), 0)
        max_path = max_left + node.val + max_right

        res = max(res, max_path)

        return node.val + max(max_left, max_right)

    maxSum(root)
    return res