# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 05:42:09 2020

@author: scker
"""

file1 = open("seq1.txt")
file2 = open("seq2.txt")

seq1 = file1.read()
seq2 = file2.read()

print(seq1)
print(seq2)

file1.close()
file2.close()

#%%
file1 = open("seq1.txt")
file2 = open("seq2.txt")
file3 = open("seq1-2.txt", "w")
file4 = open("seq2-2.txt", "w")

seq1 = file1.read()
seq2 = file2.read()
file3.write(seq1)
file4.write(seq2)

file1.close()
file2.close()
file3.close()
file4.close()

#%%
import os

file1 = os.open("/Sarah/Programming/Python/UMGC/BIFS617/week3/seq1-3.txt", os.O_RDONLY)
file2 = os.open("/Sarah/Programming/Python/UMGC/BIFS617/week3/seq2-3.txt", os.O_RDONLY)
file3 = os.open("/Sarah/Programming/Python/UMGC/BIFS617/week3/Output.txt", os.O_WRONLY|os.O_CREAT)

seq1 = file1.read()
seq2 = file2.read()

output = ">seq1/n" + str(seq1) + "/n||/n>seq2/n" + str(seq2) + "/n||"

print(output)

file3.write(output)

os.close(file1)
os.close(file2)
os.close(file3)