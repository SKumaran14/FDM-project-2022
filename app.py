import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    float_features = [float(x) for x in request.form.values()]
    final_features = [np.array(float_features)]
    prediction = model.predict(final_features)

    output = prediction[0]

    #return render_template('index.html', prediction_text='Diagnosis {}'.format(output))
    return render_template('index.html', prediction_text='< label > < h2 > < u > Diagnosis < / u > < / h2 > < h3 > M = > Malignant < / br > B = > Benign < / h3 > Diagnosis = {} < / label >'.format(output))


if __name__ == "__main__":
    app.run(debug=True)
