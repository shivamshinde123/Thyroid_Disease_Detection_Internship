from step0_utility_functions import Utility
import pandas as pd
import numpy as np
import os
import dill
import logging
import shutil

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

Utility().create_folder('Logs')
params = Utility().read_params()

main_log_folderpath = params['logging_folder_paths']['main_log_foldername']
data_preprocess1_path = params['logging_folder_paths']['data_preprocess']

file_handler = logging.FileHandler(os.path.join(
    main_log_folderpath, data_preprocess1_path))
formatter = logging.Formatter(
    '%(asctime)s : %(levelname)s : %(filename)s : %(message)s')

file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


class PreprocessStage2:

    def __init__(self) -> None:
        pass

    def preprocess2(self):
        """This method is used to perform the following operations:

        - encoding target feature
        - encoding categorical and numerical features
        - imputing categorical and numerical featurs
        - saving all the fitted transformers
        - saving all the processed data
        - removing interm data directories

        Parameters
        -----------

        None

        Returns
        --------
        None
        """

        try:
            main_data_foldername = params['data_location']['main_data_folder']
            processed_stage1_data_foldername = params['data_location']['processed_stage1_data_foldername']
            processed_stage1_data_filename = params['data_location']['processed_stage1_data_filename']

            # Loading the partial processed data
            df = pd.read_csv(os.path.join(main_data_foldername, processed_stage1_data_foldername,
                                          processed_stage1_data_filename))

            # Getting the column names (except the target feature name)
            all_columns = df.columns.values
            all_columns = list(all_columns)
            all_columns = all_columns[:-1]

            target_column_name = params['General']['target_column_name']

            # Splitting the data into independent and dependent features
            X = df.drop(target_column_name, axis=1)
            y = df[target_column_name]
            logger.info(
                'Splitted the data into independent and dependent features.')

            # label encoding the target column
            le_transformer = LabelEncoder()
            y = le_transformer.fit_transform(y)

            # Saving the label encoder transformer to pickle file
            preprocess_pipe_foldername = params['preprocess']['preprocess_pipe_foldername']
            le_transformer_filename = params['preprocess']['le_transformer_filename']

            # Creating a Data folder to save the preprocess_pipeline
            Utility().create_folder(preprocess_pipe_foldername)

            # Saving the label encoder fitting earlier
            with open(os.path.join(preprocess_pipe_foldername, le_transformer_filename), 'wb') as f:
                dill.dump(le_transformer, f)

            # Splitting the data inot the data for training and the data for validation
            random_state = params['General']['random_state']
            test_size = params['General']['test_size']

            X_train, X_val, y_train, y_val = train_test_split(
                X, y, random_state=random_state, test_size=test_size)
            logger.info(
                'Splitted the data into the data for training and the data for validation.')

            X_train = pd.DataFrame(X_train, columns=all_columns)
            X_val = pd.DataFrame(X_val, columns=all_columns)

            # finding the names of numerical and categorical columns
            cat_cols = [
                feature for feature in X_train.columns if X_train[feature].dtypes == 'O']
            num_cols = [
                feature for feature in X_train.columns if feature not in cat_cols]

            # creating a pipeline to fill the null values and encode the values in categorical columns
            cat_pipe = Pipeline([

                ('cat_imputer1', SimpleImputer(missing_values=np.nan,
                                               strategy='most_frequent', add_indicator=False)),
                ('cat_encoder', OrdinalEncoder(
                    handle_unknown='use_encoded_value', unknown_value=np.nan)),
                ('cat_imputer2', SimpleImputer(
                    missing_values=np.nan, strategy='most_frequent'))
            ])
            logger.info(
                'Created a pipeline to preprocess the categorical features in the data.')

            # Creating numerical pipeline
            num_pipe = Pipeline([
                ('num_imputer', SimpleImputer(missing_values=np.nan,
                                              strategy='most_frequent', add_indicator=False))
            ])
            logger.info(
                'Created a pipeline to preprocess the numerical features in the data.')

            # Creating a combined preprocess pipeline, training it and then saving it.
            preprocess_pipe = ColumnTransformer([
                ('num_pipeline', num_pipe, num_cols),
                ('cat_pipeline', cat_pipe, cat_cols)
            ], remainder='passthrough')
            logger.info(
                'Combined the preprocess pipelines created for categorical and numerical data preprocessing.')

            # Transforming the train and validation data using preprocess pipeline
            X_train = preprocess_pipe.fit_transform(X_train)
            logger.info(
                'Trained the whole preprocess pipeline on the train data.')
            logger.info(
                'Transformed the train data using fitted preprocess pipeline.')

            X_val = preprocess_pipe.transform(X_val)
            logger.info(
                'Transformed the test data using fitted preprocess pipeline.')

            # Saving the fitted preprocess pipeline
            preprocess_pipe_filename = params['preprocess']['preprocess_pipe_filename']
            preprocess_pipe_path = os.path.join(
                preprocess_pipe_foldername, preprocess_pipe_filename)

            with open(preprocess_pipe_path, 'wb') as pickle_file:
                dill.dump(preprocess_pipe, pickle_file)
            logger.info(
                'Saved the fitted preprocess pipeline as a python pickle file.')

            # saving the final processes data
            # Saving X_train, X_val, y_train, y_val
            processed_stage2_data_foldername = params['data_location']['processed_stage2_data_foldername']

            # Creating a Data folder to save the processed data
            Utility().create_folder(main_data_foldername)
            Utility().create_folder(os.path.join(
                main_data_foldername, processed_stage2_data_foldername))

            processed_stage2_data_filename_X_train = params[
                'data_location']['processed_stage2_data_filename_X_train']
            X_train = pd.DataFrame(X_train)
            X_train.columns = all_columns
            X_train.to_csv(os.path.join(
                main_data_foldername, processed_stage2_data_foldername, processed_stage2_data_filename_X_train), index=False, sep=',')
            logger.info('Preprocess X_train saved.')

            processed_stage2_data_filename_X_val = params[
                'data_location']['processed_stage2_data_filename_X_val']
            X_val = pd.DataFrame(X_val)
            X_val.columns = all_columns
            X_val.to_csv(os.path.join(
                main_data_foldername, processed_stage2_data_foldername, processed_stage2_data_filename_X_val), index=False, sep=',')
            logger.info('Preprocessed X_val saved')

            processed_stage2_data_filename_y_train = params[
                'data_location']['processed_stage2_data_filename_y_train']
            y_train = pd.DataFrame(y_train)
            y_train.columns = ['target']
            y_train.to_csv(os.path.join(
                main_data_foldername, processed_stage2_data_foldername, processed_stage2_data_filename_y_train), index=False, sep=',')
            logger.info('Preprocessed y_train saved')

            processed_stage2_data_filename_y_val = params[
                'data_location']['processed_stage2_data_filename_y_val']
            y_val = pd.DataFrame(y_val)
            y_val.columns = ['target']
            y_val.to_csv(os.path.join(
                main_data_foldername, processed_stage2_data_foldername, processed_stage2_data_filename_y_val), index=False, sep=',')
            logger.info('Preprocessed y_val saved')

            # Removing the interm data directories since they are of no use now
            interm1_data_foldername = params['data_location']['interm1_data_foldername']
            interm2_data_foldername = params['data_location']['interm2_data_foldername']

            shutil.rmtree(os.path.join(
                main_data_foldername, interm1_data_foldername))
            shutil.rmtree(os.path.join(
                main_data_foldername, interm2_data_foldername))
            shutil.rmtree(os.path.join(main_data_foldername,
                          processed_stage1_data_foldername))
            logger.info('Interm data directories removed.')

        except Exception as e:
            logger.error(e)
            raise e


if __name__ == "__main__":

    process1 = PreprocessStage2()
    process1.preprocess2()
    logger.info('Data preprocessing completed successfully.')
