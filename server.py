from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import random
from heart_disease import model
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


def my_prediction_model(i1, i2, i3, i4, i5):
    pred = "yes"
    res = model.predict(i1, i2, i3, i4, i5)
    print (i1, i2, i3, i4, i5)
    # print res
    if res[0] == 0:
        pred="no"
    return {"prediction":pred}


@app.route('/predict_heart', methods=['GET'])
@cross_origin()
def predict_heart():
    i1 = request.args.get('input1')
    i2 = request.args.get('input2')
    i3 = request.args.get('input3')
    i4 = request.args.get('input4')
    i5 = request.args.get('input5')
    result = my_prediction_model(i1, i2, i3, i4, i5)
    return jsonify(result)

@app.route('/predict_kidney', methods=['GET'])
@cross_origin()
def predict_kidney():
    i1 = request.args.get('input1')
    i2 = request.args.get('input2')
    i3 = request.args.get('input3')
    i4 = request.args.get('input4')
    i5 = request.args.get('input5')
    result = my_prediction_model(i1, i2, i3, i4, i5)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
