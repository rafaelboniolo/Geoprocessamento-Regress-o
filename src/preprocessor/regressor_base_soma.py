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

    for i in range(12, len(data['potassio_trocavel_xxx'])):
        potassio = float(str(data['potassio_trocavel_xxx'][i]).replace(',','.')) 
        magnesio = float(str(data['magnesio_trocavel_xxx'][i]).replace(',','.')) 
        calcio   = float(str(data['calcio_trocavel_xxx'][i]).replace(',','.'))

        y_train.append([
            calcio,
            magnesio,
            potassio            
        ])
        
        
        base_soma      = float(str(data['bases_soma'][i]).replace(',','.'))
        carbono   = float(str(data['carbono_xxx_xxx_xxx'][i]).replace(',','.'))
        profundidade   = (float(str(data['profund_inf'][i]).replace(',','.')) + float(str(data['profund_sup'][i]).replace(',','.')))/2 
        
        x_train.append([
            base_soma,
            carbono,
            profundidade
        ])


    for i in range(3, 50):
        base_soma    = float(str(data['bases_soma'][i]).replace(',','.'))
        carbono   = float(str(data['carbono_xxx_xxx_xxx'][i]).replace(',','.'))
        profundidade   = (float(str(data['profund_inf'][i]).replace(',','.')) + float(str(data['profund_sup'][i]).replace(',','.')))/2 
        
        x_test.append([
            base_soma,
            carbono,
            profundidade
        ])

    
    regr = RandomForestRegressor(max_depth=25, random_state=0,
                             n_estimators=500)
    regr.fit(x_train, y_train)  

    
    for i in regr.predict(x_test):
        print(i, '#')


    print(regr.score(x_train, y_train))

