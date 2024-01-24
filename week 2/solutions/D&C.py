"""
Main idea of D&C: break big problem into smaller ones. Solve each independently.
With enough practice, D&C should come naturally without much explicit thought. This is also true because a lot of coding questions use D&C innately.
"""
# Problem 1: Given an unsorted array of numbers and an integer k, find the kth smallest element of the array. 
# Example: [1, 3, 4, 2, 5], k = 2 -> 4
def kthSmallest(arr, k):
    if len(arr) == 1: return arr[0]
    
    pivot = arr[0]
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    equal = [x for x in arr if x == pivot]

    if k <= len(left):
        return kthSmallest(left, k)
    elif k <= len(left) + len(equal):
        return pivot
    else:
        return kthSmallest(right, k - len(left) - len(equal))

# Problem 1.1: What is the runtime?