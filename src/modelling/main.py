# This module is the training flow: it reads the data, preprocesses it, trains
# a model and saves it.
import argparse
from pathlib import Path

import pandas as pd
from preprocessing import compute_target, encode_sex, extract_x_y, load_data
from settings import TRAIN_DATA_PATH, MODELS_PATH
from sklearn.model_selection import train_test_split
from training import train_model
from utils import save_pickle


def main(trainset_path: Path, model_path: Path) -> None:
    """Train a model using the data at the given path and save
    the model (pickle)."""
    # Read data
    df = pd.read_csv(trainset_path)
    print("load")
    # Preprocess data
    df = compute_target(df)
    df = encode_sex(df)
    print("preprocess")
    # Train model
    train_df, test_df = train_test_split(df, test_size=0.3, random_state=42)
    X_train, y_train = extract_x_y(train_df)
    X_test, y_test = extract_x_y(test_df)
    print("almost training")
    model = train_model(X_train, y_train)
    print("trained")
    # Pickle model --> The model should be saved in pkl format the
    # `src/web_service/local_objects` folder
    save_pickle(model, model_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train a model using the data at the given path.")
    parser.add_argument(
        "trainset_path",
        type=Path,
        nargs="?",
        default=TRAIN_DATA_PATH,
        help="Path to the training set (default is DATA_PATH)",
    )
    parser.add_argument(
        "model_path",
        type=Path,
        nargs="?",
        default=MODELS_PATH,
        help="Path to the training set (default is DATA_PATH)",
    )
    args = parser.parse_args()
    main(args.trainset_path, args.model_path)
