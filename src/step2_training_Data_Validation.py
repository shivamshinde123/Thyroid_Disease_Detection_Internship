
from pydantic import BaseModel, conint, ValidationError, Field
from typing import List, Optional
from step0_utility_functions import Utility
import pandas as pd
import logging
import os


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

Utility().create_folder('Logs')
params = Utility().read_params()

main_log_folderpath = params['logging_folder_paths']['main_log_foldername']
data_validation_path = params['logging_folder_paths']['data_validation']

file_handler = logging.FileHandler(os.path.join(
    main_log_folderpath, data_validation_path))
formatter = logging.Formatter(
    '%(asctime)s : %(levelname)s : %(filename)s : %(message)s')

file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


class Dictvalidator(BaseModel):

    age: conint(gt=0, le=100)
    sex: str
    on_thyroxine: str
    query_on_thyroxine: str
    on_antithyroid_meds: str
    sick: str
    pregnant: str
    thyroid_surgery: str
    I131_treatment: str
    query_hypothyroid: str
    query_hyperthyroid: str
    lithium: str
    goitre: str
    tumor: str
    hypopituitary: str
    psych: str
    TSH_measured: str
    TSH: Optional[float]
    T3_measured: str
    T3: Optional[float]
    TT4_measured: str
    TT4: Optional[float]
    T4U_measured: str
    T4U: Optional[float]
    FTI_measured: str
    FTI: Optional[float]
    TBG_measured: str
    TBG: Optional[float]
    referral_source: str
    target: str
    patient_id: Optional[int]


class dataframe_validator(BaseModel):

    df_dict: List[Dictvalidator]


if __name__ == '__main__':

    main_data_folder = params['data_location']['main_data_folder']
    raw_data_folder = params['data_location']['raw_data_folder']
    raw_data_filename = params['data_location']['raw_data_filename']

    raw_data_file_path = os.path.join(
        main_data_folder, raw_data_folder, raw_data_filename)

    df = pd.read_csv(raw_data_file_path)

    try:
        logger.info('Input raw data validation started.')
        dataframe_validator(df_dict=df.to_dict(orient='records'))
        logger.info('Input raw data validation successfully completed.')
    except ValidationError as e:
        logger.warning(e)
