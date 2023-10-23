import numpy as np
import scipy.sparse
from prefect import task
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


@task(name="Train model")
#def train_model

@task(name="Make predictions")
#def predict



@task(name="Evaluate model")
#def evaluate_model(y_true: np.ndarray, y_pred: np.ndarray) -> float:
