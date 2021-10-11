from logging import debug
from flask import Flask, jsonify, request
import pickle

app = Flask('customer-churn')



with open("model2.bin", "rb") as f_in:
    model = pickle.load(f_in)

with open("dv.bin", "rb") as f_in:
    dv = pickle.load(f_in)



@app.route('/predict',methods = ['POST'])
def predict():
    customer_data = request.get_json()
    prediction = model.predict_proba(dv.transform(customer_data))[0][1]

    result = {
        'churn_probability': float(prediction)
    }

    return jsonify(result)

@app.route('/ping', methods = ['GET'])
def ping():
    return 'PONG'

if __name__ == '__main__':
    app.run(debug=True, host="localhost", port=9696)
    
    