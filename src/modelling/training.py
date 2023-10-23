import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


def train_model(X_train: pd.DataFrame, y_train: np.ndarray) -> LinearRegression:
    lr = LinearRegression()
    lr.fit(X_train, y_train)
    return lr
