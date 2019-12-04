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

    for i in range(0, len(data['acidez_potencial_xxx'])):
        
        if '-' in str(data['acidez_potencial_xxx'][i]):
            continue
        
        ctc                    = float(str(data['areia_xxx_xxx'][i]).replace(',','.')) 
        silte                    = float(str(data['carbono_xxx_xxx_xxx'][i]).replace(',','.')) 
        argila                   = float(str(data['argila_xxx_xxx'][i]).replace(',','.'))
        
        y_train.append([
            areia,
            silte,
            argila
        ])
        
        x_train.append([
            textura_argilosa,
            textura_argilosa_c,
        ])


        

argila
carbono
ctc
    for i in range(0, len(data['acidez_potencial_xxx'])):
        
        if '-' not in str(data['acidez_potencial_xxx'][i]):
            continue
        
        textura_argilosa         = float(str(data['textura_argilosa'][i]).replace(',','.'))
        textura_argilosa_c       = float(str(data['textura_argilosa_cascalhenta'][i]).replace(',','.'))
        textura_muito_argilosa   = float(str(data['textura_muito_argilosa'][i]).replace(',','.'))
        textura_m_argilosa_c     = float(str(data['textura_muito_argilosa_cascalhenta'][i]).replace(',','.'))
        textura_media            = float(str(data['textura_média'][i]).replace(',','.'))
        
        x_test.append([
            textura_argilosa,
            textura_argilosa_c,
            textura_argilosa,            
            textura_m_argilosa_c,
            textura_media            
        ])

    regr = RandomForestRegressor(max_depth=25, random_state=0,
                             n_estimators=700)
    regr.fit(x_train, y_train)  

    exp = regr.predict(x_test)
    
    print(len(exp))

    for i in exp:
        print(i, '#')

    print(regr.score(x_train, y_train))



