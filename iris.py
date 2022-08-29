from tkinter import N
from flask import Flask,render_template,request,jsonify
import pickle
import numpy as np

with open('model.pkl','rb') as f:
    model = pickle.load(f)

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('iris_data.html')

@app.route('/iris',methods=['POST'])
def predict():
    SepalLengthCm = float(request.form['SepalLengthCm'])
    SepalWidthCm = float(request.form['SepalWidthCm'])
    PetalLengthCm = float(request.form['PetalLengthCm'])
    PetalWidthCm = float(request.form['PetalWidthCm'])

    
    data = np.array([SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm],ndmin=2)
    
    result = model.predict(data)

    print(result)

    if result == 0:
        pred = 'Iris Setosa'
    if result == 1:
        pred = 'Iris Versicolour'
    if result == 2:
        pred = 'Iris Virginica'

    return jsonify(pred)




# 5.1	3.5	1.4	0.2	

# 6.7	3.0	5.2	2.3










if __name__ == "__main__":
    app.run(debug=True)
