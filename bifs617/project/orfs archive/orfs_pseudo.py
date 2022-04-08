# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 19:59:05 2020

@author: scker
"""

input(user file path and name)
input user's desired orf length
open user file

separate the sequences from the accession numbers (or any leading text in first line)
strip line breaks from sequences
convert sequences to uppercase
append sequences to dictionary with the first lines as the keys

find complements for each sequence and add to list

for sequence in list of sequences:
    for each frame in sequence:
        find ATG
        append every three bases until we find stop codon
        save orf to list
        
for each orf in list:
    add space at every three nucleotides

#create FASTA header
header = header from input + | + FRAME = frame + POS = start of orf + LEN = length of orf

count 15 codons then insert line break

write header and final sequence to new file
