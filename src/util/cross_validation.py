import numpy as np
from sklearn.model_selection import KFold
import os
import cv2
import sys
sys.path
from tqdm import tqdm

def split(data, folds = 2):

    print("Splitting dataset " + str(folds) + " folds...")
    kf = KFold(folds, shuffle=True, random_state=0)

    conj_train = []
    conj_test = []

    for train, test in kf.split(data):
        conj_train.append(data[train])
        conj_test.append(data[test])

    return conj_train, conj_test
