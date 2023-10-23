from typing import Tuple

import numpy as np
import pandas as pd
from loguru import logger
from prefect import flow, task


@task(name="compute target")
def compute_target(df):
    """
    Calculate the 'age' column in the DataFrame by adding 1.5 to the 'Rings'
    column, and remove the 'Rings' column from the DataFrame.

    Parameters:
    df (pandas.DataFrame): The input DataFrame containing a 'Rings' column.

    Returns:
    pandas.DataFrame: A modified DataFrame with the 'Rings' column removed
    and a new 'age' column.
    """
    df["age"] = df["Rings"] + 1.5
    df = df.drop(columns=["Rings"])
    return df


@task(name="encode sex")
def encode_sex(df):
    """
    Encode the 'Sex' column in the DataFrame using one-hot encoding,
    and combine the resulting one-hot encoded columns with the original
    DataFrame by concatenation.

    Parameters:
    df (pandas.DataFrame): The input DataFrame containing a 'Sex' column
    to be one-hot encoded.

    Returns:
    pandas.DataFrame: A new DataFrame with the 'Sex' column encoded using
    one-hot encoding.
    """

    one_hot = pd.get_dummies(df["Sex"])
    one_hot = one_hot.astype(int)
    data_one_hot = pd.concat([one_hot, df.drop(columns="Sex")], axis=1)
    return data_one_hot


@task(name="load data")
def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


@task(name="extract x_y")
def extract_x_y(df: pd.DataFrame, with_target=True) -> Tuple[pd.DataFrame, np.ndarray]:
    y = None
    if with_target:
        y = df["age"].values
    X = df.drop(columns={"age"})
    return X, y


@flow(name="Process data")
def process_data(file_path: str, with_target: bool = True) -> pd.DataFrame:
    """Preprocess data"""
    # Read data
    df = load_data(file_path)

    # Preprocess data
    logger.debug(f"{file_path} | Encoding sex...")
    df = encode_sex(df)

    df = compute_target(df)

    logger.debug(f"{file_path} | Extracting X & y...")
    return extract_x_y(df, with_target=with_target)
