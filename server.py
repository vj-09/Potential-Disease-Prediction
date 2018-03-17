from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import random
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


def my_prediction_model():
    pred = "yes"
    randnum = random.randint(0,100)
    if randnum > 50:
        pred="no"
    return {"prediction":pred}


@app.route('/predict_heart', methods=['GET'])
@cross_origin()
def predict_heart():
    result = my_prediction_model()
    return jsonify(result)

@app.route('/predict_kidney', methods=['GET'])
@cross_origin()
def predict_kidney():
    s = my_prediction_model()
    return jsonify(s)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)