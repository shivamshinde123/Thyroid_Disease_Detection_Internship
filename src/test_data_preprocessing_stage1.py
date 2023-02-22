import pandas as pd
import pytest
from src.step0_utility_functions import Utility
import os

@pytest.fixture
def params():
    return Utility().read_params()

def test_check_input_shape(params):

    """This python test is used to check the shape of input raw data."""

    main_data_folder = params['data_location']['main_data_folder']
    raw_data_folder = params['data_location']['raw_data_folder']
    raw_data_filename = params['data_location']['raw_data_filename']
    input_data = pd.read_csv(os.path.join(main_data_folder, raw_data_folder, raw_data_filename))

    assert input_data.shape == (9172, 31)


def test_check_output_shape(params):

    """This python test is used to check the shape of data after preprocessing performed."""

    main_data_folder = params['data_location']['main_data_folder']
    processed_stage2_data_foldername = params['data_location']['processed_stage2_data_foldername']
    processed_stage2_data_filename_X_train = params['data_location']['processed_stage2_data_filename_X_train']
    processed_stage2_data_filename_X_val = params['data_location']['processed_stage2_data_filename_X_val']
    processed_stage2_data_filename_y_train = params['data_location']['processed_stage2_data_filename_y_train']
    processed_stage2_data_filename_y_val = params['data_location']['processed_stage2_data_filename_y_val']
    X_train = pd.read_csv(os.path.join(main_data_folder,processed_stage2_data_foldername,processed_stage2_data_filename_X_train))
    X_val = pd.read_csv(os.path.join(main_data_folder,processed_stage2_data_foldername,processed_stage2_data_filename_X_val))
    y_train = pd.read_csv(os.path.join(main_data_folder,processed_stage2_data_foldername,processed_stage2_data_filename_y_train))
    y_val = pd.read_csv(os.path.join(main_data_folder,processed_stage2_data_foldername,processed_stage2_data_filename_y_val))

    assert X_train.shape == (8254, 23)
    assert X_val.shape == (918, 23)
    assert y_train.shape == (8254, 1)
    assert y_val.shape == (918, 1)