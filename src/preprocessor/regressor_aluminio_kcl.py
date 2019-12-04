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

    for i in range(0, len(data['aluminio_kcl_xxx'])):
        
        if '-' in str(data['aluminio_kcl_xxx'][i]):
            continue
        
        ctc     = float(str(data['ctc_xxx_xxx'][i]).replace(',','.')) 
        al_sat  = float(str(data['aluminio_saturacao_calc'][i]).replace(',','.')) 
        ph      = float(str(data['ph_h2o_xxx_xxx'][i]).replace(',','.'))
        al      = float(str(data['aluminio_kcl_xxx'][i]).replace(',','.'))
        

        y_train.append([
            al
        ])
        
        x_train.append([
            ctc,
            al_sat,
            ph            
        ])


        


    for i in range(0, len(data['aluminio_kcl_xxx'])):
        
        if '-' not in str(data['aluminio_kcl_xxx'][i]):
            continue
        
        ctc     = float(str(data['ctc_xxx_xxx'][i]).replace(',','.')) 
        al_sat  = float(str(data['aluminio_saturacao_calc'][i]).replace(',','.')) 
        ph      = float(str(data['ph_h2o_xxx_xxx'][i]).replace(',','.'))
        
        x_test.append([
            ctc,
            al_sat,
            ph            
        ])

    regr = RandomForestRegressor(max_depth=25, random_state=0,
                             n_estimators=700)
    regr.fit(x_train, y_train)  

    exp = regr.predict(x_test)
    
    print(len(exp))

    for i in exp:
        print(i, '#')

    print(regr.score(x_train, y_train))



