# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 21:24:33 2020

@author: scker
"""

def get_seqfile(filename):
    '''
    function for opening and reading a file based on the input
    of a filepath.
    
    Depends on os library.
    
    Parameters
    ----------
    filename : string
        file path and name to be opened

    Returns
    -------
    data in the file

    '''
    with open(filename, "r") as seqfile:
        data = seqfile.read()
    return data

print(get_seqfile("seq1.txt"))