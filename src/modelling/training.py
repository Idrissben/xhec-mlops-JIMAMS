import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV


def train_model(X_train: pd.DataFrame, y_train: np.ndarray) -> Ridge:
    param_grid = {"alpha": [0.1, 0.5, 1.0, 5.0, 10.0]}
    ridge = Ridge()
    grid_ridge = GridSearchCV(estimator=ridge, param_grid=param_grid)
    grid_ridge.fit(X_train, y_train)
    best_ridge = grid_ridge.best_estimator_
    return best_ridge
