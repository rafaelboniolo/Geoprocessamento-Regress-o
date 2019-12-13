import sys
import argparse
sys.path

from util import cross_validation
from util import path_builder
from util import initialize_dataset
from preprocessor import gridsearch
from util import facade_regressor

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ap = argparse.ArgumentParser()
ap.add_argument("-k", "--k", required=False, help="Valor de K")
ap.add_argument("-m", "--metric", required=False, help="Métrica de distância")
ap.add_argument("-w", "--weight", required=False, help="Peso")
ap.add_argument("-cv", "--crossvalidation", required=False, help="Ativar Cross validation")
ap.add_argument("-c", "--classifier", required=False, help="Classificador")
ap.add_argument("-d", "--depth", required=False, help="Depth")
ap.add_argument("-e", "--estimators", required=False, help="N Estimators")
ap.add_argument("-sep", "--separate", required=False, help="Separate Coords")
ap.add_argument("-gs", "--gridsearch", required=False, help="Grid Search")


args = vars(ap.parse_args())


k          = args["k"]
metric     = args["metric"]
weigth     = args["weight"]
cv         = args["crossvalidation"]
c          = args["classifier"]
depth      = args["depth"]
estimators = args["estimators"]
separate   = args["separate"]
gs         = args["gridsearch"]


if c == "knn":
    facade_regressor.run_knn_train(k, metric, weigth, cv, separate)
elif c == "rf":
    facade_regressor.run_random_forest_train(depth, estimators, cv, separate)
elif c == "regress":
    facade_regressor.run_random_forest_values(depth, estimators)
elif gridsearch:
    gridsearch.run(gs)


# regressor_aluminio_kcl.run()
# regressor_aluminio_kcl.run()
# regressor_fosforo.run()
# 
# dummies.run()

# knn.classify(initilize_dataset.get_splited(), 3)

# a = cross_validation.split(initilize_dataset.get_train(),4)
# x_train, y_train, x_test, y_test = initialize_dataset.get_splited()
# gridsearch.run(x_train, y_train, x_test, y_test, 2)
