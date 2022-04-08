# BIFS614, Homework 6
# Sarah Kerscher
# 29Mar2021

# load the libraries
library(caret)

# pull the data from a url and save to variable wbcd
wbcd <- read.csv(url("http://culture-bioinformatics.org/UMGC/wbcd.csv"))

# set the id column as the row names for the data
row.names(wbcd) <- wbcd$id

# adjust the data so we only look at columns 2-32
# effectively removes the first column of descriptive data
wbcd <- wbcd[,c(2:32)]

# create a set of test/training partitions using 80% of the data
index <- createDataPartition(wbcd$diagnosis, p = 0.80, list = FALSE)

# created the training and validation data sets from the index
training <- wbcd[index,]
validation <- wbcd[-index,]

# observe the distribution of diagnosis data
# table() creates a count of the different factors encountered in the diagnosis data
# prop.table() returns an array of summary statistics based on those counts
percentage <- prop.table(table(training$diagnosis)) * 100

# combine the diagnoses frequencies and percentages into a table together
cbind(freq = table(training$diagnosis), percentage = percentage)

# rovide summary statistics of the training data
summary(training)

# set up the trControl and metric flags that will be used in later algorithms
# For control, the resampling method will be cv (cross-validation), with 10 reiterations
control <- trainControl(method = "cv", number = 10)

# metric is used to determine the best model; in this case we are working with classification, so we use Accuracy
metric <- "Accuracy"

# train the four models
# ensure reproducible results
set.seed(7)

# in each model we want the model to demonstrate the diagnosis as a function of all other variables (the first argument)
# the data the we are pulling from is wbcd
# define the method to use and use the metric and trControl flags as previously defined
fit.lda <- train(diagnosis~., data = wbcd, method = "lda", metric = metric, trControl = control)
fit.knn <- train(diagnosis~., data = wbcd, method = "knn", metric = metric, trControl = control)
fit.svm <- train(diagnosis~., data = wbcd, method = "svmRadial", metric = metric, trControl = control)
fit.rf <- train(diagnosis~., data = wbcd, method = "rf", metric = metric, trControl = control)

# summarize the results from all of the models
results <- resamples(list(lda = fit.lda, knn = fit.knn, svm = fit.svm, rf = fit.rf))
summary(results)

# best model based on previous results is svm
# make predictions using svm model and the validation set of data
predictions <- predict(fit.svm, validation) 

# generate Confusion Matrix to evaluate the predictions
# the diagnosis field has to be entered in the command as factors
confusionMatrix(predictions, as.factor(validation$diagnosis))

# grab some new patient data to feed into the model
patient.data <- read.csv(url("http://culture-bioinformatics.org/UMGC/wbcd_new_patients.csv"))
predict(fit.svm, patient.data)