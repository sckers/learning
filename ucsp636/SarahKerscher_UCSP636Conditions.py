# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 20:01:48 2020

@author: scker
"""

print("This program will determine if three angles can form a triangle.")
x = float(input("Enter angle 1:  "))
y = float(input("Enter angle 2:  "))
z = float(input("Enter angle 3:  "))
angles = x + y + z
if angles < 180:
    print("No, it does not form a triangle as these angles are less than 180.")
elif angles > 180:
    print("No, it does not form a triangle as these angles are more than 180.")
else:
    print("Yes, it does form a triangle as these angles are equal to 180.")