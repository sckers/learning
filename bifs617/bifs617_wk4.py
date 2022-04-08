# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 09:28:03 2020

@author: kzsj478
"""

#Week 4 Exercises
#Discussion 1: Getting User Input
#Get user input and assign to variables
print("Input 5 numbers.")
a = float(input("First number:  "))
b = float(input("Second number:  "))
c = float(input("Third number:  "))
d = float(input("Fourth number:  "))
e = float(input("Fifth number:  "))

#Perform math operations
sum_all = a + b + c + d + e
avg = sum_all / 5

# Print results
print("\nSum = " + str(sum_all) + "\nAverage = " + str(avg))

#%%Discussion 3: Accessing Array Elements

#make a list with the elements
mylist = ["peroxidase", "gene", "protein", "oxidase", "hemoglobin"]

#print elements
print(mylist[2]+ "\n\n"+ mylist[4])