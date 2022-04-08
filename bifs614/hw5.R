# BIFS614, Homework 5
# Sarah Kerscher
# 22Mar2021

# load the libraries
library(factoextra)
library(ggplot2)

# load data and assign to variable wbcd
# read.csv tells the computer to read the file that is in csv format
# this allows the computer to recognize the data as a table
wbcd <- read.csv(url("http://culture-bioinformatics.org/UMGC/wbcd.csv"))

# add columns 2-32 to a new variable wbcd.data
# effectively removes the first column of descriptive data
wbcd.data <- wbcd[, c(2:32)]

# use the column labeled id from the original data wbcd
# make that column the row names for the new data set wbcd.data
row.names(wbcd.data) <- wbcd$id

# perform principal components analysis on dataset wbcd.data
# assign the results to wbcd.pca which are of class prcomp
# in this workflow, variables are zero centered and scaled to have unit variance
wbcd.pca <- prcomp(wbcd.data[c(2:31)], center = TRUE, scale = TRUE)


# display a summary of the principal components
summary(wbcd.pca)

# plot the data
fviz_pca_ind(wbcd.pca, geom.ind = "point", pointshape = 21, pointsize = 2,
             fill.ind = wbcd$diagnosis, col.ind = "black", palette = "jco",
             addEllipses = TRUE, label = "var", col.var = "black", repel = TRUE,
             legend.title = "Diagnosis") +
  ggtitle("2D PCA-plot from 30 feature dataset") +
  theme(plot.title = element_text(hjust = 0.5))