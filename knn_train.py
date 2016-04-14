#!/usr/bin/env python
# @see http://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_ml/py_knn/py_knn_opencv/py_knn_opencv.html
import os
import re
import numpy
import cv2

from src import KNN

# read training data
train_txts = []
train_imgs = []
with open('train/content.txt', 'r') as f:
    for line in f:
        if re.match(line, r'^\s*#'): continue
        img_filename, txt = line.split(None, 1)
        train_txts.append(txt.strip())
        train_imgs.append(cv2.imread('train/' + img_filename, 0))

knn = KNN()
knn.train(train_imgs, train_txts)
knn.save('knn_data.npz')

