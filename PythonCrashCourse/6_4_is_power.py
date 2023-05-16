# -*- coding: utf-8 -*-
"""
Created on Tue May  9 09:01:08 2023

@author: vtondlekar
A number, a, is a power of b if it is divisible by b 
and a/b is a power of b. 
Write a function called is_power that takes parameters a and b and returns 
True if a is a power of b. 

Note: you will have to think about the base case.
"""

a = int(input())

b = int(input())

    
def is_power(a, b):
    while a % b == 0:
        if a == b:
            return True
        else:
            return is_power((a/b), b)
    return False
print("is_power returns: ", is_power(a, b))
