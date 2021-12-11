import os
import pickle
from flask import Flask, request, jsonify, render_template
from xgboost import XGBClassifier
from waitress import serve
import pandas as pd
from sklearn.preprocessing import LabelEncoder



with open("xgbclassifier_tuned.pkl", "rb") as f_in:
    model = pickle.load(f_in)
        
with open("labelencoder_action.pkl", "rb") as f_in:
    action_enc = pickle.load(f_in)
    
    
app = Flask("firewall_prediction")


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('upload.html')
    elif request.method == 'POST':
        csv_file = request.files.get('file')
        X_test = pd.read_csv(csv_file)
        X_test["Result"] = model.predict(X_test)
        X_test["Result"] = pd.Series(action_enc.inverse_transform(X_test["Result"]))
        
        return X_test.to_html()

if __name__ == "__main__":
    app.run(debug=True, host= "localhost", port=6969)