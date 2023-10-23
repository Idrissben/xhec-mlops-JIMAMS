import os
from typing import Optional

import numpy as np
from loguru import logger
from modeling import evaluate_model, predict, train_model
from prefect import flow
from preprocessing import process_data
from sklearn.linear_model import Ridge
from utils import load_pickle, save_pickle


@flow(name="Train model")
def train_model_workflow(
    train_filepath: str,
    test_filepath: str,
    artifacts_filepath: Optional[str] = None,
) -> dict:
    """Train a model and save it to a file"""
    logger.info("Processing training data...")
    X_train, y_train = process_data(file_path=train_filepath, with_target=True)
    logger.info("Processing test data...")
    X_test, y_test = process_data(file_path=test_filepath, with_target=True)
    logger.info("Training model...")
    model = train_model(X_train, y_train)
    logger.info("Making predictions and evaluating...")
    y_pred = predict(X_test, model)
    rmse = evaluate_model(y_test, y_pred)

    if artifacts_filepath is not None:
        logger.info(f"Saving artifacts to {artifacts_filepath}...")
        save_pickle(os.path.join(artifacts_filepath, "model.pkl"), model)

    return {"model": model, "rmse": rmse}


@flow(name="Batch predict", retries=1, retry_delay_seconds=30)
def batch_predict_workflow(
    input_filepath: str,
    model: Optional[Ridge] = None,
    artifacts_filepath: Optional[str] = None,
) -> np.ndarray:
    """Make predictions on a new dataset"""

    if model is None:
        model = load_pickle(os.path.join(artifacts_filepath, "model.pkl"))

    X, _ = process_data(file_path=input_filepath, with_target=False)
    y_pred = predict(X, model)

    return y_pred


if __name__ == "__main__":
    from settings import MODELS_PATH, TEST_DATA_PATH, TRAIN_DATA_PATH

    train_model_workflow(
        train_filepath=TRAIN_DATA_PATH,
        test_filepath=TEST_DATA_PATH,
        artifacts_filepath=MODELS_PATH,
    )

    batch_predict_workflow(
        input_filepath=TEST_DATA_PATH,
        artifacts_filepath=MODELS_PATH,
    )
