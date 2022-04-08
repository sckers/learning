# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 20:20:54 2020

@author: scker
"""
import re

def sep_seq(filename):
    '''
    separates sequences from the accession numbers and saves to a list

    Parameters
    ----------
    filename : file
        this is the file that has already been read and contains the sequences

    Returns
    -------
    list of sequence(s)

    '''
    headers = []
    seqs = []
    for line in filename:
        line = line.strip()
        if line[0] == ">":
            headers.append(line)
        else:
            seqs.append(line.upper())
    return({headers[i] : seqs[i] for i in range(len(headers))})

file = open("seq1.txt", "r")
filename = file.read()
print(sep_seq(filename))

fileLines = FASTAseq.split("\n")
proteinSeq = "".join(fileLines[1:]).upper()