import os

def getData():
    return os.path.dirname(__file__).replace('\\util', '\\data')+("\\data.csv")

getData()