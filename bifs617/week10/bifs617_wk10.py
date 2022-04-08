# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 18:21:33 2020

@author: scker
"""
# Week 10 Discussions
# Discussion 1: Exercise 1
# Write a program that predicts the fragment lengths that would be generated 
# if AbcI is used to cut the sequence. AbcI cut site is ANT^AAT

import re

file = open(input("Enter the file path and file name that contains the "
                  "sequence:\n"))
filedata = file.read()
sequence = ""
for line in filedata:
    sequence += line.rstrip()
    
AbcI = re.search(r"(A.T)(AAT)", sequence)
seg1 = sequence[:AbcI.start(2)]
seg2 = sequence[AbcI.start(2):]

print("The first segment is " + str(len(seg1)) + " nucleotides.\nThe second "
      "segment is " + str(len(seg2)) + " nucleotides.")
print("segment 1: " + seg1 + "\nsegment 2: " + seg2)

#%%
# Discussion 2: Exercise 2
# Write a program that parses out the bionet file and stores the enzyme names
# and cut sites in a dictionary. Convert the cut site to a regular expression
# and use the enzyme name as the key. Print the dictionary to the screen.

file = open(input("Enter the file with the table formatted data to be "
                  "converted to a dictionary:\n"), "r")

enzymes = {}

for line in file:
    if line.startswith("A"):
        rows = re.finditer(r"([^\s{5,100}]+)\s{5,100}([^\s{5,100}]+)", line)
        for match in rows:
            cutsite = r"("
            for char in match.group(2):
                if char == "^" and char != match.group(2)[0]:
                    cutsite += ")("
                elif char == "N":
                    cutsite += "."
                elif char == "M":
                    cutsite += "[AC]"
                elif char == "K":
                    cutsite += "[GT]"
                elif char == "Y":
                    cutsite += "[CT]"
                elif char == "R":
                    cutsite += "[AG]"
                elif char == "W":
                    cutsite += "[AT]"
                else:
                    cutsite += char
            cutsite += ")"
            enzymes[match.group(1)] = cutsite
            
print(enzymes)
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    