import pickle
import pandas as pd
from flask import Flask, render_template, request

model = pickle.load(open('finalized_svm_model_diabetes.pkl', 'rb'))
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/result", methods=["POST"])
def submit():
    # HTML to .py
    global age, gender, polyuria, polydipsia, sudden_weight_loss
    global weakness, polyphagia, genital_thrush
    global visual_blurring, itching, irritability
    global delayed_healing, partial_paresis
    global muscle_stiffness, alopecia

    if request.method == "POST":
        age = int(request.form["num__age"])  # variable 1
        gender = request.form["cat__gender_Male"]  # variable 2
        polyuria = request.form["cat__polyuria_Yes"] # variable 3
        polydipsia = request.form["cat__polydipsia_Yes"] # variable 4
        sudden_weight_loss = request.form["cat__sudden_weight_loss_Yes"] # variable 5
        weakness = request.form["cat__weakness_Yes"]  # variable 6
        polyphagia = request.form["cat__polyphagia_Yes"]  # variable 7
        genital_thrush = request.form["cat__genital_thrush_Yes"]  # variable 8
        visual_blurring = request.form["cat__visual_blurring_Yes"]  # variable 9
        itching = request.form["cat__itching_Yes"]  # variable 10
        irritability = request.form["cat__irritability_Yes"]  # variable 11
        delayed_healing = request.form["cat__delayed_healing_Yes"]  # variable 12
        partial_paresis = request.form["cat__partial_paresis_Yes"]  # variable 13
        muscle_stiffness = request.form["cat__muscle_stiffness_Yes"]  # variable 14
        alopecia = request.form["cat__alopecia_Yes"]  # variable 15

    # .py to HTML
    # Get prediction results
    user_input = pd.DataFrame({'age':[age], 'gender':[gender], 'polyuria':[polyuria], 'polydipsia':[polydipsia],
                               'sudden_weight_loss':[sudden_weight_loss], 'weakness': [weakness], 'polyphagia': [polyphagia],
                               'genital_thrush': [genital_thrush], 'visual_blurring': [visual_blurring], 'itching': [itching],
                               'irritability': [irritability], 'delayed_healing': [delayed_healing], 'partial_paresis': [partial_paresis],
                               'muscle_stiffness': [muscle_stiffness],'alopecia': [alopecia]})
    prediction = model.predict(user_input)
    if prediction == 1:
        return render_template('result.html', prediction="have diabetes. Please consult to a doctor.")
    elif prediction == 0:
        return render_template('result.html', prediction="have no diabetes.")

if __name__ == "__main__":
    app.run(debug=True)
