# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 05:48:22 2020

@author: scker
"""
# Week 8 Exercises
# Discussion Exercise 1
# Use a regular expression to extract and print the accession number of a sequence in a FASTA file.
import re
file = open("seq1.txt")
acc = re.search(r">(.{1,10}) ", file.read())
print("The accession number is " + acc.group(1))
file.close()

#%%
# Discussion Exercise 2
# indicate ending position for each desired string in the paragraph
items = ["(RNAi)", "(dsRNA)", "(ssRNAs)", "mRNAs"]
para = ("Several rapidly developing RNA interference (RNAi) methodologies hold "
        "the promise to selectively inhibit gene expression in mammals. RNAi is "
        "an innate cellular process activated when a double-stranded RNA (dsRNA) "
        "molecule of greater than 19 duplex nucleotides enters the cell, causing "
        "the degradation of not only the invading dsRNA molecule, but also single"
        "-stranded (ssRNAs) RNAs of identical sequences, including endogenous "
        "mRNAs.")

for element in items:
    found = re.search(element, para)
    print(element + " ends at position " + str(found.end()))
