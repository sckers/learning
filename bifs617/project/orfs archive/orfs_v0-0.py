# -*- coding: utf-8 -*-
"""
UMGC | BIFS 617 | Fall 2020
Group Project
@author: Group 4: Sarah Kerscher, Nasaro Kim, Val Leang, and Joowon Lee
ver: 0.0

This file executes the orfs program with all of the functions put together
that each group member designed.

"""
import sarah
import val
import nasaro
import joowon

#get user input for file and orf length
seqdata = open(sarah.seq_input(), "r")
orfLen = nasaro.orfLen()

#split sequences in the file
seqs = sarah.sep_seq(seqdata, "seq")
headers = sarah.sep_seq(seqdata, "header")

#determine complementary strings
complements = {}
for key, value in seqs.items():
    complementseq = nasaro.reverse_complement(value)
    complements[key] = complementseq

#find ORFs in forward and reverse strands


#separate codons - orfs are going to be in a list which is then a value in a
# dictionary matching the acc no; there will be two orf dicts: forward and rev
orfsFspace = {}
orfsRspace = {}

for key, value in orfsF.items():
    orfLst = []
    for orf in value:
        sepCodons = val.codonsplit(orf)
        orfLst.append(sepCodons)
    orfsFspace[key] = orfLst
    
for key, value in orfsR.items():
    orfLst = []
    for orf in value:
        sepCodons = val.codonsplit(orf)
        orfLst.append(sepCodons)
    orfsRspace[key] = orfLst

#make header
orfheaders = {}
for key, value in orfsFspace.items():
    for orf in value:
        orfheaders[orf] = joowon.out_header(orf, frames[orf], positions[orf], 
                                            headers, key)
for key, value in orfsRspace.items():
    for orf in value:
        orfheaders[orf] = joowon.out_header(orf, frames[orf], positions[orf], 
                                            headers, key)        

#separate codons into 15 per line

#create and write to output file 
outputfile = joowon.newfile()
joowon.fasta_output(outputfile, orfheaders, orfsF)
joowon.fasta_output(outputfile, orfheaders, orfsR)
