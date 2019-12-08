from sklearn.neighbors import KNeighborsRegressor as KNN
import pandas as pd
import sys
sys.path

import numpy as np

def classify(dict_params, k, metric, weigth):

    regr = KNN(n_neighbors=int(k), weights=weigth, metric=metric)
    regr.fit(dict_params['x_train'], dict_params['y_train'])
    y_predicted = regr.predict(dict_params['x_test'])

    score = regr.score(dict_params['x_test'], dict_params['y_test'])

    print(" => {}".format(round(score, 2)))

    return score

def classify_separate(dict_params, k, metric, weigth):

    regr = KNN(n_neighbors=int(k), weights=weigth, metric=metric)

    regr.fit(dict_params['x_train'], dict_params['y_train_coord_x'])  
    regr.predict(dict_params['x_test'])
    score_coord_x = regr.score(dict_params['x_train'], dict_params['y_train_coord_x'])

    
    regr.fit(dict_params['x_train'], dict_params['y_train_coord_y'])  
    regr.predict(dict_params['x_test'])
    score_coord_y = regr.score(dict_params['x_train'], dict_params['y_train_coord_y'])

    print(" => Coord_x {}, Coord_y {}".format(round(score_coord_x, 2), round(score_coord_y, 2)))
    return [score_coord_x, score_coord_y]