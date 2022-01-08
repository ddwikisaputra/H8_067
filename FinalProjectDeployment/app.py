import flask
import numpy as np
import pickle

model = pickle.load(open('model/model_regressier.pkl', 'rb'))

app = flask.Flask(__name__, template_folder='templates')

@app.route('/')
def main():
    return(flask.render_template('main.html'))

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    casting_features = [float(x) if key == 0 else int(x) for key, x in enumerate(flask.request.form.values())]
    print(casting_features)

    final_features = [np.array(casting_features)]
    prediction = model.predict(final_features)

    fix = "{:.2f}".format(prediction[0])

    return flask.render_template('main.html', 
                                 prediction_text=fix,
                                 prediction_text_title='Prediksi Biaya Asuransi')

if __name__ == '__main__':
    app.run(debug=True)