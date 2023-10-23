from prefect import serve
from settings import MODELS_PATH, TEST_DATA_PATH, TRAIN_DATA_PATH
from workflows import batch_predict_workflow, train_model_workflow

if __name__ == "__main__":
    train_model_deployment = train_model_workflow.to_deployment(
        name="Model training Deployment",
        version="0.1.0",
        tags=["training", "model"],
        cron="0 0 * * 0",
        parameters={
            "train_filepath": TRAIN_DATA_PATH,
            "test_filepath": TEST_DATA_PATH,
            "artifacts_filepath": MODELS_PATH,
        },
    )

    batch_predict_deployment = batch_predict_workflow.to_deployment(
        name="Batch predict Deployment",
        version="0.1.0",
        tags=["inference"],
        interval=600,
        parameters={
            "input_filepath": TEST_DATA_PATH,
            "artifacts_filepath": MODELS_PATH,
        },
    )
    serve(train_model_deployment, batch_predict_deployment)
