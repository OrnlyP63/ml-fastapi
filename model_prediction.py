from typing import List
from joblib import load


def prediction(data_array:List):
    '''
    model: Trainedn SVC Model 
    data_array: input data for model
    '''
    model = load('svc.joblib')
    return model.predict([data_array])[-1]

# from sklearn.base import BaseEstimator # model: BaseEstimator=model
