# -*- coding: utf-8 -*-
"""
sarah.py

@author: Sarah Kerscher
ver: 0.3

This library contains functions for: 
    -getting the filepath by user input
    -separating the accession numbers and sequences of a FASTA file into
     dictionaries: 
         -one with the acc no as the key and sequence as the value
         -one with the acc no as the key and the entire header line as the 
          value
    -separating the sequences to 15 codons per line if the sequence has spaces
    -determining the frame in which the orf lies in the sequence

"""
import os
import sys
import re

def seq_input():
    '''
    requests user input of filepath
    
    dependencies: sys, os

    Returns
    -------
    filepath as a string

    '''
    while True:
        userinput = input("Enter a valid filepath for your source sequence file:\n")
        if os.path.exists(userinput) == True:
            break
        elif userinput == "quit":
            sys.exit()
        else:
            print("Filepath not valid. Try again or enter 'quit' to exit the "
                  "program.")
    return userinput

def sep_seq(file):
    '''
    separates sequences from accession numbers and saves dictionaries for the 
    sequences and headers
    This post 
    (https://stackoverflow.com/questions/44917009/separate-headers-from-sequences-in-fasta-file-without-using-biopython) 
    was used for reference in separating the lines. I added the regex to make
    the key just the accession number for easier reference.

    Parameters
    ----------
    file : file
        this is the file that contains the sequences and has not been read
    output : string
        either "seq" or "header" depending on the dictionary you want returned

    Returns
    -------
    dictionary with acc no as key and uppercase sequence as value

    '''
    seq_dict = {}
    sequence = ""
    file.seek(0)
    
    for line in file:
        if line.startswith(">"):
            key = re.search(">([^\s]+)", line).group(1)
            sequence = ""
        else:
            sequence += line.rstrip()
        seq_dict[key] = sequence.upper()
        
    return seq_dict
        
def sepLines(seq):
    '''
    separates codons by a space
    This is based on Val's code to space the codons, I just modified it for
    separating the lines

    Parameters
    ----------
    seq : string
        string that contains the orf sequence with spaces

    Returns
    -------
    string with the 15 codons per line

    '''
    sequence = []
    for x in range(0, len(seq),60):
        sequence.append(seq[x:x+60])
    splitORF = "\n".join(sequence)    
    
    return splitORF

def findFrame(pos, direction):
    '''
    determines the frame for the orf

    Parameters
    ----------
    pos : integer
        position of the orf in the original sequence
    direction : string
        direction of the orf, either forward or reverse

    Returns
    -------
    the frame of the orf as an integer

    '''
    remainder = abs(pos)%3
    if remainder == 1:
        absframe = 1
    elif remainder == 2:
        absframe = 2
    elif remainder == 0:
        absframe = 3
        
    if direction == "forward":
        frame = absframe
    elif direction == "reverse":
        frame = -absframe
    
    return frame

def findPos(orf, direction, seq, complement):
    '''
    finds the position of the orf in the original sequence

    Parameters
    ----------
    orf : string
        contains the orf for which we are finding the position
    direction : string
        the direction of the strand in which the orf lies
    seq : string
        the forward strand that the orf comes from
    complement : string
        the reverse strand that the orf comes from

    Returns
    -------
    the position of the orf as an integer

    '''
    
    if direction == "forward":
        pos = re.search(orf, seq).start() + 1
    elif direction == "reverse":
        pos = -(re.search(orf, complement).start() + 1)
        
    return pos

def findORFs(seq, length):
    '''
    finds all orfs in the given sequence
    This post 
    (https://stackoverflow.com/questions/13114246/how-to-find-a-open-reading-frame-in-python) 
    was used for reference on the regular expression. Some modifications had 
    to be made to get it to work in our code

    Parameters
    ----------
    seq : string
        sequence in which you want to find the orfs
    length : integer
        minimum length of orf to find

    Returns
    -------
    list of orfs

    '''
    pattern = re.compile(r"(ATG(?:...)*?(?:TAG|TAA|TGA))")
    orfs = pattern.findall(seq)
    longORFs = []
    for match in orfs:
        if len(match) < length:
            continue
        else:
            longORFs.append(match)
    return longORFs

def getheader(file):
    '''
    compiles headers from a fasta file into a dictionary
    This post 
    (https://stackoverflow.com/questions/44917009/separate-headers-from-sequences-in-fasta-file-without-using-biopython) 
    was used for reference in separating the lines. I added the regex to make
    the key just the accession number for easier reference.


    Parameters
    ----------
    file : file
        file that contains the sequences with headers and has not been read

    Returns
    -------
    dictionary with acc no as key and full header as value

    '''
    file.seek(0)
    head_dict = {}
    
    for line in file:
        if line.startswith(">"):
            acc = re.search(">([^\s]+)", line).group(1)
            header = line.rstrip()
            head_dict[acc] = header
            
    return head_dict


