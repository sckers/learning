# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 22:07:19 2020

@author: scker
"""

import math
print("Welcome to the simple math helper.")
print("What would you like to calculate?")
print("1. Square Root")
print("2. Log")
print("3. Factorial")
calc = int(input())
if calc == 1:
    x = float(input("Enter the number to square root:  "))
    ans = math.sqrt(x)
elif calc == 2:
    x = float(input("Enter the number to log:  "))
    ans = math.log10(x)
elif calc == 3:
    x = float(input("Enter the number to factorial:  "))
    ans = math.factorial(x)
print(ans)