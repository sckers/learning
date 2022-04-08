# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 19:37:44 2020

@author: scker
"""
# Discussion 2
# Parse the fasta file you downloaded in discussion 1 so and print each
# accession number with it's sequence

import re

fasta_file = open("sequence.fasta", "r")

# create dictionary and string for sequences
seq_dict = {}
sequence = ""

for line in fasta_file:
    if line.startswith(">"):
        acc = re.search("[^>\s]+", line).group()
        sequence = ""
    else:
        sequence += line.rstrip()
    seq_dict[acc] = sequence
    
for key, seq in seq_dict.items():
    print("Accession number: " + key + "\n" + seq + "\n")
    
fasta_file.close()
    
