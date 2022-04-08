# -*- coding: utf-8 -*-
"""
BIFS 617 Final Exam

@author: Sarah Kerscher
Created on Wed Nov  4 05:49:13 2020

"""
import re
# Question 1

# function to find 20 bases upstream from start codon
def bases_beforeATG(dna):
    '''
    finds the 20 bases prior to the start codon in a DNA sequence

    Parameters
    ----------
    dna : string
        sequence from which the user wants the 20 bases

    Returns
    -------
    string fo 20 bases

    '''
    dna.upper()
    pattern = r"[ATGC]{20}(?=ATG)"
    prebases = re.search(pattern, dna).group()
    return prebases

# ask for user input of the dna
user_dna = input("Enter the DNA sequence in which to return the 20 bases "
                 + "preceding the start codon:\n")
print(bases_beforeATG(user_dna))

#%% Question 2

import re

# function to create dictionary
def table_dict(file):
    '''
    creates a dictionary from a file containing two columns

    Parameters
    ----------
    file : file
        contains the columns to be made into a dictionary

    Returns
    -------
    dictionary with the first column as the key and the second as the value

    '''
    # reset file pointer to 0 in case the file has been read before
    file.seek(0)
    # initialize dictionary
    my_dict = {}
    
    # process each line in the file
    for line in file:
        row = re.search(r"(.+)\s+(.+)", line)
        # return the group that occurs before the space(s)
        key = row.group(1)
        # return that group that occurs after the space(s) but before the new line
        my_dict[key] = row.group(2).rstrip()
        
    return my_dict

# open the  file
tabledata = open("Q2_input.txt", "r")

# call the dictionary function
table = table_dict(tabledata)

# print each pair in the dictionary
for key, value in table.items():
    print(key, value)

#%% Question 3
import re

# function for separating entries
def entries(file):
    '''
    takes in an open BLAST result file and reads the entries into separate strings

    Parameters
    ----------
    file : file
        contains BLAST data and has been opened and read

    Returns
    -------
    List of entries

    '''
    # get rid of the line breaks in the string
    nobreaks = file.replace("\n", "")
    # entries are separated by "BLASTX" so this splits the entries into separate str
    data = nobreaks.split("BLASTX")
    for entry in data:
        if entry == "":
            data.remove(entry)
    return data

# function for pulling pertinent data from BLAST entries
def blastdata(result):
    '''
    pulls important data from a blast result entry

    Parameters
    ----------
    result : string
        return data from a blast search

    Returns
    -------
    entry_dict : dictionary
        important information in the form of a dictionary

    '''
    # create dictionary for storing the data
    entry_dict = {}
    # find query and add to dictionary
    query = re.search(r"Query=\s([^\s]+)", result).group(1)
    entry_dict["query"] = query
    # find top entry name and add to dictionary
    top_entry = re.search(r">(.+)(?=\s{2,}Length\s=)", result).group(1)
    entry_dict["top entry"] = top_entry.rstrip()
    # find E-value and add to dictionary
    evalue = re.search(r"Expect\s=\s([^(\sId)]+)", result).group(1)
    entry_dict["e"] = evalue
    # find identities and add to dictionary
    identities = re.search(r"Identities\s=\s([^,]+)", result).group(1)
    entry_dict["identities"] = identities
    return entry_dict   

# open file with results and create a new file for the summary
with open("BlastResults.txt", "r") as results:
    entrydata = results.read()
blastsummary = open("BlastSummary.txt", "a")

# write header for new file
blastsummary.write("Query\tBestHit\tE-value\tIdentities\n")

# split each entry at BLASTX, adding to a list
results_lst = entries(entrydata)

# find the query, top entry, E-value, and identities, then write to file
for entry in results_lst:
    data = blastdata(entry)
    blastsummary.write(data["query"] + "\t" + data["top entry"] + "\t" +
                       data["e"] + "\t" + data["identities"] + "\n")

# close files
results.close()
blastsummary.close()

#%% Question 4
import re

# function to filter out comment lines
def cmtlines(filename):
    '''
    finds the comment lines in a fasta file

    Parameters
    ----------
    filename : file
        contains the data to be retrieved and has been opened, not read

    Returns
    -------
    cmtlst : list
        list of comment lines as strings

    '''
    # reset pointer to start of file
    filename.seek(0)
    # initialize list for comment lines
    cmtlst = []
    for line in filename:
        # find the lines that start with ">"
        if line.startswith(">"):
            # add those lines to the list with the whitespace removed
            cmtlst.append(line.rstrip())
            
    return cmtlst

def parsecmt(comment):
    '''
    parses comment for important information like gene, contig, length, and reads

    Parameters
    ----------
    comment : string
        contains comment information to be parsed

    Returns
    -------
    cmt_dict : dictionary
        contains the important information found as the values

    '''
    cmt_dict = {}
    # find gene and add to dictionary
    gene = re.search(r">([^_]+)", comment).group(1)
    cmt_dict["gene"] = gene
    # find contig name and add to dictionary
    contig = re.search(r"_([^\s]+)", comment).group(1)
    cmt_dict["contig"] = contig
    # find length and add to dictionary
    length = re.search(r"length=([^\s]+)", comment).group(1)
    cmt_dict["length"] = length
    # find numreads and add to dictionary
    numreads = re.search(r"numreads=(.+)", comment).group(1)
    cmt_dict["numreads"] = numreads
    return cmt_dict

# open file and create new file to write data to
contigdata = open("MID2_454AllContigs.fna", "r")
contigtable = open("MID2_SKout.txt", "a")

# call function to filter the comment lines
cmtdata = cmtlines(contigdata)

for comment in cmtdata:
    # call function to parse comment line
    genedata = parsecmt(comment)
    # add data to file
    contigtable.write(genedata["gene"] + "\t" + genedata["contig"] + "\t" + 
                      genedata["length"] + "\t" + genedata["numreads"] + "\n")

# close files
contigdata.close()
contigtable.close()

#%% Question 5
import re

# function for grabbing the sequence from the file
def sep_seq(filename):
    '''
    pulls just the sequence from the file

    Parameters
    ----------
    filename : file
        contains the sequence

    Returns
    -------
    sequence : string
        contains the sequence, uppercase

    '''
    # initialize sequence string
    sequence = ""
    # set pointer to 0 (precaution)
    filename.seek(0)
    
    for line in filename:
        # skip any lines that have the ">" or are empty
        if line.startswith(">") or line == "":
            continue
        # append all of the sequence lines together
        else:
            sequence += line.rstrip().upper()
            
    return sequence

# function for spacing the codons
def spaced_codons(sequence):
    '''
    spaces the codons

    Parameters
    ----------
    sequence : string
        contains the sequence

    Returns
    -------
    spaced_sequence : string
        contains sequences with a space between each codon

    '''
    # initialize string for sequence
    spaced_sequence = ""
    # look at every third character
    for i in range(0, len(sequence), 3):
        # for each character we are looking at, go from that character to three
        # characters later and add a space; add to the sequence string
        spaced_sequence += sequence[i:i+3] + " "
    
    return spaced_sequence

# function for finding the codon frequency
def codon_freq(codon, sequence, tot_codons):
    '''
    determines the frequency of a codon in a sequence

    Parameters
    ----------
    codon : string
        the codon of which to determine the frequency
    sequence : string
        the sequence in which you are searching for the codon
    tot_codons : integer
        total number of codons in the sequence

    Returns
    -------
    freq : float
        frequence of the codon in the sequence

    '''
    # fina all occurrences of the codon in the sequence
    codonmatch = re.findall(codon, sequence)
    # determine the frequency
    freq = 100 * len(codonmatch) / tot_codons
    return freq

# open the file containing the sequence
seqfile = open("genome.txt", "r")

# pull the sequence from the file
seq = sep_seq(seqfile)

# calculate the total number of codons
total = len(seq)//3

# separate codons with a space; will make finding matches easier
sep_codons = spaced_codons(seq)

# make list of codons
codons = []
for base1 in ["A", "T", "G", "C"]:
    for base2 in ["A", "T", "G", "C"]:
        for base3 in ["A", "T", "G", "C"]:
            codon = base1 + base2 + base3
            codons.append(codon)

# initialize codon dictionary
codon_freqs = {}

for codon in codons:
    freq = codon_freq(codon, sep_codons, total)
    codon_freqs[codon] = freq
        
# print the frequencies
print("Codon\tFrequency")
for key, value in codon_freqs.items():
    print(key + "\t\t" + str(round(value,2)))
    
#%% Question 6
import re

def main():
    # open files containing data and create new file for the output
    seqdata = open("SeqLibrary.txt", "r")
    with open("Staden_link.txt", "r") as enzymedata:
        enzymelines = enzymedata.readlines()
    cuts_out = open("Sequence_Cutsites.txt", "a")
    
    # process the sequence file
    seqs_dict = sep_seq(seqdata)
    
    # make enzyme dictionary
    enz_dict = re_dict(enzymelines)
    
    # find cutsites and print to file for each sequence
    for key, value in seqs_dict.items():
        seq_cuts = find_cutsites(value, enz_dict)
        cuts_out.write(key + " Results\n\nEnzyme Name\tCut Positions\n")
        for name, pos in seq_cuts.items():
            pos.sort()
            str_pos = [str(item) for item in pos]
            cuts_out.write(name + "\t\t" + ", ".join(str_pos) + "\n")
        cuts_out.write("\n------------------------------\n\n")
        
    # close files
    seqdata.close()
    cuts_out.close()

# function for getting the sequences
def sep_seq(filename):
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
    filename.seek(0)
    
    for line in filename:
        if line.startswith(">"):
            key = re.search(">([^\s]+)", line).group(1)
            sequence = ""
        elif line.startswith("||"):
            continue
        else:
            sequence += line.rstrip()
        seq_dict[key] = sequence.upper()
        
    return seq_dict

# function for converting the cutsite to regex pattern
def get_regex(cutsite):
    '''
    converts an IUB format cutsite into a regex pattern

    Parameters
    ----------
    cutsite : string
        IUB formatted cutsite

    Returns
    -------
    regex : string
        formatted for a regex search pattern

    '''
    # create dictionary of nucleotide variables
    nucs = {"A" : "A",
            "T" : "T",
            "G" : "G",
            "C" : "C",
            "R" : "[RAG]",
            "Y" : "[YCT]",
            "K" : "[KGT]",
            "M" : "[MAC]",
            "S" : "[SGC]",
            "W" : "[WAT]",
            "B" : "[BCGT]",
            "D" : "[DAGT]",
            "H" : "[HACT]",
            "V" : "[VACG]",
            "N" : "[NATGC]"
            }
    
    # initialize regex string, using parentheses to make finding the cut site easier
    regex = r"("
    for char in cutsite:
        # lets us know when the cutsite is in the middle of what our search pattern
        if char == "'" and char != cutsite[0] and char != cutsite[-1]:
            regex += ")("
        # lets us know when the cutsite is at the end of the string
        elif char == "'" and char == cutsite[-1]:
            regex += ")(."
        # removes cut marking if it's the first character
        elif char == "'" and char == cutsite[0]:
            continue
        # call the dictionary of the nucleotide variables to replace characters
        # as needed
        else:
            regex += nucs.get(char, ".")
        # close the cutsite grouping
    regex += ")"
    
    return regex
    
# function for making restriction enzyme dictionary
def re_dict(filelines):
    '''
    makes restriction enzyme dictionary

    Parameters
    ----------
    filelines : list
        contains each line of the enzyme file as a string in the list

    Returns
    -------
    enzymes : dictionary
        name is the key, cutsite(s) in a list is the value

    '''
    # initialize dictionary
    enzymes = {}
    # iterate over each line from the file that is in the list
    for line in filelines:
        # skip the header
        if re.search(r"^\s", line) or re.search(r"^REBASE", line) or re.search(r"^Rich", line):
            continue
        # remove // at end of cutsite lines
        data = line.rstrip("//\n")
        # split the lines containing cutsites between the name and the site(s)
        columns = data.split("/")
        # the enzyme name is the first element
        name = columns.pop(0)
        # any remaining elements in the list are the cutsites
        # convert cutsites to regex and put in list
        REcutsites = []
        for iubsite in columns:
            cutsite = get_regex(iubsite)
            REcutsites.append(cutsite)
        # add to dictionary
        enzymes[name] = REcutsites
    
    return enzymes

# function that takes sequence and RE dict to get the cut positions
def find_cutsites(sequence, enzyme_dict):
    '''
    finds positions of the cutsites for a sequence

    Parameters
    ----------
    sequence : string
        contains the sequence in which to find the cutsites
    enzyme_dict : dictionary
        contains the enzymes to search for; name is the key, list of cutsites
        is the value

    Returns
    -------
    cuts_dict : dictionary
        key is the name and value is a list of the positions for the cuts

    '''
    cuts_dict = {}
    for key, value in enzyme_dict.items():
        for cutsite in value:
            # initialize list for cutsite positions
            cut_pos = []
            for match in re.finditer(cutsite, sequence):
                if re.search(r"\)\(", cutsite):
                    cut_pos.append(match.start(2))
                else:
                    cut_pos.append(match.start())
            if key in cuts_dict.keys() and len(cut_pos) > 0:
                cuts_dict[key].extend(cut_pos)
            elif len(cut_pos) > 0:
                cuts_dict[key] = cut_pos
                
    return cuts_dict       

main()