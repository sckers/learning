# -*- coding: utf-8 -*-
"""
val.py

@author: Valerine Leang
ver: 0.2

This library contains functions for:
    -separating the codons in an orf with a space
    
"""

def codonsplit(seq):
    '''
    separates codons by a space

    Parameters
    ----------
    seq : string
        string that contains the orf sequence

    Returns
    -------
    string with the codons separated by a space

    '''
    sequence = []
    for x in range(0, len(seq),3):
        sequence.append(seq[x:x+3])
    splitORF = " ".join(sequence)    
    
    return splitORF
'''
def start_codon(seq):
    for x in range(len(seq),3):
        codon = seq[x:x+3]
        if codon == "ATG":
            position = x
            
def stop_codon():
    for i in range(position,len(dna),3)
        stopcodon = dna[i:i+3]
        if stopcodon in ['TAA','TAG','TGA']:
            position1 = i
            yield (position1-position+3, dna[position:position1+3]
                   break
'''            