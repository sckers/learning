# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 16:39:53 2020

@author: scker
"""
import re
def getheader(file):
    '''
    compiles headers from a fasta file into a dictionary

    Parameters
    ----------
    file : file
        file that contains the sequences with headers and has not been read

    Returns
    -------
    dictionary with acc no as key and full header as value

    '''
    head_dict = {}
    
    for line in file:
        if line.startswith(">"):
            acc = re.search(">([^\s]+)", line).group(1)
            header = line.rstrip()
            head_dict[acc] = header
            
    return head_dict

file = open("bookishbubs_test1.txt", "w")
file.write(">AF12345 test sequence 1\nCGATATTCCCATGCGGTTTATTTATGCAAAACTGTGACGTTCGCTTGA")
file.close()

file = open("bookishbubs_test1.txt", "r")
headers = getheader(file)
print(headers)
file.close()

#%%
import re
file = open("bookishbubs_test2.txt", "w")
file.write(">AF12345 test sequence 1\nCGATATTCCCATGCGGTTTATTTATGCAAAACTGTGACGTTCGCTTGA")
file.close()

file = open("bookishbubs_test2.txt", "r")

head_dict = {}

for line in file:
    if line.startswith(">"):
        acc = re.search(">([^\s]+)", line).group(1)
        header = line.rstrip()
        head_dict[acc] = header

print(head_dict)
file.close()