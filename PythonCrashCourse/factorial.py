# -*- coding: utf-8 -*-
"""
Created on Mon May  8 13:35:21 2023

@author: vtondlekar
"""

num = int (input())

fact = 1
i = 1

while (i <= num):
    fact = fact*i
    i = i + 1

print("Factorial of",+num ,"is", fact)