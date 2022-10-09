# Early-Diabetes-Detection-Using-Symptoms
## Problem Statement
Inadequate insulin production or inresponsiveness of body cells to insulin may cause an increase in blood glucose in the body of a person and causing diabetes. Diabetes could cause many other complications, such as loss of vision, kidney infection, and heart problems. Hence, early detection of diabetes can help the patients to keep their sugar levels under control by taking healthy diet with required drugs.

## Objective
To build an efficient model that can help the patients to detect if they have diabetes.

## Dataset Source
This dataset is originally from <a href="https://archive.ics.uci.edu/ml/datasets/Early+stage+diabetes+risk+prediction+dataset.#" target="_blank">UCI Machine Learning Repository</a>. It contains the sign and symptpom data of newly diabetic or would be diabetic patient.

## Techniques Used 
* There is imbalanced class in the dataset, where the majority class belongs to the “0” (we denoted it as negative) label and the minority class belongs to the “1” (we denoted it as positive) label. Hence, SMOTE based techniques (SMOTE, ADASYN, SMOTEENN, SMOTETomek) would be used to overcome imbalanced class issue before model training.
* A function which involves the usage of pipeline was built in order to handle the inbalanced dataset, scale the data, and run the data with a set of classifiers one by one. Besides, the function also includes hyperparameter tuning process with 5-fold cross validation for each classifier so as to select the best model and its best parameters with the help of <a href="https://pypi.org/project/pipelinehelper/">`PipelineHelper`</a>.
* The final model was selected based the testing score returned by the model. 

## Result
The final model is a random forest model which trained which includes the usage of ADASYN technique. The final model returned a recall score of 96.5 % on the test set. 

https://user-images.githubusercontent.com/57357735/194742448-52412c5a-66c2-485b-a25e-9adb154a0013.mp4

## Recommendation
* Implement ensemble learning, such as by using voting classifier or stacking classifier.
* Randomized search could be used to tune the hyperparameters to see if the hyperparameter combination is the same.
* If it is possible, we could increase the size of dataset by collecting more data to train the model. 

## Disclaimer
This application is for learning purpose only. The prediction result may not meet your expectation.
