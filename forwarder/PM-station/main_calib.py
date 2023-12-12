import joblib # pip install joblib
from sklearn.ensemble import GradientBoostingRegressor # pip install -U scikit-learn
from catboost import CatBoostRegressor # pip install catboost
from xgboost import XGBRegressor # pip install xgboost
import numpy as np # pip install numpy

def calibration(key, value, temperature, humidity):
    if key == 'MP-25_1':
        model = joblib.load("MP2,5_1.joblib")
    elif key == 'MP-10_1':
        model = joblib.load("MP10_1.joblib")
    elif key == 'MP-25_2':
        model = joblib.load("MP2,5_2.joblib")
    elif key == 'MP-10_2':
        model = joblib.load("MP10_2.joblib")

    return model.predict(np.array([value, temperature, humidity]).reshape(1, -1))[0]