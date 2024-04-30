from flask import Flask, render_template, redirect, url_for,request
import pickle

app = Flask(__name__)
app.debug = True

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=['POST','GET'])
@app.route("/predict/", methods=['POST','GET'])
def predict():
    if request.method == 'POST':
        # Retrieve form data
        name = request.form['name']
        age = request.form['age']
        marital_status = request.form['maritalstatus']
        work_type = request.form['Worktype']
        residence = request.form['Residence']
        gender = request.form['gender']
        bmi = request.form['bmi']
        gluc_level = request.form['gluclevel']
        smoke = request.form['Smoke']
        hypertension = request.form['Hypertension']
        heart_disease = request.form['Heartdisease']

        print(f"Name: {name}, Age: {age}, Marital Status: {marital_status}, Work Type: {work_type}, Residence: {residence}, Gender: {gender}, BMI: {bmi}, Glucose Level: {gluc_level}, Smoke: {smoke}, Hypertension: {hypertension}, Heart Disease: {heart_disease}")
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