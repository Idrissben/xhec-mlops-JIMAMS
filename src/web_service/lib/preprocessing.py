import pandas as pd


def encode_sex(df):
    """
    Encode the 'Sex' column in the DataFrame using one-hot encoding,
    ensuring the presence of "F", "M", and "I" columns.
    Combine the resulting one-hot encoded columns with the original
    DataFrame by concatenation.

    Parameters:
    df (pandas.DataFrame): The input DataFrame containing a 'Sex' column
    to be one-hot encoded.

    Returns:
    pandas.DataFrame: A new DataFrame with the 'Sex' column encoded using
    one-hot encoding.
    """

    # Ensure the 'Sex' column has "F", "M", and "I" categories
    # One-hot encode the 'Sex' column
    one_hot = pd.get_dummies(df["Sex"], prefix="", prefix_sep="")

    # Ensure the presence of "F", "M", and "I" columns
    for col in ["F", "M", "I"]:
        if col not in one_hot.columns:
            one_hot[col] = 0

    # Order columns
    one_hot = one_hot[["F", "M", "I"]]

    # Combine the resulting one-hot encoded columns with the original DataFrame
    data_one_hot = pd.concat([one_hot, df.drop(columns="Sex")], axis=1)

    return data_one_hot


def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


def process_data(data: dict, with_target: bool = True) -> pd.DataFrame:
    """Preprocess data"""
    # Read data
    df = pd.DataFrame(data, index=[0])

    df.rename(
        columns={
            "Whole_weight": "Whole weight",
            "Shucked_weight": "Shucked weight",
            "Viscera_weight": "Viscera weight",
            "Shell_weight": "Shell weight",
        },
        inplace=True,
    )

    # Preprocess data
    df = encode_sex(df)

    # Ensure right order
    df = df[
        [
            "F",
            "I",
            "M",
            "Length",
            "Diameter",
            "Height",
            "Whole weight",
            "Shucked weight",
            "Viscera weight",
            "Shell weight",
        ]
    ]

    return df
