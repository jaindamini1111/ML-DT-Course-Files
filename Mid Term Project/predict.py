import os
import pickle
from flask import Flask, request, jsonify, render_template
from sklearn.ensemble import RandomForestClassifier
from waitress import serve
import pandas as pd
from sklearn.preprocessing import LabelEncoder



with open("randomforest_tuned.pkl", "rb") as f_in:
    model = pickle.load(f_in)
    
with open("labelencoder_country.pkl", "rb") as f_in:
    country_enc = pickle.load(f_in)
    
with open("labelencoder_ethnicity.pkl", "rb") as f_in:
    ethinicity_enc = pickle.load(f_in)
    
with open("labelencoder_gender.pkl", "rb") as f_in:
    gender_enc = pickle.load(f_in)
    
    
app = Flask("autism_prediction")


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('upload.html')
    elif request.method == 'POST':
        csv_file = request.files.get('file')
        X_test = pd.read_csv(csv_file)
        X_test["gender"] = pd.Series(gender_enc.transform(X_test["gender"]))
        X_test["ethnicity"] = pd.Series(ethinicity_enc.transform(X_test["ethnicity"]))
        X_test["jaundice"] = X_test["jaundice"].map({"no": 0, "yes": 1})
        X_test["country"] = pd.Series(country_enc.transform(X_test["country"]))
        
        X_test["autism"] = model.predict(X_test)
        X_test["autism"] = X_test["autism"].map({0: "no", 1: "yes"})
        
        return X_test.to_html()

if __name__ == "__main__":
    app.run(debug=True, host= "localhost", port=6969)