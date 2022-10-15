from deepClassifier.config import ConfigurationManager
from deepClassifier.components import PrepareCallback,PrepareTraining
from deepClassifier.entity import PrepareCallbackConfig,PrepareTrainingConfig
from deepClassifier import logger

STAGE_NAME = "Prepare Train stage"

def main():
    config=ConfigurationManager()
    prepare_Callback_config=config.get_prepare_callback_config()
    prepare_Callback =PrepareCallback(config=prepare_Callback_config)
    callback_list=prepare_Callback.get_tb_ckpt_callbacks()

    prepare_training_config=config.get_prepare_training_config()
    prepare_training =PrepareTraining(config=prepare_training_config)
    prepare_training.get_base_model()
    prepare_training.train_valid_generator()
    prepare_training.train(
        callback_list=callback_list
        )

if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<")
        main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<\n\nx=========x")
    except Exception as e:
        logger.exception(e)
        raise e