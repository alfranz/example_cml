from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import plot_confusion_matrix
import matplotlib.pyplot as plt
import json
import os
import numpy as np
import joblib
import logging

# Read in data

logging.info("Reading data ...")

X_train = np.genfromtxt("data/train_features.csv")
y_train = np.genfromtxt("data/train_labels.csv")


# Fit a model
depth = 4
logging.info("Fitting model ...")
clf = RandomForestClassifier(max_depth=depth)
clf.fit(X_train,y_train)
logging.info("Saving model ...")
joblib.dump(clf, "data/clf.joblib")


logging.info("Done!")