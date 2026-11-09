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
1. Based on the baseline model comparison, Random Forest achieved the top baseline performance (96.96% Macro Recall, 99.60% ROC-AUC). Models such as Gaussian Naive Bayes (lowest recall, violated independence assumption), AdaBoost (high fold variance), and Decision Tree (redundant relative to ensemble methods) had been excluded from further evaluation process.
2. After Tuning Comparison (SMOTE + Hyperparameter Tuning), KNN is selected as final model due to  high recall (96.75%) paired with superior fold stability (1.17% Std Dev), which is recommended for clinical reliability.

## Model Deployment 🚀
Besides, I also created a flask application (along HTML and CSS too) with a proper frontend and UI that can be run on the local computer. This is because not every user is a coder, so it is unrealistic to expect the end-users to know how to run the Jupyter Notebook and get output. 
First, we need to use Pickle to serialize the trained model and save the serialized format to a file. After you run the codes, you could find a pickle file called ‘finalized_knn_diabetes.pkl’ in your directory. We would use it in the main.py (the application file to make a prediction based on user inputs and sends the result back to the user).
Then, we need to create a folder called ‘templates’ to store the home.html file (basically a form that enables the users to provide their inputs) and the result.html file (a file that shows the result to the users).

Another folder called ‘static’ is to store CSS files to improve the appearance of the webpage or to store any images. You can link the CSS file to the HTML file by using <link>. It is optional whether you want to create a CSS file, as you always can apply internal CSS in the HTML by including the styling features using the <style> tag in the <head> part of the HTML file (⚠️PS: Internal CSS might increase the page size and loading time).

Other than Flask library, we also need to import the following libraries:
* render_template : to render the HTML templates.
* request: to send HTTP requests using Python.
At first, we need to create the route to the home page by using @app.route(“/”). After that, we need to build a custom-built predicting function and @app.route(“/result”, methods=[“POST”]) to predict whether the user has diabetes from the inputs from the user and render the output to the result.html. It is important to note that the methods=[“POST”] in the form element of home.html too.

After you have completed the coding part, you can run the main.py on your local PC and view the app using the browsers by clicking the link that appears. You will see the home.html page after clicking the link.
(The demo is shown in the video below). <br><br>

https://user-images.githubusercontent.com/57357735/194742448-52412c5a-66c2-485b-a25e-9adb154a0013.mp4

## Recommendation 📥
* Explore hybrid resampling techniques such as SMOTE-ENN or SMOTE-Tomek to clean noisy class boundaries.
* Implement soft-voting ensemble classifiers combining XGBoost, Random Forest, and KNN.
* Collect a broader demographic sample to evaluate model stability against real-world covariate shifts.

## Disclaimer 😊
This application is for learning purpose only. The prediction result may not meet your expectation. It is always good to consult a doctor if you are not sure if you have diabetes or not.  
