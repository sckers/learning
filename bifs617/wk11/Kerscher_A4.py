# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 20:46:25 2020

@author: scker
"""
# 1. Test whether a sequence has an AT repeat (3 or more occurrences)
# Read a FASTA format file (ie test.txt) and return a message to the user 
# whether or not the repeat exists. Use at least one function

import re
import sys

# make function to find AT repeat
def findATrep(seq):
    '''
    confirms if AT repeats at least 3 times in the dna sequence

    Parameters
    ----------
    seq : string
        contains the dna sequence

    Returns
    -------
    boolean

    '''
    return re.search(r"(AT){3,}", seq)

# function to split sequence from header
def split_fasta(file):
    '''
    separates headers and sequences in a dictionary

    Parameters
    ----------
    file : file
        contains sequence(s)

    Returns
    -------
    Dictionary with accessioin numbers as the keys and sequences as the values

    '''
    seq_dict = {}
    sequence = ""
    
    for line in file:
        # find the header and save for later
        if line.startswith(">"):
            acc = re.search(">([^\s]+)", line).group(1)
            # if we've encountered a header, the sequence string needs to be
            # reset for a new sequence
            sequence = ""
        else:
            # combine each line that is part of the sequence
            sequence += line.rstrip()
        # assign the saved header as the key and the sequence as the value
        seq_dict[acc] = sequence
        
    return seq_dict

# Read in the file
fasta_file = open("test.txt")

# separate acc number(s) and sequence(s)
seqs = split_fasta(fasta_file)

# iterate through dictionary to find sequences with AT repeats
for key, value in seqs.items():
    if findATrep(value):
        print("The repeat exists in sequence " + str(list(
            seqs.keys()).index(key) + 1) + ".")
    else:
        print("The repeat does NOT exist in sequence " + str(list(
            seqs.keys()).index(key) + 1) + ".")
        
fasta_file.close()

#%%
# 2. Parse out an EMBL record including the ID, description (DE), and 
# sequence (SQ); use at least one function

# function for pairing the id with data (DE or SQ)
def split_data(lst, data):
    '''
    pairs ID with other data in file (DE or SQ)

    Parameters
    ----------
    lst : list
        contains list of EMBL entries
    data : string
        either "SQ" or "DE"

    Returns
    -------
    Dictionary with IDs as the keys and sequences or descriptions as the 
    values

    '''
    seq_dict = {}
    value = ""
    
    for entry in lst:
        # blank lines at the end of the document result in empty strings
        # which we don't need/want
        if entry != "":
            # find the ID and save it; starts with ID and ends with a ;
            key = re.search(r"ID\s*([^;]+)", entry).group(1)
            # find the DE or SQ and save it
            if data == "DE":
                # DE starts with DE and ends with XX that indicates the next line
                value = re.search(r"DE\s*([^(XX)]+)", entry).group(1)
            elif data == "SQ":
                # SQ starts with XXSQ and runs to end; SQ could be in the
                # protein cds, so needed XX to differentiate
                SQ = re.search(r"XXSQ\s*(.+)", entry).group(1)
                # we only want what's after the last ; in the SQ line
                numseq = SQ.rsplit(";", 1)[1]
                # we don't want numbers or spaces; these are all possible
                # nucleotide symbols
                value = "".join(re.split(r"[^atgcuryswkmbdhvn\.-]", numseq))
            else:
                # program does not account for anything that isn't SQ or DE
                sys.exit("The data type entered is not valid. Must be 'SQ' or 'DE'."
                      + "\nProgram ended.")
            # add key and value to dictionary
            seq_dict[key] = value
        
    return seq_dict

# function for separating EMBL entries
def embls(file):
    '''
    takes in an open EMBL file and reads the entries into separate strings

    Parameters
    ----------
    file : file
        contains EMBL data and has been opened and read

    Returns
    -------
    List of entries

    '''
    # get rid of the line breaks in the string
    nobreaks = file.replace("\n", "")
    # entries are separated by // so this splits the entries into separate str
    data = nobreaks.split("//")
    return data

# open and read file
emblFile = open("embl.txt", "r").read()

# separate entries into a list
entries = embls(emblFile)

# create dictionaries for the IDs and DEs and IDs and SQs
de_dict = split_data(entries, "DE")
sq_dict = split_data(entries, "SQ")

# print each ID, DE, and SQ in the original file
for ID, DE in de_dict.items():
    print("ID: " + ID + "\nDE: " + de_dict[ID] + "\nSQ: " + sq_dict[ID])
    
emblFile.close()
