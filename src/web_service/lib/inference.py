import os
from typing import Optional

import numpy as np
from lib.preprocessing import process_data
from sklearn.linear_model import Ridge
from utils import load_pickle


def batch_predict_workflow(
    data: dict,
    model: Optional[Ridge] = None,
    artifacts_filepath: Optional[str] = None,
) -> np.ndarray:
    """Make predictions on a new dataset"""

    if model is None:
        model = load_pickle(os.path.join(artifacts_filepath, "model.pkl"))

    X = process_data(data=data, with_target=False)

    return model.predict(X)[0]
