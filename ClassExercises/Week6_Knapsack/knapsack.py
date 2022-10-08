"""
Programmer: Chris Tralie
Purpose: To show a dynamic programming solution to the 0-1 knapsack problem
with backtracing that uses O(capacity * len(items)) time and space, and to 
apply this to find a "non-flourishing" solution to a change problem
"""

def knapsack(capacity, weights, values):
    """
    Perform the 0-1 knapsack problem with backtracing

    Parameters
    ----------
    capacity: int
        Capacity of the knapsack
    weights: list of N ints
        List of weights of items in backpack
    values: list of N floats
        Parallel list of values of each item
    
    Returns
    -------
    float: Biggest value we can fit in the knapsack,
    list of int: Indices of items that achieve the above value
    """
    ## Step 1: Setup Dynamic Programming Tables
    N = len(weights)
    # Create a dynamic programming table with items down the rows and capacities across the columns
    # This is why capacity and weights have to be ints...we take all sub-capacities from 
    # 0, 1, 2, ..., capacity
    # Base cases are 0 in the top row (no elements in use) and 0 in the leftmost column (capacity 0)
    table = [[0]*(capacity+1) for i in range(N+1)]
    # Also store a matrix indicating whether a particular item is chosen 
    # This can be used for backtracing
    included = [[0]*(capacity+1) for i in range(N+1)]
    
    
    ## Step 2: Apply recurrence rules
    for item_i in range(1, N+1):
        for capacity_j in range(1, capacity+1): # Consider all sub_capacities from 1 to capacity
            if weights[item_i-1] <= capacity_j:
                # Case 1: We take this item.  Look at the subproblem using everything up to but
                # not including this element, with a capacity of capacity_j - the weight of this item,
                # plus the value of this item since we're including it
                # We index with item_i-1 since the first row is the null item
                case1 = table[item_i-1][capacity_j - weights[item_i-1]] + values[item_i-1]
                # Case 2: We don't include the item.  In this case, we look to the best solution
                # of everything up to but not including this item
                case2 = table[item_i-1][capacity_j]
                if case1 > case2:
                    table[item_i][capacity_j] = case1
                    included[item_i][capacity_j] = 1
                else:
                    table[item_i][capacity_j] = case2
            else:
                # If we can't fit this item into this capacity, look at the best
                # solution so far of this capacity that doesn't use this item
                table[item_i][capacity_j] = table[item_i-1][capacity_j]
        
    ## Step 3: Backtrace solution to find optimal items:
    optimal_items = []
    item_i = N
    capacity_j = capacity
    while item_i > 0 and capacity_j > 0:
        if included[item_i][capacity_j]:
            optimal_items.append(item_i-1)
            capacity_j -= weights[item_i-1]
        item_i -= 1
    # Make sure this is actually an optimal solution
    assert(sum([values[i] for i in optimal_items]) == table[-1][-1])
    return table[-1][-1], sorted(optimal_items)


def knapsack_test():
    # Test suggested at https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
    capacity = 50
    weights = [10, 20, 30]
    values = [60, 100, 120]
    value, optimal_items = knapsack(capacity, weights, values)
    print(value, optimal_items)

knapsack_test()