# BIFS614, Final, question 5
# Sarah Kerscher

# load the libraries
library(factoextra)
library(ggplot2)

# load data and assign to variable wbcd
# read.csv tells the computer to read the file that is in csv format
# this allows the computer to recognize the data as a table
diabetes <- read.csv(url("http://culture-bioinformatics.org/UMGC/diabetes_data.csv"))

diabetes$Gender <- ifelse(diabetes$Gender == "Male", 0, 1)
for(i in 3:16){
  diabetes[ , i] <- ifelse(diabetes[ , i] == "Yes", 1, 0)
}

# perform principal components analysis on dataset
# assign the results to diabetes.pca which are of class prcomp
# in this workflow, variables are zero centered and scaled to have unit variance
diabetes.pca <- prcomp(diabetes[c(1:16)], center = TRUE, scale = TRUE)


# display a summary of the principal components
summary(diabetes.pca)

# plot the data
fviz_pca_ind(diabetes.pca, geom.ind = "point", pointshape = 21, pointsize = 2,
             fill.ind = diabetes$diagnosis, col.ind = "black", palette = "jco",
             addEllipses = TRUE, label = "var", col.var = "black", repel = TRUE,
             legend.title = "Diagnosis") +
  ggtitle("2D PCA-plot from 17 feature dataset") +
  theme(plot.title = element_text(hjust = 0.5))