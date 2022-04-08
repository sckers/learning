# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 04:20:32 2020

@author: scker
"""
# Discussion 2: Parsing Blast Output
# Write a program that calls an online blast function using a fasta sequence
# you've downloaded, then use BioPython to parse the results to the screen

import Bio

# parse file
sequence = repr(Bio.SeqIO.parse("sequence.fasta", "fasta").seq)

