import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

# Create flask app
flask_app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))


def resultat():
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
    return prediction

@flask_app.route('/', methods=['GET','POST'])
def predict():
    if request.method == 'GET':
        return render_template('index.html')
    else:      
        _text ="Votre salaire est de : {prediction:.2f} MAD".format(prediction=resultat())
        return render_template('index.html', _anchor="index.html#result", prediction_text=_text)
    
if __name__ == "__main__":
    flask_app.run(debug=True)