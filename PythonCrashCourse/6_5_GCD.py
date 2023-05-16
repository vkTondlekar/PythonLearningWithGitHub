# -*- coding: utf-8 -*-
"""
Created on Tue May  9 11:47:36 2023

@author: vtondlekar
"""
a = int(input())
b = int(input())

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
print("Greatest Common Divisor is :", gcd(a, b))