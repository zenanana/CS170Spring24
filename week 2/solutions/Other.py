"""
There will be some unintuitive solutions that you should memorize. However once memorized, they can be very useful in solving other problems as well.
"""

# Problem 1: Given an array of size n+1 where all elements are in range [0, n-1] and all elements occur once except one number which occurs twice. Find the repeating number.
# Example: [1, 2, 3, 4, 4] -> 4
def findDuplicate(arr):
    hare, tortoise = 0, 0
    while True:
        hare, tortoise = arr[arr[hare]], arr[tortoise]
        if hare == tortoise:
            return hare
