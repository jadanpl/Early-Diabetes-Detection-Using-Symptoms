# Early-Diabetes-Detection-Using-Symptoms
## Problem Statement 🤩
Inadequate insulin production or inresponsiveness of body cells to insulin may cause an increase in blood glucose in the body of a person and causing diabetes. Diabetes could cause many other complications, such as loss of vision, kidney infection, and heart problems. Hence, early detection of diabetes can help the patients to keep their sugar levels under control by taking healthy diet and required drugs.

## Objective 🤔
To build an efficient model that can help the patients to detect if they have diabetes.

## Dataset Source 📅
This dataset is originally from <a href="https://archive.ics.uci.edu/ml/datasets/Early+stage+diabetes+risk+prediction+dataset.#" target="_blank">UCI Machine Learning Repository</a>. It contains the sign and symptpom data of newly diabetic or would be diabetic patient.

## Techniques Used 🕵️‍♀️
* There is imbalanced class in the dataset, where the majority class belongs to the “0” (we denoted it as negative) label and the minority class belongs to the “1” (we denoted it as positive) label. Hence, SMOTE based techniques (SMOTE, ADASYN, SMOTEENN, SMOTETomek) would be used to overcome imbalanced class issue before model training.
* A pipeline was built to preprocess data (scaling & one-hot encoding), as well as to handle the inbalanced dataset. 
* To select the best model and its best parameters for each of the SMOTE based techniques, a function was built and it includes hyperparameter tuning process with 10-fold cross validation and the usage of <a href="https://pypi.org/project/pipelinehelper/" target="_blank">`PipelineHelper`</a>.
* The function was run with one SMOTE based technique being selected for each time. The final model was selected based the difference between cross validation score and the testing score returned. 

## Result 🔎
The final model is a support vector machine (SVM) with the SMOTE-ENN technique. The final model returned a recall score of 95.75% for the testing data. This score is slightly higher than the recall score that the SVM returned before the usage of the SMOTE-ENN technique.  Besides, I also created a flask application with a proper frontend and UI that can be run on the local computer (as shown in the video below). <br><br>

https://user-images.githubusercontent.com/57357735/194742448-52412c5a-66c2-485b-a25e-9adb154a0013.mp4

## Recommendation 📥
* Implement ensemble learning, such as by using voting classifier or stacking classifier.
* Randomized search could be used to tune the hyperparameters to see if the hyperparameter combination is the same.
* If it is possible, we could increase the size of dataset by collecting more data to train the model. 

## Disclaimer 😊
This application is for learning purpose only. The prediction result may not meet your expectation. It is always good to consult a doctor if you are not sure if you have diabetes or not.  
