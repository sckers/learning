# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 14:48:20 2020

@author: Val
"""
gencode = {
'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}

seq = "AAGTTGTTTAAAACGACTACTAAATCCGCGTGATAGGGGATTTCATATTT"
#split codon to multiple of 3
for x in range(0, len(seq),3):
    sequence.append(seq(x:x+3))
return sequence


#find start codon position for output header

def start_to_endORF(seq,frame):
    seq = seq.upper()
    for x in range(frame, len(seq),3):
        codon = seq[x:x+3]
        if codon == "ATG":
            position = x
            for i in range(position,len(seq),3):
                codon1 = seq(i:i+3)
                if codon1 in ['TAG','TAA','TGA']:
                    position1 = i
                    yield(position1-position+3, seq[position:position1+3])
                    break

