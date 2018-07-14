# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 23:57:49 2018

@author: Souvik Banerjee
"""

def fiblist(n):
    """
    int -> list
    Computing Fibonacci numbers
    >> fiblist(4)
    [0, 1, 1, 2, 3]
    
    >> fiblist(8)
    [0, 1, 1, 2, 3, 5, 8, 13, 21]
    """
    # Empty list
    result = []
    # Set the first and second element of the list as 0 and 1
    result.append(0)
    result.append(1)
    # set sum to 0
    final_sum = 0
    for i in range(2,n+1):
        final_sum = result[i-1] + result[i-2]
        result.append(final_sum)
    return result