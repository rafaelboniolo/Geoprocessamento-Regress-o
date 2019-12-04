import sys
sys.path
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsRegressor as KNN
from sklearn.model_selection import GridSearchCV
from util import path_builder

from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import make_regression
                   

def run():

    PATH = path_builder.getDataCamada()

    data = pd.read_csv(PATH)

    x_train = []
    y_train = []

    x_test = []
    y_test = []

    for i in range(0, len(data['fosforo_xxx_xxx'])):
        
        if '-' in str(data['fosforo_xxx_xxx'][i]):
            continue
        
        carbono = float(str(data['carbono_xxx_xxx_xxx'][i]).replace(',','.')) 
        argila = float(str(data['argila_xxx_xxx'][i]).replace(',','.'))
        fosforo = float(str(data['fosforo_xxx_xxx'][i]).replace(',','.'))
        profundidade = (float(str(data['profund_sup'][i]).replace(',','.')) + float(str(data['profund_inf'][i]).replace(',','.')))/2

        y_train.append([
            fosforo
        ])
        
        x_train.append([
            carbono,
            argila,
            profundidade
        ])


        


    for i in range(0, len(data['fosforo_xxx_xxx'])):
        
        if '-' not in str(data['fosforo_xxx_xxx'][i]):
            continue
        
        carbono = float(str(data['carbono_xxx_xxx_xxx'][i]).replace(',','.')) 
        argila = float(str(data['argila_xxx_xxx'][i]).replace(',','.'))
        profundidade = (float(str(data['profund_sup'][i]).replace(',','.')) + float(str(data['profund_inf'][i]).replace(',','.')))/2

        x_test.append([
            carbono,
            argila,
            profundidade
        ])


    regr = RandomForestRegressor(max_depth=25, random_state=0,
                             n_estimators=500)
    regr.fit(x_train, y_train)  

    exp = regr.predict(x_test)
    
    print(len(exp))

    for i in exp:
        print(i, '#')

    print(regr.score(x_train, y_train))



