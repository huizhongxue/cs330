"""Computes the nth Fibonnaci number

Parameters
----------
n : the index of the element to be returned from the Fibonnaci sequence
Returns
-------
the nth Fibonnaci number
"""
def fibonnaci_with_recursion(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonnaci_with_recursion(n-1)+fibonnaci_with_recursion(n-2)


"""
Now, try to run the above function with a big input such as 1000. What do you notice?
Draw a tree of the recursion calls. What do you notice??

To get rid of the recursive calls on overlapping subproblems, we could use a memoization table.
"""

#global memoization table
fibonnaci_table = [-1]*10000
fibonnaci_table[0] = 0
fibonnaci_table[1] = 1

"""Computes the nth Fibonnaci number using memoization

Same parameters and inputs as fibonnaci_with_recursion but should handle large numbers quickly
"""
def fibonnaci_with_memoization(n):
    #use the global fibonnaci table
    global fibonnaci_table

    if n == 0: return 0
    elif n == 1: return 1
    elif n >= 2 :
        for i in range(2, n+1, 1):
            fibonnaci_table[i] = fibonnaci_table[i-1] + fibonnaci_table[i-2]
        return fibonnaci_table[n]
    return -1
