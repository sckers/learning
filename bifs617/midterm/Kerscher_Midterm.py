# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 20:29:23 2020

@author: scker
"""
#%%
#1) Attached is a file called genomic_dna.txt. It contains a DNA sequence that is comprised of two
#exons and an intron. The first exon runs from the start of the sequence to the 63 bp, and the
#second exon runs from the 91 bp to the end of the sequence. Write a program that will print out
#to files the coding and non-coding regions of the sequence (i.e. The exons in one file called
#coding.txt, and the intron into another file called non_coding.txt). 

#open file and create new files to write to
genomic = open("genomic_dna.txt")
coding = open("coding.txt", "w")
noncoding = open("non_coding.txt", "w")

#separate coding and noncoding regions of sequence
gen_seq = genomic.read()
exon1 = gen_seq[0:63]
exon2 = gen_seq[90:]
nc_seq = gen_seq[63:90]

#write to new files
coding_output = ">exon 1\n" + exon1 + "\n>exon 2\n" + exon2
nc_output = ">noncoding sequence\n" + nc_seq
coding.write(coding_output)
noncoding.write(nc_output)

#close files
genomic.close()
coding.close()
noncoding.close()

#%%
#2) Modify your code for Q1 above so it calculates what percentage of the sequence is coding and
#displays the result to the screen. 

#open file
genomic = open("genomic_dna.txt")

#separate coding and noncoding regions of sequence
gen_seq = genomic.read()
exon1 = gen_seq[0:63]
exon2 = gen_seq[90:]
nc_seq = gen_seq[63:90]

#calculate percentage and print
percent_coding = (len(exon1) + len(exon2))/len(gen_seq) * 100
print("The percentage of the sequence that is coding is " + str(round(percent_coding, 2)) + "%")

#close files
genomic.close()

#%%
#3) Attached is a file called sequences.txt, it contains 3 sequences (one sequence per line). Also
#attached is a file called AccessionNumbers.txt. Write a program that reads in those files and
#produces 3 separate FATSA files. Each accession number in the AccessionNumbers.txt file
#corresponds to a sequence in the sequences.txt file. 

#open and read files
seqs = open("sequences.txt", "r")
accNums = open("AccessionNumbers.txt", "r")

#separate lines into individual elements
seqs_sep = []
for line in seqs:
    seqs_sep.append(line.rstrip()) #this adds elements to a list and the .rstrip eliminates the new line character

accNums_sep = []
for line in accNums:
    accNums_sep.append(line.rstrip())
    
#Change seqs to all upper and remove special characters
seqs_revised = []
for element in seqs_sep:
    sequence = ""
    element = element.upper()
    for char in element:
        if char.isalpha():
            sequence += char
    seqs_revised.append(sequence)

#create file names
filenames = []
for element in accNums_sep:
    file = element + ".txt"
    filenames.append(file)
    
#combine accession numbers and sequences
outputs = []
for element in range(len(accNums_sep)):
    output = ">" + accNums_sep[element] + "\n" + seqs_revised[element]
    outputs.append(output)

#create files
files = []
for file in filenames:
    files.append(open(file, "w"))
    
#write to files
for element in range(len(files)):
    files[element].write(outputs[element])

#close files
seqs.close()
accNums.close()
for file in files:
    file.close()

#%%
#4) Write a program that checks to see if two DNA sequences given as input by the user are reverse
#compliments of one another. 
    
#Request user input
seq1 = input("Enter two sequences:\nSequence 1:  ").upper()
seq2 = input("Sequence 2:  ").upper()

#convert one sequence to reverse complement
seq1_rev = seq1[::-1]
seq1_comp = ""
for char in seq1_rev:
    if char == "A":
        seq1_comp += "T"
    elif char == "T":
        seq1_comp += "A"
    elif char == "C":
        seq1_comp += "G"
    elif char == "G":
        seq1_comp += "C"

#compare sequences
if seq1_comp == seq2:
    print("The two sequences are reverse complements.")
else:
    print("The two sequences are not reverse complements.")
    
#%%
#5) Write a program to read a file, and then print its lines in reverse order, the last line first. You can
#use the sequence.txt file (attached) to test your program with.
    
#Open and read file
file = open("sequences.txt", "r")

#reverse lines
forward = []
for line in file:
    forward.append(line.rstrip())
reverse = forward[::-1]

#print lines
for element in reverse:
    print(element)
    
#%%
#6) Write a program that will predict the size of a population of organisms. The program should ask
#for the starting number of organisms, their average daily population increase (as a percentage),
#and the number of days they will multiply. 
    
#Request input

print("Input the population statistics:")
while True:
    num = float(input("Starting population size:  "))
    if num >= 2:
        break
    else:
        print("Error: Starting population size must be at least 2. Input again.")
        
while True:
    inc = float(input("Average daily population increase as a percentage:  ")) / 100
    if inc >= 0:
        break
    else:
        print("Error: Average daily population increase cannot be negative. Input again.")
        
while True:
    days = int(input("Days to multiply:  "))
    if days >= 1:
        break
    else:
        print("Error: Days to multiply must be at least 1. Input again.")
        
#Calculate population size over each day
print("Day               Organisms\n----------------------------")
for n in range(0, days):
    newNum = num * (1 + inc)**n
    print(str(n + 1) + "                 " + str(newNum))
    
#%%
#7) Write a program that takes user entered lines from the keyboard and stores them in an array.
#When the user enters "quit", the program prints out all the lines sorted (i.e. a line starting with
#an “Ab…” would print out before one starting with “Ac…”). 

#get user input
arr = []
while True:
     line = input("Enter input or 'quit'.\n")
     if line == "quit":
         break
     arr.append(line)

#print sorted list
arr.sort()
print(*arr, sep = '\n')

#%%
#8) Now modify the program so it tells you how many lines have been entered, and then prints out
#only lines 2, 3, and 4.

#get user input
arr = []
while True:
     line = input("Enter input or 'quit'.\n")
     if line == "quit":
         break
     arr.append(line)

#print number of lines
print("There are " + str(len(arr)) + " lines.")

#print elements 2, 3, 4 from sorted list - I assumed you still wanted the list to be sorted
arr.sort()
print(*arr[1:4], sep = '\n')

#%%
#9) Ask the user for a list of sequence lengths, separated by whitespace (Example: 100 123 45
#…etc.). Store the sequence lengths as one string in a variable

user_lst = input("Enter a list of sequence lengths separated by whitespace.\nExample:  100 123 45...\n")

#a) Split that string and create an array from it (each number being an element of the array)
lengths = user_lst.split()

#b) Use a for loop to get the sum of all sequence lengths.
length_sum = 0
for element in lengths:
    length_sum += int(element)

#c) Print the average.
avg = length_sum / len(lengths)
print("The average length is " + str(round(avg, 2)))

#%%
#10) Write a program that asks the user to enter the number of calories and fat grams in a food item.
#The program should display the percentage of the calories that come from fat.

#Request user input
tCal = float(input("Enter the total calories and fat grams in a food item.\nTotal calories:  "))
fatGrams = float(input("Fat grams:  "))

#Calculate calories from fat
fCal = fatGrams * 9
if fCal > tCal:
    print("Error: The number of calories from fat cannot be greater than the total number of calories. Restart program.")

#Calculate perctage of calories from fat
percentCal = fCal / tCal * 100
print("The percentage of calories from fat in your food item is " + str(round(percentCal, 2)))
if percentCal < 30:
    print("This food item is low in fat.")
