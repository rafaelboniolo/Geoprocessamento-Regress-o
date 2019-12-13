from sklearn.neighbors import KNeighborsRegressor as KNN
import pandas as pd
import math
import sys
sys.path
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import mean_absolute_error as mae
import numpy as np

def regress_train(dict_params, max_depth, n_estimators):

    score ={}

    regr = RandomForestRegressor(max_depth=int(max_depth), random_state=0, n_estimators=int(n_estimators))
    regr.fit(dict_params['x_train'], dict_params['y_train'])
    predicted = regr.predict(dict_params['x_test'])
    score['r2'] = regr.score(dict_params['x_train'], dict_params['y_train'])
    score['mse'] = mse(dict_params['y_test'], predicted)
    score['rmse'] = math.sqrt(score['mse'])
    score['mae'] = mae(dict_params['y_test'], predicted)
    print("Geral: R2 {} - MSE {} - RMSE {} - MAE {}".format(round(score['r2'], 2), score['mse'], score['rmse'], score['mae']))

    return score

def regress_values(x_train, y_train, x_test, y_test, labels, max_depth, n_estimators):


    regr = RandomForestRegressor(max_depth=int(max_depth), random_state=0, n_estimators=int(n_estimators))
    regr.fit(x_train, y_train)
    predicteds = regr.predict(x_test)
    score = regr.score(x_train, y_train)
    print("R2 {}".format(score))

    for label, predicted in zip(labels, predicteds):
        print("{} coord_x: {} coord_y: {}".format(label, predicted[0], predicted[1]))


def regress_separate_train(dict_params, max_depth, n_estimators):

    score ={}

    regr = RandomForestRegressor(max_depth=int(max_depth), random_state=0, n_estimators=int(n_estimators))


    regr.fit(dict_params['x_train'], dict_params['y_train_coord_x'])  
    predicted = regr.predict(dict_params['x_test'])
    score['r2_x']   = float(regr.score(dict_params['x_train'], dict_params['y_train_coord_x']))
    score['mse_x']  = float(mse(dict_params['y_test_coord_x'], predicted))
    score['rmse_x'] = float(math.sqrt(score['mse_x']))
    score['mae_x']  = float(mae(dict_params['y_test_coord_x'], predicted))

    print("Coord_x: R2 {} - MSE {} - RMSE {} - MAE {}".format(round(score['r2_x'], 2), score['mse_x'], score['rmse_x'], score['mae_x']))

    
    regr.fit(dict_params['x_train'], dict_params['y_train_coord_y'])  
    regr.predict(dict_params['x_test'])
    score['r2_y']   = float(regr.score(dict_params['x_train'], dict_params['y_train_coord_y']))
    score['mse_y']  = float(mse(dict_params['y_test_coord_y'], predicted))
    score['rmse_y'] = float(math.sqrt(score['mse_y']))
    score['mae_y']  = float(mae(dict_params['y_test_coord_y'], predicted))

    print("Coord_y: R2 {} - MSE {} - RMSE {} - MAE {}".format(round(score['r2_y'], 2), score['mse_y'], score['rmse_y'], score['mae_y']), end="\n\n")

    return score
