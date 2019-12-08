import os

def getData():
    return os.path.dirname(__file__).replace('\\util', '\\data')+("\\data.csv")

def getDataCamada():
    return os.path.dirname(__file__).replace('\\util', '\\data')+("\\ctb0022-camada.csv")

def getDataObservacao():
    return os.path.dirname(__file__).replace('\\util', '\\data')+("\\ctb0022-observacao.csv")
