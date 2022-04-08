# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 17:41:41 2020

@author: scker
"""

def perimeter(x):
    """
    requests user to enter length for x sides in shape
    returns perimeter of shape
    """
    perim = 0
    for i in range(x):
        length = float(input("Enter side " + str(i + 1) + ":  "))
        perim += length
    return perim

function = perimeter(4)