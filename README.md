# Early-Diabetes-Detection-Using-Symptoms
## Problem Statement 🤩
Inadequate insulin production or inresponsiveness of body cells to insulin may cause an increase in blood glucose in the body of a person and causing diabetes. Diabetes could cause many other complications, such as loss of vision, kidney infection, and heart problems. Hence, early detection of diabetes can help the patients to keep their sugar levels under control by taking healthy diet and required drugs.

## Objective 🤔
To build an efficient model that can help the patients to detect if they have diabetes.

## Dataset Source 📅
This dataset is originally from <a href="https://archive.ics.uci.edu/ml/datasets/Early+stage+diabetes+risk+prediction+dataset.#" target="_blank">UCI Machine Learning Repository</a>. It contains the sign and symptpom data of newly diabetic or would be diabetic patient.

## Key Exploratory Findings💡 
* Chi-Square ($\chi^2$) tests of independence revealed that 12 out of 15 categorical symptoms have a statistically significant relationship with diabetes ($p < 0.05$). Polyuria ($\chi^2 = 227.87$) and Polydipsia ($\chi^2 = 216.17$) are the strongest individual predictors.  
* Non-diabetic patients predominantly report 0–2 symptoms. In contrast, diabetic patients exhibit a high symptom load, peaking sharply between 7 and 9 symptoms.
* Patients at age extremes ($\le 20$ and $\ge 75$) consistently presented with sudden weight loss without obesity.

## Techniques Used 🕵️‍♀️
* Preprocessing (ColumnTransformer): MinMaxScaler applied to continuous age to prevent scaling distortion in distance-based estimators (KNN/SVM), while binary categorical variables are encoded via OneHotEncoder(drop='if_binary').
* Leak-Free Cross-Validation: Standard 5-fold Stratified CV evaluates Macro Recall, F1-Score, and ROC-AUC. Feature transformations and SMOTE sampling are fit strictly inside training folds using imblearn.pipeline.Pipeline.
* Hyperparameter Tuning: RandomizedSearchCV optimizes hyperparameters across selected candidate models using refit='recall_macro'.

## Result 🔎
1. Baseline Model Comparison (Un-sampled)Random Forest achieved the top baseline performance (96.96% Macro Recall, 99.60% ROC-AUC).Excluded Models: Gaussian Naive Bayes (lowest recall, violated independence assumption), AdaBoost (high fold variance), and Decision Tree (redundant relative to ensemble methods).
2. Post-Tuning Comparison (SMOTE + Hyperparameter Tuning)ModelRecall (Macro) MeanRecall (Macro) StdF1 (Macro) MeanROC-AUC MeanXGBoost97.08%2.48%97.00%99.03%Random Forest96.96%2.45%96.96%99.58%KNN96.75%1.17%96.00%98.71%SVM95.88%1.89%95.92%99.10%Logistic Regression93.71%1.52%93.05%97.38%
3. Final Model Selection RationaleTop Sensitivity Model — XGBoost: Recommended when the primary objective is maximizing sensitivity (97.08% Recall) to minimize false negatives in medical screening.Top Clinical Contender — KNN: Recommended for clinical reliability due to high recall (96.75%) paired with superior fold stability (1.17% Std Dev).

Besides, I also created a flask application with a proper frontend and UI that can be run on the local computer (as shown in the video below). <br><br>

https://user-images.githubusercontent.com/57357735/194742448-52412c5a-66c2-485b-a25e-9adb154a0013.mp4

## Recommendation 📥
* Explore hybrid resampling techniques such as SMOTE-ENN or SMOTE-Tomek to clean noisy class boundaries.
* Implement soft-voting ensemble classifiers combining XGBoost, Random Forest, and KNN.
* Collect a broader demographic sample to evaluate model stability against real-world covariate shifts.

## Disclaimer 😊
This application is for learning purpose only. The prediction result may not meet your expectation. It is always good to consult a doctor if you are not sure if you have diabetes or not.  
