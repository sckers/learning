# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 14:48:20 2020

@author: Val
"""



#split codon to multiple of 3
def splitcodon():
    for x in range(0, len(seq),3):
        sequence.append(seq(x:x+3))
        return sequence


#find start codon


def start codon(seq):
    for x in range(len(seq),3):
        codon = seq[x:x+3]
        if codon == "ATG":
            position = x
            
def stop codon():
    for i in range(position,len(dna),3)
        stopcodon = dna[i:i+3]
        if stopcodon in ['TAA','TAG','TGA']:
            position1 = i
            yield (position1-position+3, dna[position:position1+3]
                   break
                         
            