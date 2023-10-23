# Use this module to code a `pickle_object` function.
# This will be useful to pickle the model (and encoder if need be).
import pickle
import random

from prefect import flow, task


@task(name="Save pickle")
def save_pickle(file_path, obj):
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


@task(name="Load pickle")
def load_pickle(file_path):
    with open(file_path, "rb") as file:
        model = pickle.load(file)

    return model


@task(retries=3, retry_delay_seconds=60)
def failure():
    print("running")
    if random.randint(1, 10) % 2 == 0:
        raise ValueError("This number is not even")


@flow()
def test_failure():
    failure()


@task(name="Load", tags=["Serialize"])
def task_load_pickle(path: str):
    with open(path, "rb") as f:
        loaded_obj = pickle.load(f)
    return loaded_obj


@task(name="Save", tags=["Serialize"])
def task_save_pickle(path: str, obj: dict):
    with open(path, "wb") as f:
        pickle.dump(obj, f)
