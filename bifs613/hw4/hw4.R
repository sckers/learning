# Question 1 Part A
library(e1071)
credit_training <- read.csv("credit_training.csv")
credit_test <- read.csv("credit_test.csv")
history_test <- read.csv("history_test.csv")
history_training <- read.csv("history_training.csv")
# NOTE that myuniquenumber is an integer between 300 & 600
# you must pick the value and set that variable
myuniquenumber <- 343
training <- credit_training[1:myuniquenumber,]
history <- history_training[1:myuniquenumber,]
clsf <- naiveBayes(training, history, 0)
predictions <- predict(clsf, credit_test)
table(predictions)
# copy and paste the output
table(history_test)
# copy and paste the output

# Question 1 Part B
library(e1071)
library(randomForest)
credit_training <- read.csv("credit_training.csv")
credit_test <- read.csv("credit_test.csv")
history_test <- read.csv("history_test.csv")
history_training <- read.csv("history_training.csv")
# NOTE that myuniquenumber is an integer between 300 & 600
# you must pick the value and set that variable
myuniquenumber <- 343
training <- credit_training[1:myuniquenumber,]
history <- history_training[1:myuniquenumber,]
clsf <- randomForest(training, history)
predictions <- predict(clsf, credit_test)
table(predictions)
# copy and paste the output
table(history_test)
# copy and paste the output

# Question 3
library(HMM)

# Defining HMM
hmm = initHMM(c("C", "N"), c("A", "T", "G", "C"), c(0.5, 0.5), matrix(c(0.55, 0.5, 0.45, 0.5), 2), 
              matrix(c(0.204, 0.195, 0.144, 0.186, 0.354, 0.334, 0.298, 0.285), 2))
hmm

# Generate sample of rolls
observation = c("C", "G", "C", "G", "T", "T", "C", "A", "T", "T", "C", "A", "A", "T", "G")

#Viterbi parsing
viterbi(hmm, observation)