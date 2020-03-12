from imageai.Prediction.Custom import CustomImagePrediction
import os
import os.path

execution_path = os.getcwd()

prediction = CustomImagePrediction()
prediction.setModelTypeAsResNet()
prediction.setModelPath('{path}/traineddata/model_ex-032_acc-0.765625.h5'.format(path=execution_path))
prediction.setJsonPath('{path}/traineddata/model_class.json'.format(path=execution_path))
prediction.loadModel(num_objects=2)  # number of trained objects


def predict(img):
    predictions, probabilities = prediction.predictImage(img, result_count=1)

    for eachPrediction, eachProbability in zip(predictions, probabilities):
        print(str(eachPrediction) + " : " + str(eachProbability))
    return {'status': 'ok'}
