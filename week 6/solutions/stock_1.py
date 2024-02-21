"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""

def maxProfit(prices: list[int]) -> int:
    best = 0
    curr_min = float('inf')
    for price in prices:
        best = max(best, price - curr_min)
        curr_min = min(curr_min, price)
    return best