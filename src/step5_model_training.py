
from sklearn.pipeline import Pipeline
from xgboost import XGBClassifier
from sklearn.metrics import balanced_accuracy_score, precision_score, recall_score, f1_score, classification_report
import json
import os
import joblib
import logging
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from step0_utility_functions import Utility
import mlflow
import mlflow.sklearn

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

Utility().create_folder('Logs')
params = Utility().read_params()

main_log_folderpath = params['logging_folder_paths']['main_log_foldername']
model_creation_path = params['logging_folder_paths']['model_creation']

file_handler = logging.FileHandler(os.path.join(
    main_log_folderpath, model_creation_path))
formatter = logging.Formatter(
    '%(asctime)s : %(levelname)s : %(filename)s : %(message)s')

file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


class ModelTraining:

    def __init__(self) -> None:
        pass

    def model_training(self):
        """This method is used to train a model on training data and also to evaluate the trained model on the validation data

        Parameters
        -----------

        None

        Returns
        --------
        None
        """

        try:
            main_data_foldername = params['data_location']['main_data_folder']
            processed_stage2_data_foldername = params['data_location']['processed_stage2_data_foldername']
            processed_stage2_data_filename_X_train = params[
                'data_location']['processed_stage2_data_filename_X_train']
            processed_stage2_data_filename_X_val = params[
                'data_location']['processed_stage2_data_filename_X_val']
            processed_stage2_data_filename_y_train = params[
                'data_location']['processed_stage2_data_filename_y_train']
            processed_stage2_data_filename_y_val = params[
                'data_location']['processed_stage2_data_filename_y_val']

            X_train = pd.read_csv(os.path.join(
                main_data_foldername, processed_stage2_data_foldername, processed_stage2_data_filename_X_train)).values
            X_val = pd.read_csv(os.path.join(
                main_data_foldername, processed_stage2_data_foldername, processed_stage2_data_filename_X_val)).values
            y_train = pd.read_csv(os.path.join(main_data_foldername, processed_stage2_data_foldername,
                                               processed_stage2_data_filename_y_train)).values.flatten()
            y_val = pd.read_csv(os.path.join(main_data_foldername, processed_stage2_data_foldername,
                                processed_stage2_data_filename_y_val)).values.flatten()

            # Initializing a machine learning model

            with mlflow.start_run():
                max_depth = params['model']['params']['max_depth']
                n_estimators = params['model']['params']['n_estimators']
                max_leaves = params['model']['params']['max_leaves']
                learning_rate = params['model']['params']['learning_rate']

                mlflow.log_param('max_depth', max_depth)
                mlflow.log_param('n_estimators', n_estimators)
                mlflow.log_param('max_leaves', max_leaves)
                mlflow.log_param('learning_rate', learning_rate)


                xgboost_pipe = XGBClassifier(
                    max_depth=max_depth, n_estimators=n_estimators, max_leaves=max_leaves, learning_rate=learning_rate)
                logger.info('Model initialized')

                # Fitting the model on train data
                xgbc = xgboost_pipe.fit(X_train, y_train)
                logger.info('Model trained on the train data.')

                # Predicting metrics using the trained model and the test data
                y_pred = xgbc.predict(X_val)

                balanced_accuracy_scr = balanced_accuracy_score(y_val, y_pred)
                p_scr = precision_score(y_val, y_pred, average='weighted')
                r_scr = recall_score(y_val, y_pred, average='weighted')
                f1_scr = f1_score(y_val, y_pred, average='weighted')
                clf_report = classification_report(
                    y_val, y_pred, output_dict=True)
                clf_report = pd.DataFrame(clf_report).transpose()

                mlflow.log_metric('balanced_accuracy_score',
                                  balanced_accuracy_scr)
                mlflow.log_metric('precision_score', p_scr)
                mlflow.log_metric('recall_score', r_scr)
                mlflow.log_metric('f1_score', f1_scr)

                logger.info(
                    'Trained model evaluation done using validation data.')

            # Saving the calculated metrics into a json file in the Metrics folder
            metrics_folder = params['metrics_path']['metrics_folder']
            metrics_filename = params['metrics_path']['metrics_file']

            Utility().create_folder(metrics_folder)

            with open(os.path.join(metrics_folder, metrics_filename), 'w') as json_file:
                metrics = dict()
                metrics['balanced_accuracy_score'] = balanced_accuracy_scr
                metrics['precision_score'] = p_scr
                metrics['recall_score'] = r_scr
                metrics['f1_score'] = f1_scr

                json.dump(metrics, json_file, indent=4)

            clf_report_path = params['metrics_path']['clf_report_filename']

            clf_report.to_csv(os.path.join(metrics_folder, clf_report_path))

            logger.info('Saved evaluations in files.')

            # Saving the trained machine learing model in the models folder
            model_foldername = params['model']['model_foldername']
            model_name = params['model']['model_name']

            Utility().create_folder(model_foldername)

            model_dir = os.path.join(model_foldername, model_name)

            joblib.dump(xgbc, model_dir)

            logger.info('Trained model saved as a joblib file.')

        except Exception as e:
            logger.error(e)
            raise e


if __name__ == "__main__":

    mt = ModelTraining()
    mt.model_training()
