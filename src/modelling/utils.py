# Use this module to code a `pickle_object` function.
# This will be useful to pickle the model (and encoder if need be).
import pickle


def save_pickle(obj, file_path):
    """
    Serialize and save an object to a given file path using pickle.

    Parameters:
    - obj: The Python object to be serialized.
    - file_path: The location where the pickled object will be saved.

    Returns:
    None
    """
    with open(file_path, "wb") as f:
        pickle.dump(obj, f)


def load_pickle(file_path):
    with open(file_path, "rb") as file:
        model = pickle.load(file)

    return model
