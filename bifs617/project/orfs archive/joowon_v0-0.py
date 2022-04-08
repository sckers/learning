# Joowon Lee
# 10/22/2020
#import modules
import re

# Open input file containing an ORF sequence
file = open('orf.txt')
orf_sequence = file.read()
file.close()

# Input a frame number of the found ORF
orf_frameNum = str(input("Enter frame number: "))

# Open an output file and write the ORF in FASTA format
def fasta_output(orf, orf_output, header, sequence):
    output = open('orf_output.txt', 'w')
    header = ""
    for line in orf_sequence:
        if line.startswith('>'):
            header = line.rstrip('\n')[1:]
        else:
            sequence = line.rstrip('\n')
            orf_startPos(sequence)
            orf_length = len(sequence)
            output.write('>' + header + ' | ' + ' FRAME = ' + orf_frameNum + ' POS = ' + orf_startPos + ' LEN = ' + orf_length + '\n')
            if line.startwith('ATG'):
                output.write(r'(ATG )([ATGC][ATGC][ATGC][' ']){1, 13}[ATGC]{3}' + '\n')
            else:
                output.write(r'([ATGC][ATGC][ATGC][' ']){1, 14}[ATGC]{3}' + '\n')
    print(fasta_output)

fasta_output(orf, orf_output, header, sequence)
