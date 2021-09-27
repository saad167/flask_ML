import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

# Create flask app
flask_app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@flask_app.route("/")
def Home():
    return render_template("index.html")


@flask_app.route("/pre")
def pre():
    return render_template("pre.html")


@flask_app.route("/predict", methods = ["POST"])
def predict():
    l=np.zeros(8)
    l[7]= request.form['nbexp']
    sexe=request.form['sexe']
    if sexe=="F":
        l[0]=1
    if sexe=="H" :
       l[1]=1
    nivetude =request.form['nivetude']
    if nivetude=="BAC":
        l[2]=1
    if nivetude=="BAC+2":
        l[3]=1
    if nivetude=="BAC+3":
        l[4]=1
    if nivetude=="BAC+4":
        l[5]=1
    if nivetude=="BAC+5":
         l[6]=1
    features=l.reshape((1,-1))

    prediction = model.predict(features)
    prediction= prediction[0]
    return render_template("predict.html", prediction_text = "Votre salaire est de : {prediction:.2f} MAD".format(prediction=prediction))

if __name__ == "__main__":
    flask_app.run(debug=True)