# Early-Diabetes-Detection-Using-Symptoms
## Problem Statement
A person is diagnosed to have diabetes if he or she suffers from an extended level of blood glucose in the body which happened because of inadequate insulin production, or because the body cells do not respond to insulin. Diabetes is recognised as a chronic disease as it could cause many other complications, such as loss of vision, kidney infection, and heart problems. Hence, early detection of diabetes can help the patients to keep their sugar levels under control by taking healthy diet with required drugs. 

## Objective
To build an efficient model that can help the patients to detect if they have diabetes.

## Dataset Description
This dataset is originally from <a href="https://archive.ics.uci.edu/ml/datasets/Early+stage+diabetes+risk+prediction+dataset.#">UCI Machine Learning Repository</a>. It contains the sign and symptpom data of newly diabetic or would be diabetic patient.
1. Age 1.20-65
2. Sex 1. Male, 2.Female
3. Polyuria 1.Yes, 2.No.
4. Polydipsia 1.Yes, 2.No.
5. sudden weight loss 1.Yes, 2.No.
6. weakness 1.Yes, 2.No.
7. Polyphagia 1.Yes, 2.No.
8. Genital thrush 1.Yes, 2.No.
9. visual blurring 1.Yes, 2.No.
10. Itching 1.Yes, 2.No.
11. Irritability 1.Yes, 2.No.
12. delayed healing 1.Yes, 2.No.
13. partial paresis 1.Yes, 2.No.
14. muscle stiness 1.Yes, 2.No.
15. Alopecia 1.Yes, 2.No.
16. Obesity 1.Yes, 2.No.
17. Class 1.Positive, 2.Negative.

## Result
The final model is a random forest model which trained with ADASYN technique. It returned a recall score of 96.5 % on the test set. 

## Recommendation
* Implement ensemble learning, such as by using voting classifier or stacking classifier.
* Randomized Search could be used to tune the hyperparameters to see if the hyperparameter combination is the same.
* If it is possible, we could increase the size of dataset by collecting more data to train the model. 
