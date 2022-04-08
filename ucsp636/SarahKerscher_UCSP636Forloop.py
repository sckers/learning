# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 15:22:13 2020

@author: scker
"""

index = [1, 2, 3, 4, 5]
print("My Odd and Even Table")
for i in index:
    if i % 2 != 0:
        print(str(i) + " is an odd number.")
    elif i % 2 == 0:
        print(str(i) + " is an even number:")
        print("     Multiplying it by 1 equals " + str(i*1) + ".")
        print("     Multiplying it by 2 equals " + str(i*2) + ".")
print("Done!")