# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 18:48:54 2020

@author: scker
"""
# Week 9 Discussions
# Discussion 1: Searching a Dictionary
# Create a dictionary of accession numbers and sequences and write a program
# in which the user inputs the accession number and gets back the sequence.
# Make sure to include code for when the accession number can't be found.

# Create library (sequences are truncated for simplicity)
seqLib = {
    "D55698" : "caggtccagc tgcagcagtc tggagctgag ctgatgaagc ctggggcctc",
    "KY249690" : "caggttcagc tggtgcagtc tggagctgag gtgaagaagc ctggggcctc",
    "AY835587" : "atgaacccac tgtggaccct cctctttgtg ctgtcagccc ccagaggggt"
    }

# function for calling the sequence
def get_seq(accNo):
    return seqLib[accNo]

while True:
    user_accNo = input("Enter a valid accession number:\n")
    if user_accNo in seqLib:
        print(get_seq(user_accNo))
        break
    elif user_accNo == "quit":
        break
    else:
        print("The accession number you entered cannot be found. Try again "
              "or enter 'quit' to exit the program.")
        
print("End of program")

#%%
# Discussion 2: DNA Translation
# Ask the user for a DNA sequence and return the protein sequence
# Assume there is the appropriate number of nucleotides and the sequence is in
# frame 1

gencode = {
'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}

# get user input
dnaString = input("Enter a DNA sequence to convert it to the protein sequence:\n")
dnaSeq = dnaString.upper()
last_codon_start = len(dnaSeq) - 2

proteinSeq = ""

for start in range(0, last_codon_start, 3):
    trinucleotide = dnaSeq[start:start+3]
    proteinSeq += gencode[trinucleotide]
    
print(proteinSeq)































