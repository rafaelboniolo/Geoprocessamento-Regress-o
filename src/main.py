import sys
import argparse
from classifier import knn
sys.path

# ap = argparse.ArgumentParser()
# ap.add_argument("-k", "--K", required=True, help="Valor de K")

# args = vars(ap.parse_args())


# k = args["k"]

# if k.isnumeric():
    # print('knn executando com k = '+ k)
knn.classify()
# else:
    # print('knn executando com k = 3')
    # knn.classify()
