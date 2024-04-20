from flask import Flask,redirect,url_for,render_template

app = Flask(__name__)
app.debug = True
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict")
def predict():
    return render_template("predict.html")

if __name__ == "__main__":
    app.run()