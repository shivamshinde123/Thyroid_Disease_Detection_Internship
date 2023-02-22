
from step0_utility_functions import Utility
import pandas as pd
import numpy as np
import logging
import os

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


class PreprocessStage1:

    def __init__(self) -> None:
        pass

    def remove_unneccessary_columns(self, lst_of_useless_cols):
        """This method is used to remove the column which doesn't contribute to the model training

        Args: List of unneccessary columns 

        Returns: None
        """

        try:
            main_data_foldername = params['data_location']['main_data_folder']
            raw_data_foldername = params['data_location']['raw_data_folder']
            raw_data_filename = params['data_location']['raw_data_filename']
            interm1_data_foldername = params['data_location']['interm1_data_foldername']
            interm1_data_filename = params['data_location']['interm1_data_filename']

            df = pd.read_csv(os.path.join(main_data_foldername,
                                          raw_data_foldername, raw_data_filename))

            for feature in lst_of_useless_cols:
                df.drop(feature, axis=1, inplace=True)

            # Creating a Data folder to save the processed data
            Utility().create_folder(main_data_foldername)
            Utility().create_folder(os.path.join(main_data_foldername, interm1_data_foldername))

            df.to_csv(os.path.join(main_data_foldername, interm1_data_foldername,
                                   interm1_data_filename), index=False, sep=',')

            logger.info('Removed unnecessary columns from the data.')

        except Exception as e:
            logger.error(e)
            raise e

    def converting_illogical_ages_to_null(self):
        """This method is used to convert the illogical ages from the data to the null values. This is to be done in order to reduce the false information in the dataset

        Args: None

        Returns: None
        """
        try:
            main_data_foldername = params['data_location']['main_data_folder']
            interm1_data_foldername = params['data_location']['interm1_data_foldername']
            interm1_data_filename = params['data_location']['interm1_data_filename']
            interm2_data_foldername = params['data_location']['interm2_data_foldername']
            interm2_data_filename = params['data_location']['interm2_data_filename']

            df = pd.read_csv(os.path.join(main_data_foldername,
                                          interm1_data_foldername, interm1_data_filename))

            df['age'] = np.where(df['age'] > 100, np.nan, df['age'])
            df['age'] = np.where(df['age'] <= 0, np.nan, df['age'])

            # Creating a Data folder to save the processed data
            Utility().create_folder(main_data_foldername)
            Utility().create_folder(os.path.join(main_data_foldername, interm2_data_foldername))

            df.to_csv(os.path.join(main_data_foldername, interm2_data_foldername,
                                   interm2_data_filename), index=False, sep=',')

            logger.info(
                'Removed values of the column age that does not make sense.')

        except Exception as e:
            logger.error(e)
            raise e

    def replacing_dash_with_others_in_target_column(self):
        """This method is used to replace the '-' value present in the target column with 'Others'

        Args: None

        Returns: None
        """

        try:
            main_data_foldername = params['data_location']['main_data_folder']
            interm2_data_foldername = params['data_location']['interm2_data_foldername']
            interm2_data_filename = params['data_location']['interm2_data_filename']
            processed_stage1_data_foldername = params['data_location']['processed_stage1_data_foldername']
            processed_stage1_data_filename = params['data_location']['processed_stage1_data_filename']

            df = pd.read_csv(os.path.join(main_data_foldername,
                                          interm2_data_foldername, interm2_data_filename))

            df['target'] = np.where(
                df['target'] == '-', 'Others', df['target'])

            # Creating a Data folder to save the processed data
            Utility().create_folder(main_data_foldername)
            Utility().create_folder(os.path.join(main_data_foldername, processed_stage1_data_foldername))

            df.to_csv(os.path.join(main_data_foldername, processed_stage1_data_foldername,
                                   processed_stage1_data_filename), index=False, sep=',')

            logger.info('Replaced dash with others in target column.')

        except Exception as e:
            logger.error(e)
            raise e


if __name__ == '__main__':

    lst = params['General']['list_of_columns_to_remove']

    process1 = PreprocessStage1()

    logger.info('Data preprocessing started.')
    process1.remove_unneccessary_columns(lst)
    process1.converting_illogical_ages_to_null()
    process1.replacing_dash_with_others_in_target_column()
