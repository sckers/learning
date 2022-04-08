# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 05:09:28 2020

@author: scker
"""

from math import *
def polysum(n, s):
    """
    n: number of sides
    s: length of sides
    return: sum of area and square of perimeter rounded to four decimal places
    """
    area = 0.25*n*s**2 / tan(pi/n)
    perim = n*s
    return round(area + perim**2, 4)