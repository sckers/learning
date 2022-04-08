# BIFS 617, Homework 5
# Sarah Kerscher
# Problem 1: Derive the weights for the provided sequences
# a. compute the pairwise distances between the sequences
library(ape)
library(phangorn)
seq <- as.DNAbin(strsplit(matrix(c("acta", "actt", "cgtt", "agat")), ""))
dist_dna <- dist.dna(seq, model = "raw")

# b. apply UPGMA method to join sequences and the clusters
join_seq <- upgma(dist_dna)

# c. build phylogenetic tree
tree_plot <- plot(join_seq, main = "UPGMA")

# Problem 6: Create an MSA and phylogenetic tree using ape and clustalw
# Read accession numbers from the sequences downloaded for hw2
GenBankSeqs <- (c("NM_000518.5", "NM_205489.2", "NM_173917.2", "NM_001144841.1",
                "NM_001164428.1", "NM_001164018.1", "NM_001201019.1", 
                "NM_001097648.1", "NM_001283367.1", "NM_001168847.1"))
seqs <- read.GenBank(GenBankSeqs)

# write to a fasta file
write.FASTA(seqs, file = "new.fasta")

# Run clustalw
system(paste('"C:\\Program Files (x86)\\ClustalW2\\clustalw2.exe" new.fasta'))

# read alignment file
seqAln <- read.dna("new.aln", format = "clustal")

# Create tree using neighbor-joining method
nj_dist <- dist.dna(seqAln)
tree <- nj(nj_dist)

# Plot the tree
plot(tree, main = "Phylogenetic Tree", sub = "Using the Neighbor-Joining Method")