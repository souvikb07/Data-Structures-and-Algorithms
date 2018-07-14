# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 00:41:14 2018

@author: Souvik Banerjee
"""
def euclidgcd(a,b):
    """
    (int,int) -> int
    Return Great common divissior
    >> euclidgcd(357,234)
    3
    >> euclidgcd(2341537,8746812)
    1
    """
    if b == 0:
        return a
    a_dash = a % b
    return euclidgcd(b, a_dash)