import sys
import argparse
sys.path
from util import path_builder
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsRegressor as KNN
from sklearn.model_selection import GridSearchCV

def run(x_train, y_train, x_test, y_test, k=1):

    grid_params = {
        'n_neighbors': [11, 5, 7, 3, 19, 13, 15, 1, 23, 9],
        'weights': ['uniform', 'distance'],
        'metric': ['euclidean', 'manhattan', 'hamming', 'minkowski', 'chebyshev' ] 
    }


    gs = GridSearchCV(KNN(), grid_params, verbose=1, cv=int(k), n_jobs=-1)

    gs_results = gs.fit(x_train, y_train)

    print(gs_results.best_score_)
    print(gs_results.best_estimator_)
    print(gs_results.best_params_)
