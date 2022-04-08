# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#%% Problem 1
s = "abcdefghijklmnopqrstuvwxyz"
numvow = 0
for letter in s:
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
        numvow += 1
print("Number of vowels: " + str(numvow))