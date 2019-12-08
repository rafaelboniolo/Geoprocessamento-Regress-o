import sys
import argparse
from regressor import knn as regressor_knn
from regressor import random_forest as regressor_rf
sys.path
from util import path_builder
from util import cross_validation
from util import initialize_dataset
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsRegressor as KNN
from sklearn.model_selection import GridSearchCV
from tqdm import tqdm
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)


def run_knn (k=3, metric="euclidean", weigth="uniform", cv=2, separate_coords=False):
    
    if k == None:
        k = 3
    if metric == None:
        metric = "euclidean"
    if weigth == None:
        weigth = "uniform"
    if cv == None:
        cv = 2
    if separate_coords == None:
        separate_coords = False
        

    print("##################################")
    print("## Running KNN with params: ")
    print("## {} neighbors".format(k))
    print("## {} metric".format(metric))
    print("## {} weigth".format(weigth))
    print("## {} CrossValidation".format(cv))
    print("##################################")


    try:
        
        resultados = []
        resultados_x = []
        resultados_y = []

        train, test = cross_validation.split(initialize_dataset.get_train(),int(cv))

        for i, j in zip(train, test):    
        
            dict_params = initialize_dataset.split_data_cv(i, j, separate_coords=separate_coords) 
            
            if(separate_coords):
                result = regressor_knn.classify_separate(dict_params, k=k, metric=metric, weigth=weigth)
                resultados_x.append(result[0])
                resultados_y.append(result[1])

            else:           
                result = regressor_knn.classify(dict_params, k=k, metric=metric, weigth=weigth)
                resultados.append(result)

        if separate_coords:
            print("Media Coord_x = {}".format(sum(resultados_x)/int(cv)))
            print("Media Coord_y = {}".format(sum(resultados_y)/int(cv)))
        else:
            print("Media Geral = {}".format(sum(resultados)/int(cv)))


    
    except ValueError:
        pass

def run_random_forest (depth=100, estimators=1000, cv=2, separate_coords=False):

    if depth == None:
        depth = 100
    if estimators == None:
        estimators = 1000
    if cv == None:
        cv = 2
    if separate_coords == None:
        separate_coords = False

    print("##################################")
    print("## Running RandomForest with params: ")
    print("## {} max_depth".format(depth))
    print("## {} n_estimators".format(estimators))
    print("## {} CrossValidation".format(cv))
    print("##################################")

    try:
        
        resultados = []
        resultados_x = []
        resultados_y = []

        train, test = cross_validation.split(initialize_dataset.get_train(),int(cv))

        for i, j in zip(train, test):
        
            dict_params = initialize_dataset.split_data_cv(i, j, separate_coords=separate_coords) 
            
            if(separate_coords):                
                result = regressor_rf.classify_separate(dict_params, max_depth=depth, n_estimators=estimators)
                resultados_x.append(result[0])
                resultados_y.append(result[1])

            else:
                result = regressor_rf.classify(dict_params, max_depth=depth, n_estimators=estimators)
                resultados.append(result)

        if separate_coords:
            print("Media Coord_x = {}".format(sum(resultados_x)/int(cv)))
            print("Media Coord_y = {}".format(sum(resultados_y)/int(cv)))
        else:
            print("Media Geral = {}".format(sum(resultados)/int(cv)))


    
    except ValueError:
        pass
