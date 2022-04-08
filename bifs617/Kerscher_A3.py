# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 18:16:47 2020

@author: scker
"""
# Question 1: Write a program that asks the user for a motif and determines if the motif is in the sequence
# a. Write a function that accepts the sequence as an argument. Use regex to find the motif and print the response

import re
import os

def find_motif(proteinSeq, motif):
    if re.search(motif, proteinSeq):
        print("Motif found.")
    else:
        print("Motif not found.")

# b. Assume sequence is in FASTA file. Prompt user for the file, open, read, then put through function
# get file from user and validate that the file exists
while True:
    filepath = input("Enter the path and file name for your protein sequence.\n")
    if os.path.exists(filepath) == True:
        break
    elif filepath == "quit":
        quit()
    else:
        print("Check that you entered the path and filename correctly and try again. Or enter 'quit' to quit.")  
   
# open and read file and get motif from user (convert to uppercase to ensure everything is the same case for comparison)
FASTAfile = open(filepath)
FASTAseq = FASTAfile.read()
motif = (input("Enter a protein motif to search for.\n")).upper()

# remove FASTA header and convert sequence to all uppercase for comparison with motif
fileLines = FASTAseq.split("\n")
proteinSeq = "".join(fileLines[1:]).upper()

# call function
find_motif(proteinSeq, motif)

#%%
# Question 2: Calculate and print each part of the question. Write a function for each part that accepts
# an array as the argument and returns the desired result
# a. Number of measurements (count)
def num_data(array):
    count = len(array)
    return count

# b. Average enzyme activity
def enzymeAct(array):
    avg = sum(array) / len(array)
    return avg

# c. Maximum value in the data set
def max_value(array):
    array.sort()
    return array[-1]

# d. Minimum vlaue in the data set
def min_value(array):
    array.sort()
    return array[0]

# call functions for each data set and print
brain = [65, 69, 70, 63, 70, 68]
heart = [102, 95, 98, 110]
lung = [112, 115, 113, 109, 95, 98, 100]
names = ["brain", "heart", "lung"]
data = [brain, heart, lung]
for i in range(len(data)):
    dataCount = num_data(data[i])
    dataEA = enzymeAct(data[i])
    dataMax = max_value(data[i])
    dataMin = min_value(data[i])
    print("For the " + str(names[i]) +":\nThe number of measurements is " + str(dataCount)
          + ".\nThe average enzyme activity is " + str(dataEA) + ".\nThe maximum value is "
          + str(dataMax) + ".\nThe minimum value is " + str(dataMin) + ".\n")