library(e1071)
library(caret)
library(randomForest)
ctrain <- read.csv("credit_training.csv")
ctest <- read.csv("credit_test.csv")
htest <- read.csv("history_test.csv")
htrain <- read.csv("history_training.csv")

# convert values in history files to binary
htest_binary <- data.frame(ifelse(htest == "critical" | htest == "delayed", 0, 1))
htrain_binary <- data.frame(ifelse(htrain == "critical" | htrain == "delayed", 0, 1))

myuniquenumber <- 343
training <- ctrain[1:myuniquenumber,]
history <- htrain_binary[1:myuniquenumber,]
clsf <- naiveBayes(training, as.factor(history), 0)
predictions <- predict(clsf, ctest)
hbinary <- htest_binary[1:300,]
# make confusion matrix
confusionMatrix(predictions, as.factor(hbinary))

# using random forest model
modelRF <- randomForest(training, as.factor(history))
predictionsRF <- predict(modelRF, ctest)
confusionMatrix(predictionsRF, as.factor(hbinary))