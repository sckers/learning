# BIFS614, Final,Question 6
# Sarah Kerscher

# load the libraries
library(caret)

# pull the data from a url and save to variable wbcd
diabetes <- read.csv(url("http://culture-bioinformatics.org/UMGC/diabetes_data.csv"))

# create a set of test/training partitions using 80% of the data
index <- createDataPartition(diabetes$diagnosis, p = 0.80, list = FALSE)

# created the training and validation data sets from the index
training <- diabetes[index,]
validation <- diabetes[-index,]

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
# define the method to use and use the metric and trControl flags as previously defined
fit.lda <- train(diagnosis~., data = diabetes, method = "lda", metric = metric, trControl = control)

fit.lda
