import flask
from flask import Flask, request, jsonify
from imageai.Prediction.Custom import CustomImagePrediction
import os
import os.path
from keras import backend as K
import json

# ------------------------------------------------
# gunicorn --workers=1 main:app (tensorflow backend)
# -------------------------------------------------
app = flask.Flask(__name__)
execution_path = os.getcwd()

K.clear_session()
prediction = CustomImagePrediction()
prediction.setModelTypeAsResNet()
prediction.setModelPath('{path}/traineddata/model_ex-032_acc-0.765625.h5'.format(path=execution_path))
prediction.setJsonPath('{path}/traineddata/model_class.json'.format(path=execution_path))
prediction.loadModel(num_objects=2)  # number of trained objects


def predict(img):
    import base64
    imgdata = base64.b64decode(img)
    filename = 'some_image.jpg'  # I assume you have a way of picking unique filenames
    with open(filename, 'wb') as f:
        f.write(imgdata)
    predictions, probabilities = prediction.predictImage(image_input=filename, result_count=1)

    for eachPrediction, eachProbability in zip(predictions, probabilities):
        return {'Result': str(eachPrediction), 'Accuracy': str(eachProbability)}


@app.route('/', methods=['POST'])
def index():
    data = request.get_json(force=True)
    result = predict(data['img'])
    if not data:
        return jsonify({'Message': 'Invalid Params'})
    response = app.response_class(
        response=json.dumps(result),
        status=200,
        mimetype='application/json'
    )
    return response
