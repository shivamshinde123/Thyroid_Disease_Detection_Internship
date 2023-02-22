import logging
import os
from step0_utility_functions import Utility

import pandas as pd


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

Utility().create_folder('Logs')
params = Utility().read_params()

main_log_folderpath = params['logging_folder_paths']['main_log_foldername']
make_data_path = params['logging_folder_paths']['data_loading']

file_handler = logging.FileHandler(os.path.join(main_log_folderpath, make_data_path))
formatter = logging.Formatter(
    '%(asctime)s : %(levelname)s : %(filename)s : %(message)s')

file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


class MakeDataset:

    def __init__(self) -> None:
        pass

    def load_and_save(self, url, filename):
        """This method is used to load the data from google drive and to save the loaded data

        Parameters
        -----------

        url: URL of the data
        Returns
        --------
        None
        """

        try:
            # getting data url from params.yaml file
            inital_url = params['data_location']['data_url_base']

            url = inital_url + url.split('/')[-2]

            # Reading the csv file
            data = pd.read_csv(url)

            main_data_folder = params['data_location']['main_data_folder']
            raw_data_folder = params['data_location']['raw_data_folder']

            # Creating a Data folder to save the loaded data
            Utility().create_folder(main_data_folder)
            Utility().create_folder(os.path.join(main_data_folder, raw_data_folder))

            # Saving the loaded data to the Data folder
            data.to_csv(os.path.join(main_data_folder, raw_data_folder, str(
                filename)), index=False, sep=',')

        except Exception as e:
            logger.error(e)
            raise e


if __name__ == "__main__":

    data_url = params['data_location']['data_url']

    md = MakeDataset()
    logger.info('Loading of data started.')

    raw_data_filename = params['data_location']['raw_data_filename']
    md.load_and_save(data_url, raw_data_filename)
    logger.info(
        'Data loading completed and data saved to the directory Data/raw')
