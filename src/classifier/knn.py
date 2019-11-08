from sklearn.neighbors import KNeighborsRegressor as KNN
import pandas as pd
import sys
import numpy as np
sys.path

PATH = "C:\\Users\\rafae\\Documents\\GitHub\\Geoprocessamento-Regressao\\src\\classifier\\data.csv"

def classify(k=3):

    data = pd.read_csv(PATH)
    x_train = pd.get_dummies(np.array(data.head()['relevo_local']))
    y_train = []

    for i in range(0, len(np.array(data.head()['coord_x']))):
        y_train.append(
                [
                    np.array(data.head()['coord_x']).astype(np.float)[i], 
                    np.array(data.head()['coord_y']).astype(np.float)[i]
                    
                ]
            )
   
    

    classifier = KNN(n_neighbors=k, weights="uniform", metric="hamming")
    
    classifier.fit(x_train, y_train)

    x = classifier.predict(x_train)

    print(x)