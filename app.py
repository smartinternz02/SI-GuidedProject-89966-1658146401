from distutils.log import debug
import numpy as np
import pandas as pd 
from flask import Flask,request,jsonify,render_template
import pickle


app = Flask(__name__)
model = pickle.load(open('weather_prediction.pickle','rb'))
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/predict',methods=['POST'])
def y_predict():
    if request.method == "POST":
        ds = request.form["Date"]
        a = {"ds":[ds]}
        ds = pd.DataFrame(a)
        prediction = model.predict(ds)
        output = round(prediction.iloc[0,18],2)
        print(output)
        return render_template('home.html',prediction_text = "Temperature on selected date is. {} degree celsius".format(output))
    return render_template("home.html")


if __name__ == "__main__":
    app.run(port=5000,debug=False)
