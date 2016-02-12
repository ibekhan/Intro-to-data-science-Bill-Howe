library('caret')
library('ggplot2')
library('rpart')
library('randomForest')
library('e1071')

data <- read.csv("seaflow_21min.csv",header=TRUE,sep=",")

# answer to question 1
print(summary(data$pop))

# answer to question 2
print(summary(data$fsc_small))

# answer to question 3
split_index <- createDataPartition(data$time,p=0.5,list=FALSE)
train_time <- data$time[split_index]
test_time <- data$time[-split_index]

# answer to question 4
train_pe <- data$pe[split_index]
test_pe <- data$pe[-split_index]
train_chl_small <- data$chl_small[split_index]
test_chl_small <- data$chl_small[-split_index]
totalfacs <- max(as.numeric(factor(data$pop)))
train_df <- data.frame(x=train_pe,y=train_chl_small,fac=as.factor(data$pop[split_index]))
test_df <- data.frame(x=test_pe,y=test_chl_small,fac=as.factor(data$pop[-split_index]))
train_plot <- ggplot(data=train_df,aes(x=x,y=y,color=fac))+geom_point(size=1)
print(train_plot)

# answer to question 5, 6, 7
model_data_train <- data.frame(fsc_small=data$fsc_small[split_index],fsc_perp=data$fsc_perp[split_index],chl_small=data$chl_small[split_index],pe=data$pe[split_index],chl_big=data$chl_big[split_index],chl_small=data$chl_small[split_index],response=data$pop[split_index])
fol <- formula(response ~ fsc_small + fsc_perp + chl_small + pe + chl_big + chl_small)
model <- rpart(fol,data=model_data_train,method="class")
print(model)

# answer to question 8
data_test <- data.frame(fsc_small=data$fsc_small[-split_index],fsc_perp=data$fsc_perp[-split_index],chl_small=data$chl_small[-split_index],pe=data$pe[-split_index],chl_big=data$chl_big[-split_index],chl_small=data$chl_small[-split_index],response=data$pop[-split_index])
pop_predict <- predict(model,newdata=data_test,type="class")
print(sum(pop_predict==data$pop[-split_index])/length(pop_predict))
print(table(as.factor(pop_predict),as.factor(data$pop[-split_index])))

# answer to question 9, 10
model <- randomForest(fol,model_data_train)
pop_predict <- predict(model,newdata=data_test,type="class")
print(model)
print(sum(pop_predict==data$pop[-split_index])/length(pop_predict))
print(importance(model))
print(table(as.factor(pop_predict),as.factor(data$pop[-split_index])))

# answer to question 11
model <- svm(fol,model_data_train)
pop_predict <- predict(model,newdata=data_test,type="class")
print(model)
print(sum(pop_predict==data$pop[-split_index])/length(pop_predict))
print(table(as.factor(pop_predict),as.factor(data$pop[-split_index])))

# answer to question 13
print(plot(data$fsc_big))

# answer to question 14
baddata <- data.frame(x=data$time,y=data$chl_big,fac1=as.factor(data$file_id),fac2=as.factor(data$pop))
print(ggplot(data=baddata,aes(x=x,y=y,color=fac2))+geom_point(size=1))

# answer to question 15
# remove the file_id 208 dataset
data_df <- as.data.frame.list(data)
index_208 <- which(data_df$file_id == 208)
datanew <- data_df[-c(index_208[1]:index_208[length(index_208)]),]
data <- datanew
split_index <- createDataPartition(data$time,p=0.5,list=FALSE)
model_data_train <- data.frame(fsc_small=data$fsc_small[split_index],fsc_perp=data$fsc_perp[split_index],chl_small=data$chl_small[split_index],pe=data$pe[split_index],chl_big=data$chl_big[split_index],chl_small=data$chl_small[split_index],response=data$pop[split_index])
fol <- formula(response ~ fsc_small + fsc_perp + chl_small + pe + chl_big + chl_small)
model <- svm(fol,model_data_train)
data_test <- data.frame(fsc_small=data$fsc_small[-split_index],fsc_perp=data$fsc_perp[-split_index],chl_small=data$chl_small[-split_index],pe=data$pe[-split_index],chl_big=data$chl_big[-split_index],chl_small=data$chl_small[-split_index],response=data$pop[-split_index])
pop_predict <- predict(model,newdata=data_test,type="class")
print(model)
print(sum(pop_predict==data$pop[-split_index])/length(pop_predict))
print(table(as.factor(pop_predict),as.factor(data$pop[-split_index])))

