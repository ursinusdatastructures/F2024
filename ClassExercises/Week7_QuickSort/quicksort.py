def swap(arr, i, j):
    """
    Swap two elements in an array
    
    Parameters
    ----------
    arr: list
        The array
    i: int
        Index of first element
    j: int
        Index of second element
    """
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def quicksort_rec(arr, lo, hi, cmp):
    """
    Recursively sort an array in-place using the Lomuto partitioning
    scheme
    
    Parameters
    ----------
    arr: list
        Array to sort
    lo: int
        Lowest index of the chunk to sort
    hi: int
        Highest index of the chunk to sort
    cmp: function(obj1, obj2) -> boolean
        A comparator
    """
    if lo < hi:
        pivot = arr[hi]
        i = lo
        for j in range(lo, hi+1):
            if cmp(arr[j], pivot) < 0:
                swap(arr, i, j)
                i += 1
        swap(arr, i, hi)
        quicksort_rec(arr, lo, i-1, cmp)
        quicksort_rec(arr, i+1, hi, cmp)

def quicksort(arr, cmp):
    """
    An entry point for in-place quicksort using the Lomuto 
    partitioning scheme
    
    Parameters
    ----------
    arr: list
        Array to sort
    cmp: function(obj1, obj2) -> boolean
        A comparator
    """
    quicksort_rec(arr, 0, len(arr)-1, cmp)

import numpy as np
np.random.seed(0)
arr = np.random.randint(0, 100, 20)
quicksort(arr, lambda x, y: x - y)
print(arr)
    
