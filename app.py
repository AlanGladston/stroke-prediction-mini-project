from flask import Flask, render_template, redirect, url_for,request,flash
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)
app.debug = True
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

model = pickle.load(open('model.pickle','rb'))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=['POST','GET'])
@app.route("/predict/", methods=['POST','GET'])
def predict():
    if request.method == 'POST':
        # Retrieve form data
        name = request.form['name']
        age = int(request.form['age'])
        marital_status = request.form['maritalstatus']
        work_type = request.form['Worktype']
        residence = request.form['Residence']
        gender = request.form['gender']
        bmi = float(request.form['bmi'])
        gluc_level = float(request.form['gluclevel'])
        smoke = request.form['Smoke']
        hypertension = request.form['Hypertension']
        heart_disease = request.form['Heartdisease']
        if marital_status == "married":
            marital_status = 1
        else:
            marital_status = 0

        if residence == "urban":
            residence_type_urban = 1
            residence_type_rural = 0
        else:
            residence_type_urban = 0
            residence_type_rural = 1

        if work_type == "govtemp":
            work_type_govt_job = 1
            work_type_private = 0
            work_type_self_employed = 0
            work_type_children = 0
        elif work_type == "privatejob":
            work_type_govt_job = 0
            work_type_private = 1
            work_type_self_employed = 0
            work_type_children = 0
        elif work_type == "selfemp":
            work_type_govt_job = 0
            work_type_private = 0
            work_type_self_employed = 1
            work_type_children = 0
        else:
            work_type_govt_job = 0
            work_type_private = 0
            work_type_self_employed = 0
            work_type_children = 1

        if smoke == "smoker":
            smoking_status_smokes = 1
            smoking_status_formerly_smoked = 0
            smoking_status_never_smoked = 0
            smoking_status_unknown = 0
        elif smoke == "formerly-smoked":
            smoking_status_smokes = 0
            smoking_status_formerly_smoked = 1
            smoking_status_never_smoked = 0
            smoking_status_unknown = 0
        elif smoke == "non-smoker":
            smoking_status_smokes = 0
            smoking_status_formerly_smoked = 0
            smoking_status_never_smoked = 1
            smoking_status_unknown = 0
        else:
            smoking_status_smokes = 0
            smoking_status_formerly_smoked = 0
            smoking_status_never_smoked = 0
            smoking_status_unknown = 1

        if gender == "Female":
            gender_female = 1
            gender_male = 0
        else:
            gender_female = 0
            gender_male = 1

        if heart_disease == "heartdis":
            heart_disease = 1
        else:
            heart_disease = 0

        if hypertension == "hypten":
            hypertension = 1
        else:
            hypertension = 0

        user_details = [age, hypertension, heart_disease, marital_status, gluc_level, bmi, work_type_govt_job,
                        work_type_private, work_type_self_employed, work_type_children, residence_type_rural,
                        residence_type_urban, smoking_status_unknown, smoking_status_formerly_smoked,
                        smoking_status_never_smoked, smoking_status_smokes, gender_female, gender_male]
        feature_value = [np.array(user_details)]
        feature_name = ['age', 'hypertension', 'heart_disease', 'ever_married', 'avg_glucose_level', 'bmi',
                        'work_type_Govt_job', 'work_type_Private', 'work_type_Self-employed', 'work_type_children',
                        'Residence_type_Rural', 'Residence_type_Urban', 'smoking_status_Unknown',
                        'smoking_status_formerly smoked', 'smoking_status_never smoked', 'smoking_status_smokes',
                        'gender_Female', 'gender_Male']
        df = pd.DataFrame(feature_value, columns=feature_name)
        prediction = model.predict(df)[0]
        print(prediction)

        if prediction == 1:
            flash(f'{name} has high risk of stroke', 'warning')
        elif prediction == 0:
            flash(f'{name} has low risk for getting stroke', 'success')
    return render_template("predict.html")

@app.route("/bmi")
def bmi():
    return render_template("bmi.html")

@app.route("/counsel")
def counsel():
    return render_template("counsel.html")

@app.route("/cta")
def cta():
    return render_template("cta.html")

if __name__ == "__main__":
    app.run()
@app.route("/bmi")
def bmi():
    return render_template("bmi.html")

@app.route("/counsel")
def counsel():
    return render_template("counsel.html")

@app.route("/cta")
def cta():
    return render_template("cta.html")

if __name__ == "__main__":
    app.run()