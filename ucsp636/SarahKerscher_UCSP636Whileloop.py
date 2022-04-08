# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 20:44:10 2020

@author: scker
"""

length = 0
perim = 0
print("This program will determine the perimeter from the length of sides that you enter.")
while length != -1:
    perim += length
    length = float(input("Enter the length of the next side (enter -1 when finished):  "))
print("The perimeter of your shape is " + str(perim))