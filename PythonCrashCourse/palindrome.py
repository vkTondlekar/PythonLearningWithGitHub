# -*- coding: utf-8 -*-
"""
Created on Mon May  8 15:47:32 2023

@author: vtondlekar
"""

def first(word):
    return word[0]
"""Returns the first character of a string."""


def last(word):
    return word[-1]
"""Returns the last of a string."""


def middle(word):
    return word[1:-1]
"""Returns all but the first and last characters of a string."""


def is_palindrome(word):
    if len(word) <= 1 :
        return True
    if first(word) != last(word):
        return False
    return is_palindrome(middle(word))
"""Returns True if word is a palindrome."""


print(is_palindrome('vishal'))
print(is_palindrome('bob'))
print(is_palindrome('tomato'))
print(is_palindrome('madam'))