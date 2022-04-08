# derive nucleotide frequencies
library("Biostrings")
library("readr")
DNAseq1 <- readDNAStringSet("seqeuence1_A2.txt")
nuc_freq1 <- oligonucleotideFrequency(DNAseq1, 1)
nuc_freq1
dinuc_freq1 <- dinucleotideFrequency(DNAseq1)
dinuc_freq1

DNAseq2 <- readDNAStringSet("seqeuence2_A2.txt")
nuc_freq2 <- oligonucleotideFrequency(DNAseq2, 1)
nuc_freq2
dinuc_freq2 <- dinucleotideFrequency(DNAseq2)
dinuc_freq2