import pandas as pd
from imblearn.over_sampling import SMOTE
from sklearn.neighbors import KNeighborsClassifier
from imblearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
import pickle

diabetes = pd.read_csv("https://raw.githubusercontent.com/jadanpl/Early-Diabetes-Detection-Using-Symptoms/main/diabetes_data.csv")
diabetes.columns = diabetes.columns.str.lower().str.replace(" ","_")

# split data into output and input
X = diabetes.drop(['class'], axis=1) # inputs
Y = diabetes['class'].map({'Negative':0,'Positive':1}) # outputs
cat_cols = list(X.drop(['age'], axis=1))

# Building Random Forest Classifier
final_model = Pipeline(steps=[('preprocessing', ColumnTransformer(transformers=[('cat', OneHotEncoder(sparse_output=False, dtype='int', drop="if_binary"), cat_cols),
                                                                              ('num', MinMaxScaler(), ['age'])])),
                            ('smote', SMOTE(random_state=42)),
                            ('classifier', KNeighborsClassifier(metric='manhattan', n_neighbors=3, weights='distance'))])

# Fit the model on dataset
final_model.fit(X, Y)

# save the model
filename = 'finalized_knn_diabetes.pkl'
pickle.dump(final_model, open(filename, 'wb'))
# import joblib
# joblib.dump(final_model, 'finalized_knn_diabetes.joblib')
