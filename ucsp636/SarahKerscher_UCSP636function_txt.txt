# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 16:49:32 2020

@author: scker
"""

def side(x):
    """
    requests user input for side x
    returns input
    """
    length = float(input("Enter side " + str(x) + ":  "))
    return length

print("Enter the lengths for each side of your shape.")

one = side(1)
two = side(2)
three = side(3)
four = side(4)
perimeter = one + two + three + four

if one == two == three == four:
    print("The shape forms a square with a perimeter of " + str(perimeter))
elif one == two and three == four or one == three and two == four or one == four and two == three:
    print("The shape forms a rectangle with a perimeter of " + str(perimeter))
else:
    print("The shape does not form a rectangle or square.")