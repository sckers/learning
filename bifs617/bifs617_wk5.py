# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 08:35:33 2020

@author: scker
"""

#Week 5 Exercises
#%% Discussion 1: if/else statements

#Request user input
num = int(input("Input a number:\n"))

#test for evenness and print result
if num % 2 == 0:
    print(str(num) + " is even.")
else:
    print(str(num) + " is odd.")
    
#%% Discussion 2: More if/else statements

#Assign my name to a variable
my_name = "Sarah"
    
#Ask user for guess
guess = input("Guess my name!\n")
    
#Test guess and print result
if guess == my_name:
    print("Well done, good guess work!")
else:
    print("Try again next time!")