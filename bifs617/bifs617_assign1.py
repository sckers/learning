# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 06:22:56 2020

@author: scker
"""

#%% Question 1
#each line must be a separate print to print on separate lines
print("What is the difference between")

#I have to trade off which marking to use to indicate the string in order to include the different markings (' and ") in the string
print("a ' and a " + '"? Or between a " and a \\"?')

#print nothing to add the empty line
print()

#Use " to indicate string to be able to include ' in the string
print("One is what we see when we're typing our program.")

#Use ' to indicate the string to be able to include " in the string
print('The other is what appears on the "console."')

#%% Question 2
#DNA sequence was copied from a GenBank entry, so all nucleotides are lowercase and there are spaces between every 10 nucleotides
#Open file containing sequence and assign contents to variable
file = open("seq3.txt")
DNAseq = file.read()

#Define variable for appending RNA string
RNAseq = ""

#use for loop to read over each character in the string and change any t's to u's
for char in DNAseq:
    if char == "t":
        char = "u"
    RNAseq += char

#Print DNA and RNA sequences:
print("DNA sequence:  " + DNAseq)
print("RNA sequence:  " + RNAseq)

#close file
file.close()

#%% Question 3
#Using the same sequence as for question 2
#Open file containing sequence and assign contents to variable and open new file to write to
file1 = open("seq3.txt")
DNAseq = file1.read()
file2 = open("DNA_Statistics.txt", "w")

#Define variables for adding AT and GC content
AT = 0
GC = 0

#Use a for loop to read over each character in the string and add up the AT's and GC's
for char in DNAseq:
    if char == "a" or char == "t":
        AT += 1
    if char == "c" or char == "g":
        GC += 1

#determine total number of nucleotides
nucs = AT + GC

#Calculate GC and AT content
GCpercent = (GC/nucs)*100
ATpercent = (AT/nucs)*100

#Write results to file, rounding the percentages to the nearest tenth
file2.write("The GC content of the DNA sequence given is: " + str(round(GCpercent,1)) + "%")
file2.write("\nThe AT content of the DNA sequence given is: " + str(round(ATpercent,1)) + "%")

#Close files
file1.close()
file2.close()