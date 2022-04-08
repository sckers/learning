# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 05:36:34 2020

@author: scker
"""

#%% problem 1
#Test case
balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

#My code
monthIR = annualInterestRate / 12.0
for i in range(12):
    monthpay = balance * monthlyPaymentRate
    monthub = balance - monthpay
    balance = monthub + monthIR * monthub
print("Remaining balance: " + str(round(balance, 2)))

#%% problem 2
#Test Case
balance = 3926
annualInterestRate = 0.2

#My code
monthIR = annualInterestRate / 12.0
fixedpay = 0
upbal = balance
while upbal > 0:
    for i in range(12):
        monthub = upbal - fixedpay
        upbal = monthub + monthIR * monthub
    if upbal > 0:
        upbal = balance
        fixedpay += 10
        
print("Lowest payment: " + str(fixedpay))

#%% problem 3
#Test case
balance = 999999
annualInterestRate = 0.18

#My code
monthIR = annualInterestRate / 12.0
upbal = balance
low = balance / 12
high = balance * (1 + monthIR)**12 / 12
payment = (low + high) / 2
epsilon = 0.01

while abs(upbal) >= epsilon:
    upbal = balance
    for i in range(12):
        monthub = upbal - payment
        upbal = monthub + monthIR * monthub
    if abs(upbal) < epsilon:
        break
    else:
        if upbal > 0:
            low = payment
        else:
            high = payment
    payment = (low + high) / 2
print("Lowest payment: " + str(round(payment, 2)))
