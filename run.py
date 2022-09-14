# Import the Libraries
from statistics import mode
import numpy as np
import pandas as pd
from flask import Flask, redirect, render_template, request, url_for
import joblib

from Preprocess import preprocess_new


reg_model = joblib.load('LinearRegressionModel.pkl')


# Intialize the Flask APP
app = Flask(__name__)


# print(type(model))

@app.route('/')
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':  # while prediction
        # DropDownList
        make = request.form['make']
        # Input
        model = request.form['model']
        # input
        year = int(request.form['year'])
        # DropDownList
        engine_fuel_type = request.form['engine_fuel_type']
        # Input
        engine_hp = float(request.form['engine_hp'])
        # Input
        engine_cylinders = float(request.form['engine_cylinders'])
        # DropDownList
        transmission_type = request.form['transmission_type']
        # DropDownList
        driven_wheels = request.form['driven_wheels']
        # DropDownList
        number_of_doors = int(request.form['number_of_doors'])
        # DropDownList
        vehicle_size = request.form['vehicle_size']
        # DropDownList
        vehicle_style = request.form['vehicle_style']
        # Input
        highway_mpg = float(request.form['highway_mpg'])
        # Input
        city_mpg = float(request.form['city_mpg'])

        X_new = pd.DataFrame({'make': [make],
                              'model': [model],
                              'year': [year],
                              'engine_fuel_type': [engine_fuel_type],
                              'engine_hp': [engine_hp],
                              'engine_cylinders': [engine_cylinders],
                              'transmission_type': [transmission_type],
                              'driven_wheels': [driven_wheels],
                              'number_of_doors': [number_of_doors],
                              'vehicle_size': [vehicle_size],
                              'vehicle_style': [vehicle_style],
                              'highway_mpg': highway_mpg,
                              'city_mpg': [city_mpg]})

        # Call the Function and Preprocess the New Instances
        X_processed = preprocess_new(X_new)
        # call the Model and predict
        y_pred_new = reg_model.predict(X_processed)
        price = np.expm1(y_pred_new)
        y_pred_new1 = '{:.2f}'.format(price[0])

        if(price == np.expm1(8.17615829e+09) or price == -1):
            return render_template('predict.html', text ='Please Cheek The Model Name!!')
        else:
            return render_template('predict.html', text='Car prediction is : ' , pred_val= y_pred_new1 , sympol = '$')
    else:
        return render_template('predict.html')


# Run the App from the Terminal
if __name__ == '__main__':
  #  app.run(debug=True,host='192.168.1.111',port=5000)
    app.run( port = 6060 , debug=True)
