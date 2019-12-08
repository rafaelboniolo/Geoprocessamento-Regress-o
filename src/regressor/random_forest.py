from sklearn.neighbors import KNeighborsRegressor as KNN
import pandas as pd
import sys
sys.path
from sklearn.ensemble import RandomForestRegressor
import numpy as np

def classify(dict_params, max_depth, n_estimators):


    regr = RandomForestRegressor(max_depth=int(max_depth), random_state=0, n_estimators=int(n_estimators))
    regr.fit(dict_params['x_train'], dict_params['y_train'])
    regr.predict(dict_params['x_test'])
    score = regr.score(dict_params['x_train'], dict_params['y_train'])

    print(" => {}".format(round(score, 2)))

    return score

def classify_separate(dict_params, max_depth, n_estimators):

    regr = RandomForestRegressor(max_depth=int(max_depth), random_state=0, n_estimators=int(n_estimators))


    regr.fit(dict_params['x_train'], dict_params['y_train_coord_x'])  
    regr.predict(dict_params['x_test'])
    score_coord_x = regr.score(dict_params['x_train'], dict_params['y_train_coord_x'])

    
    regr.fit(dict_params['x_train'], dict_params['y_train_coord_y'])  
    regr.predict(dict_params['x_test'])
    score_coord_y = regr.score(dict_params['x_train'], dict_params['y_train_coord_y'])

    print(" => Coord_x {}, Coord_y {}".format(round(score_coord_x, 2), round(score_coord_y, 2)))
    return [score_coord_x, score_coord_y]
