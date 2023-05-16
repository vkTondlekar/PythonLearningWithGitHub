# -*- coding: utf-8 -*-
"""
Created on Tue May  9 12:05:20 2023

@author: vtondlekar
"""

x = int(input())
y = int(input())

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, (x%y))
print("GCD is: ", gcd(x, y))

def lcm(x, y):
    lcm = (x * y)//gcd(x, y)
    return lcm
print("LCM is :", lcm(x, y))