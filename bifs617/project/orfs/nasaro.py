# -*- coding: utf-8 -*-
"""
nasaro.py

@author: Nasaro Kim
ver: 0.4
This library contains functions for:
    -reversing the string
    -complementing the string
    -getting the reverse complement of a string
    -getting the min ORF length
"""

from __future__ import print_function
from __future__ import generators
from __future__ import division
import time
import math
import subprocess
import os
import re
import string
import sys
import pdb
import itertools

def reverse(seq):
    '''
    generates reverse strings

    Parameters
    ----------
    seq : string
        contains input sequence

    Returns
    -------
    reverse sequence as a string

    '''
    reverse = seq[::-1]
    return reverse

def complement(seq):
    '''
    generates complement string

    Parameters
    ----------
    seq : string
        string containing sequence

    Returns
    -------
    the complementary string of the input sequence

    '''
    seq_list = list(seq)
    complement_dict = {"A" : "T", "T" : "A", "C" : "G", "G" : "C"}
    seq_list = [complement_dict[base] for base in seq_list]
    return "".join(seq_list)

def reverse_complement(seq):
    '''
    calls reverse() and complement() to get the reverse complement of the 
    original sequence

    Parameters
    ----------
    seq : string
        contains original sequence to be converted to reverse complement

    Returns
    -------
    reverse complement sequence as a string

    '''
    rev_seq = reverse(seq)
    reverse_complement = complement(rev_seq)
    return reverse_complement

def orfLen():
    '''
    requests user to determine minimum length of orfs to search for

    Returns
    -------
    min_orf : integer
        length of orfs requested

    '''
    while True:
        try:
            min_orf = int(input('Enter the minimum ORF nucleotide length to search for:\n'))
            break
        except ValueError:
            print('Invalid entry. Try again.') 
    return min_orf

'''
#function_5: to scan start codon  - working processes 
if seq[0]== 'ATG':  


#function_6: to scan stop codon and search for stop codons('TAA', 'TAG', 'TGA') to define ORF  - working processes 
def Defining_ORF_Based_On_Stop_Codons(codons):
    if codon in ['TAA', 'TAG', 'TGA']:
    
# function_5: to generate frame numbers  - working processes 
def Defining_Frame_Based_On_Sequence_length(seq):
    frame_length = len(seq) / 3
    for position in range(len(seq)-3): 
        if position<= frame_length:
            frame = 1
        elif position <= frame_length * 2:
            frame = 2
        else:
            frame = 3
        if complement == 1:
            frame += 3
    return frame
'''
