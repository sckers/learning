# -*- coding: utf-8 -*-
"""
Created on Sun May 10 20:23:08 2020

@author: scker
"""

print("Welcome to the winning card program.")
import array
persona = array.array('d',[])
personb = array.array('d',[])

year = 1
while year < 6:
    a = float(input("Enter the salary for individual 1 in year " + str(year) + ":  "))
    b = float(input("Enter the salary for individual 2 in year " + str(year) + ":  "))
    if a != b:
        persona.append(a)
        personb.append(b)
        year = year + 1
    else:
        print("Error: Salaries for each individual in a given year cannot be the same. Please re-enter the salaries.")

if sum(persona) > sum(personb):
    print("Individual 1 has the highest salary.")
elif sum(persona) < sum(personb):
    print("Individual 2 has the highest salary.")
else:
    print("Both individuals have the same salary")