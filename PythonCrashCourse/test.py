# -*- coding: utf-8 -*-
"""
Created on Mon May  8 15:06:05 2023

@author: vtondlekar
"""

def b(z):
    prod = a(z, z)
    print(z, prod)
    return prod

def a(x, y):
    x = x + 1
    return x * y

def c(x, y, z):
    total = x + y + z
    square = b(total)**2

x = 1
y = x + 1
print(c(x, y+3, x+y))