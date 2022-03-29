import pandas as pd
import numpy as np
import sklearn
import flask
import flask_cors
import joblib
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
from data_ingestion.data_loader import load_data
from model_building.reducing_features import  clusters
# from PredictionsToDB.PredictionsToDB import createTable , enterTable

#
# d1 = load_data()
# op =  d1.get_data()

# op.drop('DATE')

# c1 = clusters(min_samples=[10,20,30 ,50,70,100,150,200,300,350,400] , eps=[0.5 , 1,4,10,20,30,40,50,60,70,80,90,100])
# c1 = clusters(400 , 100)
# final  = c1.makeclusters(op.drop(columns = ['DATE']))
app = flask.Flask(__name__)


# createTable()

@app.route('/' , methods =  ['GET' , "POST"])
@cross_origin()
def home_page():
    return render_template("form.html")

@app.route('/prediction' , methods =  ['GET' , 'POST'])
@cross_origin()
def pred_page():
    if request.method=='POST':
        Precipitation = float(request.form["Precipitation"])
        Dry_Bulb_Temp = float(request.form["Dry_Bulb_Temp"])
        Wet_Bulb_Temp=  float(request.form["Wet_Bulb_Temp"])
        Relative_Humidity = float(request.form["Relative_Humidity"])
        Wind_Speed=  float(request.form["Wind_Speed"])
        Wind_Direction = float(request.form["Wind_Direction"])
        Sea_level_Pressure = float(request.form["Sea_level_Pressure"])

        input = np.array([Dry_Bulb_Temp, Wet_Bulb_Temp, Relative_Humidity, Wind_Speed,Wind_Direction, Sea_level_Pressure, Precipitation]).reshape(1,7)

        # enterTable(Dry_Bulb_Temp, Wet_Bulb_Temp, Relative_Humidity, Wind_Speed,Wind_Direction, Sea_level_Pressure, Precipitation)

        model , scaler = get_serialized_objects()

        output = model.predict(np.array(scaler.transform(input)).reshape(1,7))
        return render_template('prediction.html' , result = str(round(output[0],2)))

def get_serialized_objects():
    path = 'Final_Model//'
    randomforest_obj = joblib.load(path+"XGBoost.pickle")
    scaler_obj = joblib.load(path+"scaler_obj.pickle")
    return randomforest_obj , scaler_obj

if __name__ == "__main__":

    app.run(debug=True)


