x# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 08:57:54 2020

@author: scker
"""

#BIFS617
#Sarah Kerscher
#Assignment 2

#%% Question 1
#a. Define the given amino acids in an array and print
amacids = ["Phe", "Val", "Asn", "Gln", "His", "Leu", "Cys", "Gly", "Ser"]
print(*amacids, sep = ", ")

#b. Print the number of amino acids
print("There are " + str(len(amacids)) + " amino acids.")

#c. Add His to the end of the array and print
amacids.append("His")
print(*amacids, sep = ", ")

#d. Ask for user input and print
num = int(input("Enter an integer between 1 and " + str(len(amacids)) + ":\n"))
print(amacids[num-1])

#e. Invert sequence based on user input
#Request positions from user
pos1 = int(input("Input two position numbers between which to invert the sequence, up to " + str(len(amacids)) + ":\n"))
pos2 = int(input())

#invert sequence
"""
Question: I tried to write this with one line using splicing but when I printed inv_seq, I got an empty list:
    code:
        inv_seq = amacids[(pos1-1):pos2:-1]
        print(inv_seq)
    output:
        []
Did I write something wrong? Why did I get an empty list back?
"""
inv_seq = amacids[(pos1-1):pos2]
inv_seq.reverse()

#replace inverted sequence in amacids list
print("Before inversion: " + ', '.join(amacids))
amacids[(pos1-1):pos2] = inv_seq
print("After inversion: " + ', '.join(amacids))

#%% Question 2
#add amino acids to list
amacids = ["Trp", "Arg", "Liu", "Ilu", "Asp"]

#ask for user input
pos = int(input("Enter an amino acid position between 1 and " + str(len(amacids)) + ".\n"))

#print result
if pos - 1 not in range(len(amacids)):
    print("Error: that position number is not valid.")
else:
    print(amacids[pos-1])
    
#%% Question 3
#add nucleotides to list
nucs = ["C", "C", "G", "T", "A", "A", "C", "G", "C"]

#a. add T and print
nucs.append("T")
print(*nucs)

#b. Remove first element and print
nucs = nucs[1:len(nucs)]
print(*nucs)

#c. Add T to beginning and print
nucs.insert(0, "T")
print(*nucs)