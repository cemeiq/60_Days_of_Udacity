import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from logisticregression import LogisticRegression
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split


def main():
   
    # GENERATING RANDOM DATA FOR TRAINING TESTING 

    np.random.seed(12)
    num_observations = 5000

    x1 = np.random.multivariate_normal([0, 0], [[1, .75],[.75, 1]], num_observations)
    x2 = np.random.multivariate_normal([1, 4], [[1, .75],[.75, 1]], num_observations)

    simulated_separableish_features = np.vstack((x1, x2)).astype(np.float32)
    simulated_labels = np.hstack((np.zeros(num_observations),
                              np.ones(num_observations)))
    
    X_train, X_test, y_train, y_test = train_test_split(simulated_separableish_features, simulated_labels, test_size=0.33)

    clf = LogisticRegression(10,5e-5)
    clf.fit(X_train,y_train)
    y_pred = clf.predict(X_test)
    print(y_pred)


if __name__ == "__main__":
    main()
