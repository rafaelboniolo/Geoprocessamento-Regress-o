import sys
sys.path
import pandas as pd
import numpy as np
from util import path_builder
                   

def run():

    PATH = path_builder.getDataCamada()

    data = pd.read_csv(PATH)

    data = data['camada_nome'].str.get_dummies()

    data.to_csv(r'./taxon.csv')