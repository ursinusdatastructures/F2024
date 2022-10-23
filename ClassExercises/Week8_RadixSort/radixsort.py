import numpy as np

def get_digit(x, i, b):
    """
    Get the b^i's place in x (Josh's idea)
    """
    return (x//b**i)%b

def radix_sort(arr, b=10):
    M = max(arr)+1
    rounds = int(np.ceil(np.log(M)/np.log(b)))
    res = arr.copy()
    for i in range(rounds):
        # Step 0: Setup the buckets
        buckets = []
        for k in range(b):
            buckets.append([]) 
        # Step 1: Put all of the numbers into buckets according to their digit
        for x in res:
            bucket = get_digit(x, i, b)
            buckets[bucket].append(x)
        # Step 2: Setup the output array
        res = np.array([0]*len(arr))
        # Step 3: Put the elments in each bucket in the final array in order
        # of buckets
        start = 0
        for elems in buckets: # M times looping
            res[start:start+len(elems)] = elems # N operations total
            start += len(elems)
        print("Round", i, ":", res)
    return res



arr = [684,559,629,192,835,763,707,359,9,723,277,754,804,599,70,472,600,396,314,705]
print(radix_sort(arr))
