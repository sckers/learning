# -*- coding: utf-8 -*-
"""
joowon.py

@author: Joowon Lee
ver: 0.1

This library contains functions for:
    -creating a new file with a timestamp
    -creating a header for an orf
    -writing an orf and its header to an output file
    
"""
import datetime


def newfile():
    '''
    opens new file to write to with a timestamp in the file name

    Returns
    -------
    file

    '''
    time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output = open(("orf_output_" + time + ".txt"), "a")
    return output

def fasta_output(file, orf, header):
    '''
    writes the orf and header to the output file that has already been made

    Parameters
    ----------
    file : file
        the output file to which the data is to be written
    orf : string
        contains the orf with spaces and separated lines 
        (ie formatted for the final output)
    header : string
        contains the final output header that goes with the orf

    Returns
    -------
    writes to the output file, but doesn't actually return anything

    '''
    file.write(header + "\n" + orf +"\n\n")

def out_header(orf, frame, position, headerdict, acc):
    '''
    creates header for output file for a single orf

    Parameters
    ----------
    orf : string
        contains orf for which to create the header
    frame : integer
        frame in which the orf lies
    position : integer
        starting position of orf in original sequence
    headerdict : disctionary
        contains acc no:input header
    acc : string
        acc no associated with the orf

    Returns
    -------
    the output header as a string

    '''
    if frame > 0:
        fr = '+' + str(frame)
    elif frame < 0:
        fr = str(frame)
    
    header = (headerdict[acc] + " | FRAME = " + fr + " POS = " + 
              str(position) + " LEN = " + str(len(orf) - orf.count(" ")))
    return header
