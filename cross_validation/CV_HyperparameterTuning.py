import pandas as pd
import numpy as np
import sklearn
from sklearn.model_selection import    train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.svm import SVR
import joblib
from data_ingestion.data_loader import load_data
from sklearn.metrics import mean_absolute_error , mean_squared_error
load = load_data()
data = load.get_data()


df = joblib.load("..//TrainingData//FinalData.pickle")
df = pd.DataFrame(df)
# print(df)

# RF_model = RandomForestRegressor()
# XG_model = XGBRegressor()
# SVR_model = SVR()
#
# RF_grid = GridSearchCV(RF_model , {'n_estimators':[80 , 100 , 125 , 150] , "criterion":['squared_error', 'absolute_error'] }, n_jobs=-1 , verbose=True)
# XG_grid  = GridSearchCV(XG_model , {'learning_rate':[0.01 , 0.05 , 0.1 ,0.17, 0.3   ],  'gamma':[0.1,0.2,0.4] , 'min_child_weight':[1,5,10]} , n_jobs = -1, verbose=True)
# SVR_grid = GridSearchCV(SVR_model , {'kernel':['linear','poly'] , 'degree':[3]}  , n_jobs = -1, verbose=True)
#
X = df
y = data['VISIBILITY']
X_train , X_test , y_train,  y_test = train_test_split(X , y , test_size=0.3)

#
# RF_grid.fit(X_train , y_train)
# XG_grid(X_train , y_train)
# SVR_grid(X_train , y_train)
#
# rf_pred = RF_grid.predict(X_test)
# xg_pred = XG_grid.predict(X_test)
# scr_pred = SVR_grid(X_test)
#
#
# print('random forest accuracy :',np.sqrt(mean_squared_error(y_test , rf_pred)))
# print('xgboost accuracy :',np.sqrt(mean_squared_error(y_test , xg_pred)))
# print("SVM acuracy" ,np.sqrt(mean_squared_error(y_test , scr_pred)))

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train  ,y_train)
pred=model.predict(X_test)

print(np.sqrt(mean_squared_error(y_test , pred)))
print(model.score(X_test , y_test))
