# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 05:48:40 2020

@author: Nasaro Kim

Functions for processing the sequences into ORFs
"""
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