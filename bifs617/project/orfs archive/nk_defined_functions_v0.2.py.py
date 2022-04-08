#!/usr/bin/env python
# coding: utf-8

# In[17]:


############################################################################################
# Final Group Project - Group 4
#     Program:  nk_defined_functions_v0.2.py             
#
# Project Description: 
#                Split sequences from the input files - working processes 
#                Find the codons for splicing the ORFs - working processes 
#                write functions for the forward and reverse strings - completed 
#
# Group 4 Team members:
#                   Sarah Kerscher
#                   Nasaro Kim
#                   Joowon Lee
#                   Valerine Leang
############################################################################################

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

# prior input sequence should be string and stored as a variable (ex) read_sequence = 'AATTACTAATCAGCCCATGATCATAACATAACTGTGTATGTCTTAGAGGACCAAACCCCCCTCCTTCC'
# Writer: Nasaro Kim

# Definition

# function_1: to generate reverse strings
def Reverse(seq):  
    reverse=seq[::-1]
    return reverse #output is stored in a variable called reverse

# function_2: to generate complement strings
def Complement(seq):
    seq_list = list(seq) #convert seq from string to list
    complement_dict = {'A': 'T','T': 'A','C': 'G','G': 'C'}
    seq_list = [complement_dict[base] for base in seq_list]
    return ''.join(seq_list)

# function_3: to generate reverse_complement strings
def Reverse_Complement(seq):
    rev_seq = Reverse(seq) # nest function of Reverse
    reverse_complement = Complement(rev_seq) # nest function of Complement
    return reverse_complement 



# function_4: to ask user input for the minimum number of searching ORFs  - working processes 
def Minimum_Maximum_ORF():
    user_input_number=''
    min_orf = int(user_input_number)
    while True:
        user_input_number= input('Enter the minimum ORF to search for: ')
        min_orf = int(user_input_number)
        if min_orf==int:
            if min_orf<=50:
                print(f'you just enter: {min_orf}')
                break
            elif min_orf>50: 
                print(f'the maximum acceptable number for ORF is 50.')
                break
        else:
            print('wrong entry. Try again.') 
            continue
    return min_orf


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


# In[15]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[2]:





# In[ ]:




