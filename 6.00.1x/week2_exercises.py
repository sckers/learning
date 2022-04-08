# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 04:13:05 2020

@author: scker
"""
#%% Guess my number
print("Please think of a number between 0 and 100!")
low = 0
high = 100
guess = int((high + low) / 2)

print("Is your secret number " + str(guess) + "?")
ans = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
while ans != "c":
    if ans == "h":
        high = guess
        guess = int((high + low) / 2)
    elif ans == "l":
        low = guess
        guess = int((low + high) / 2)
    else:
        print("Sorry, I did not understand your input.")
    print("Is your secret number " + str(guess) + "?")
    ans = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
if ans == "c":
    print("Game over. Your secret number was: " + str(guess))
    
#%% square
def square(x):
    """
    x: int or float
    """
    return x**2
square(2)

#%%eval quadratic
def evalQuadratic(a, b, c, x):
    """
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic
    """
    return (a*(x**2)) + (b*x) + c
evalQuadratic(1, 1, 2, 1)

#%%
def h(x):
    x = x + 1
    print(x)
    
h

#%%
def iterPower(base, exp):
    """
    base: int or float
    exp: int >= 0
    
    returns: int or float, base^exp
    """
    ans = 1
    if exp == 0:
        ans = 1
    while exp > 0:
        ans = ans*base
        exp -= 1
    
    return ans

#%%
def recurPower(base, exp):
    if exp == 0:
        return 1
    else:
        return base*recurPower(base, exp-1)
    
#%%
def gcdIter(a,b):
    if a <= b:
        test = a
    else:
        test = b
    while a % test != 0 or b % test != 0:
        test -= 1
    return test

a = 17
b = 12
print("The GCD of " + str(a) + " and " + str(b) + " is " + str(gcdIter(a,b)))

#%%
def gcdRecur(a,b):
    if b == 0:
        return a
    else:
        return gcdRecur(b, a%b)

a = 17
b = 12
print("The GCD of " + str(a) + " and " + str(b) + " is " + str(gcdRecur(a,b)))

#%% is in
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if aStr == "":
        return False
    elif char == aStr[len(aStr)//2]:
        return True
    elif len(aStr) > 1:
        if char < aStr[len(aStr)//2]:
            return isIn(char, aStr[0:len(aStr)//2])
        else:
            return isIn(char, aStr[len(aStr)//2:len(aStr)])
    else:
        return False
    
#%% Grader
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