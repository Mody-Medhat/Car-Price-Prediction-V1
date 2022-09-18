import numpy as np
import pandas as pd
from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
import joblib

from Preprocess import preprocess_new

reg_model = joblib.load('LinearRegressionModel.pkl')
car = pd.read_csv('CarData.csv')
## add new columns
car["Make-Model"] = car['Make'].astype(str) + " " + car["Model"]
car["fuel_type"] = car['Make'].astype(
    str) + " " + car["Engine Fuel Type"].astype(str)
car["vehicle_style_make"] = car['Make'].astype(
    str) + " " + car["Vehicle Style"].astype(str)


# Intialize the Flask APP
app = Flask(__name__)
cors = CORS(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    makes = sorted(car['Make'].unique())
    models = sorted(car['Make-Model'].unique())
    vehicle_sizes = sorted(car['Vehicle Size'].unique())
    vehicle_styles = sorted(car['vehicle_style_make'].unique())
    fuel_types = sorted(car['fuel_type'].unique())
    Engine_Fuel_Types = sorted(car['Engine Fuel Type'].astype(str).unique())
    car_styles = sorted(car['Vehicle Style'].unique())

    makes.insert(0, 'Select Brand...')
    return render_template('index.html', makes=makes,
                           models=models,
                           vehicle_sizes=vehicle_sizes,
                           vehicle_styles=vehicle_styles,
                           fuel_types=fuel_types,
                           Engine_Fuel_Types=Engine_Fuel_Types,
                           car_styles = car_styles)


@app.route('/predict', methods=['GET', 'POST'])
@cross_origin()
def predict():
    # DropDownList
    make = request.form['make']
    # Input
    model = request.form['model']
    try:
        # input
        year = int(request.form['year'])
       # Input
        engine_hp = float(request.form['engine_hp'])
        # Input
        engine_cylinders = float(request.form['engine_cylinders'])
        # Input
        highway_mpg = float(request.form['highway_mpg'])
        # Input
        city_mpg = float(request.form['city_mpg'])
    except ValueError:
        year = 0
        engine_hp = 0
        engine_cylinders = 0
        highway_mpg = 0
        city_mpg = 0
        # DropDownList
    engine_fuel_type = request.form['engine_fuel_type']
    engine_fuel_type = engine_fuel_type.split(' ', 1)[1]
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
    vehicle_style = vehicle_style.split(' ', 1)[1]

    X_new = pd.DataFrame({'make': [make],
                          'make_model': [model],
                          'year': [year],
                          'engine_fuel_type': [engine_fuel_type],
                          'engine_hp': [engine_hp],
                          'engine_cylinders': [engine_cylinders],
                          'transmission_type': [transmission_type],
                          'driven_wheels': [driven_wheels],
                          'number_of_doors': [number_of_doors],
                          'vehicle_size': [vehicle_size],
                          'vehicle_style': [vehicle_style],
                          'highway_mpg': [highway_mpg],
                          'city_mpg': [city_mpg]})

    # Call the Function and Preprocess the New Instances
    X_processed = preprocess_new(X_new)
    # call the Model and predict
    y_pred_new = reg_model.predict(X_processed)
    price = np.expm1(y_pred_new)
    y_pred_new1 = '{:.2f}'.format(price[0])
    if(price == np.expm1(8.17615829e+09) or price == -1):
        meg = 'Please Cheek The Data'
        return meg
    else:
        meg = 'Car Price : '
        doller = '$'
        return meg + y_pred_new1 + doller


# Run the App from the Terminal
if __name__ == '__main__':
  #  app.run(debug=True,host='192.168.1.111',port=5000)
    app.run(port=6080, debug=True)
