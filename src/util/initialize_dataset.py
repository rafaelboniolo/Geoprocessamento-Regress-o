import sys
sys.path

from util import path_builder
import pandas as pd
import numpy as np

def get_splited():
    PATH = path_builder.getDataCamada()

    data = pd.read_csv(PATH)

    x_train = []
    y_train = []

    x_test = []
    y_test = []

    test = data.loc[(data['coord_x'] == '-') | (data['coord_y'] == '-')]
    train = data.drop(test.index)


    train.drop('observacao_id', inplace=True, axis=1)
    labels = test['observacao_id']
    test.drop('observacao_id', inplace=True, axis=1)

    for i, j in zip(train['coord_x'], train['coord_y']):
        y_train.append([float(i), float(j)])
    
    train.drop('coord_x', inplace=True, axis=1)
    train.drop('coord_y', inplace=True, axis=1)

    test.drop('coord_x', inplace=True, axis=1)
    test.drop('coord_y', inplace=True, axis=1)

    x_train = train.to_numpy().astype(np.float)
    x_test = test.to_numpy().astype(np.float)
    

    return x_train, y_train, x_test, y_test, labels.to_numpy().astype(np.str)

def get_train():
    PATH = path_builder.getDataCamada()

    data = pd.read_csv(PATH)

    x_train = []

    data.drop('observacao_id', inplace=True, axis=1)
    test = data.loc[(data['coord_x'] == '-') | (data['coord_y'] == '-')]
    train = data.drop(test.index)


    train = train.to_numpy().astype(np.float)

    return train

def split_data_cv(train, test, separate_coords):
    train = pd.DataFrame(train)
    test = pd.DataFrame(test)

    x_train = []
    y_train = []
    
    y_train_coord_x = []
    y_train_coord_y = []

    x_test = []
    y_test = []

    y_test_coord_x = []
    y_test_coord_y = []

    params = {}
 
    if separate_coords:
        for i, j in zip(test[0], test[1]):
            y_test_coord_x.append(float(i))
            y_test_coord_y.append(float(j))

        for i, j in zip(train[0], train[1]):
            y_train_coord_x.append(float(i))
            y_train_coord_y.append(float(j))
    
    else:
        for i, j in zip(test[0], test[1]):
            y_test.append([float(i), float(j)])

        for i, j in zip(train[0], train[1]):
            y_train.append([float(i), float(j)])
    
    
    train.drop(0, inplace=True, axis=1)
    train.drop(1, inplace=True, axis=1)

    test.drop(0, inplace=True, axis=1)
    test.drop(1, inplace=True, axis=1)

    params['x_train'] = np.array(train).astype(np.float)
    params['y_train'] = np.array(y_train).astype(np.float)
    params['x_test']  = np.array(test).astype(np.float)
    params['y_test']  = np.array(y_test).astype(np.float)
    params['y_test_coord_x']  = np.array(y_test_coord_x).astype(np.float)
    params['y_test_coord_y']  = np.array(y_test_coord_y).astype(np.float)
    params['y_train_coord_x'] = np.array(y_train_coord_x).astype(np.float)
    params['y_train_coord_y'] = np.array(y_train_coord_y).astype(np.float)

    return params