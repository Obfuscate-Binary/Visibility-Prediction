import pandas as pd
import numpy as np
import sklearn
import matplotlib
import seaborn
import flask
import flask_cors
import pandas_profiling
from sklearn.cluster import DBSCAN
from sklearn.decomposition import PCA
from sklearn.model_selection import GridSearchCV
import pickle
from model_building.reducing_features import clusters
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
from data_ingestion.data_loader import load_data
from model_building.reducing_features import  clusters

#
# d1 = load_data()
# op =  d1.get_data()

# op.drop('DATE')

# c1 = clusters(min_samples=[10,20,30 ,50,70,100,150,200,300,350,400] , eps=[0.5 , 1,4,10,20,30,40,50,60,70,80,90,100])
# c1 = clusters(400 , 100)
# final  = c1.makeclusters(op.drop(columns = ['DATE']))
app = flask.Flask(__name__)


@app.route('/' , methods =  ['GET' , 'POST'])
def home_page():
    return render_template("form.html")

@app.route('/prediction' , methods =  ['GET' , 'POST'])
def pred_page():
    #return render_template("form.html")
    return jsonify('Its prediction page')



app.run(debug=True)


