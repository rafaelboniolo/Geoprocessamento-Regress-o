import sys
import argparse
sys.path
from util import path_builder
from util import initialize_dataset
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsRegressor as KNN
from sklearn.model_selection import GridSearchCV
from sklearn.exceptions import UndefinedMetricWarning
from sklearn.model_selection import LeaveOneOut
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=UndefinedMetricWarning)

def run(cv=3):

    if cv == None:
        cv = 3

    grid_params = {
        'n_neighbors': [11, 5, 7, 3, 9, 13, 2],
        'weights': ['uniform', 'distance'],
        'metric': ['euclidean', 'manhattan' ] 
    }

    x_train, y_train, x_test, y_test, labels = initialize_dataset.get_splited()

    params = initialize_dataset.split_data_cv(x_train, y_train, True)

    gs = GridSearchCV(KNN(), grid_params, verbose=1, cv=int(cv), n_jobs=-1, scoring="explained_variance")

    gs_results = gs.fit(params['x_train'], params['y_train_coord_x'])

    print(gs_results.best_score_)
    print(gs_results.best_estimator_)
    print(gs_results.best_params_)
