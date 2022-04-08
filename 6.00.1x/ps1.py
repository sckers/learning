# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#%% Problem 1
s = "sarah"
numvow = 0
for letter in s:
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
        numvow += 1
print("Number of vowels: " + str(numvow))

#%% Problem 2
s= "azcbobobegghakl"
bob = 0
x = 0
for letter in s:
    y = x + 3
    if s[x:y] == "bob":
        bob += 1
    x += 1
print("Number of times bob occurs is: " + str(bob))

#%% Problem 3
s = "azcbobobegghakl"
x = 0
y = 1
alpha = s[x]
while s[x] < s[y]:
    alpha = alpha + s[y]
    x += 1
    y += 1
print(alpha)

#%%
s = "azcbobobegghakl"
alpha = s[0]
temp = s[0]

for x in range(len(s)-1):
    if s[x] <= s[x+1]:
        temp += s[x+1]
        if len(temp) > len(alpha):
            alpha = temp
    else:
        temp = s[x+1]

print("Longest substring in alphabetical order is: " + alpha)