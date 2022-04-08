# -*- coding: utf-8 -*-
"""
UMGC | BIFS 617 | Fall 2020
Group Project
@author: Group 4: Sarah Kerscher, Nasaro Kim, Val Leang, and Joowon Lee
ver: 0.2

This file executes the orfs program with all of the functions put together
that each group member designed.

"""
import sarah
import val
import nasaro
import joowon

# get user input for file and orf length
seqdata = open("projectfasta.txt", "r")
orfLen = nasaro.orfLen()

# create output file
outputfile = joowon.newfile()

# split sequences in the file
seqs = sarah.sep_seq(seqdata)
headers = sarah.getheader(seqdata)

# process each sequence
for acc, seq in seqs.items():
    # find complementary strand
    complementseq = nasaro.reverse_complement(seq)
    
    # find orfs in both strands and put them in a dictionary (orfdict) key is
    # either forward or reverse, value is a list of orfs
    orfdict = {}
    orfdict["forward"] = sarah.findORFs(seq, orfLen)
    orfdict["reverse"] = sarah.findORFs(complementseq, orfLen)
    
    # process each orf
    for direction, orflst in orfdict.items():
        for orf in orflst:
            # add spaces between codons
            sepCodons = val.codonsplit(orf)
            
            # find position
            pos = sarah.findPos(orf, direction, seq, complementseq)
            
            # find frame
            frame = sarah.findFrame(pos, direction)
            
            # split orf into 15 codons per line
            orflines = sarah.sepLines(sepCodons)
            
            # create header
            outheader = joowon.out_header(sepCodons, frame, pos, headers, acc)
            
            # append to the file
            joowon.fasta_output(outputfile, orflines, outheader)
            
outputfile.close()
seqdata.close()
