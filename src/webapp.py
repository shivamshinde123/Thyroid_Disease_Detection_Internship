
import streamlit as st
import numpy as np
from step0_utility_functions import Utility
import os
import dill
import joblib
import pandas as pd


params = Utility().read_params()


class WebApp:

    def __init__(self) -> None:
        pass

    def webapp(self):
        """This method is used to create a webapp by which users will be able to make predictions

        Parameters
        -----------

        None

        Returns
        --------
        None
        """

        try:
            st.set_page_config(
                page_title="Thyroid Disease Detection App",
                page_icon=":butterfly",
                layout="wide",
                initial_sidebar_state="expanded",
            )
            # Adding the title to the page
            st.title('Thyroid Disease Detection')

            # Adding a author name to the project
            st.caption('A project by Shivam Shinde')

            # Making Predictions
            st.header('Make Prediction')

            # Creating an interfact to get inputs from the user
            col1, col2, col3 = st.columns(3, gap='large')

            age = col1.slider('age', min_value=1,
                                max_value=100, step=1, value=23)
            TSH = col1.slider('TSH', min_value=0.005,
                                max_value=530.0, step=0.01, value=100.0)
            T3 = col1.slider('T3', min_value=0.05,
                                max_value=18.0, step=0.01, value=12.0)
            TT4 = col1.slider('TT4', min_value=2.0,
                                max_value=60.0, step=0.01, value=30.0)
            T4U = col1.slider('T4U', min_value=0.17,
                                max_value=2.33, step=0.01, value=1.0)
            FTI = col1.slider('FTI', min_value=1.4,
                                max_value=881.0, step=0.01, value=300.0)

            I131_treatment = col2.selectbox(
                'I131_treatment', ['True', 'False'])
            lithium = col2.selectbox('lithium', ['True', 'False'])
            goitre = col2.selectbox('goitre', ['True', 'False'])
            tumor = col2.selectbox('tumor', ['True', 'False'])
            hypopituitary = col2.selectbox(
                'hypopituitary', ['True', 'False'])
            psych = col2.selectbox('psych', ['True', 'False'])

            sex = col3.selectbox('sex', ['Male', 'Female'])
            on_thyroxine = col3.selectbox(
                'on_thyroxine', ['True', 'False'])
            on_antithyroid_meds = col3.selectbox(
                'on_antithyroid_meds', ['True', 'False'])
            sick = col3.selectbox('sick', ['True', 'False'])
            if sex == 'Male':
                pregnant = col3.selectbox('pregnant', ['False'])
            else:
                pregnant = col3.selectbox('pregnant', ['True', 'False'])

            thyroid_surgery = col3.selectbox(
                'thyroid_surgery', ['True', 'False'])

            input = np.array([[age, sex, on_thyroxine, on_antithyroid_meds, sick,
                                pregnant, thyroid_surgery, I131_treatment,
                                lithium, goitre, tumor, hypopituitary, psych, TSH, T3, TT4, T4U, FTI
                                ]])

            input = pd.DataFrame(input, columns=['age', 'sex', 'on_thyroxine', 'on_antithyroid_meds', 'sick',
                                                    'pregnant', 'thyroid_surgery', 'I131_treatment',
                                                    'lithium', 'goitre', 'tumor', 'hypopituitary', 'psych', 'TSH', 'T3', 'TT4', 'T4U', 'FTI'
                                                    ])

            predict = st.button('Make a Prediction')

            # Actions after user clicks on 'Make a Prediction' button
            if predict:
                with st.spinner('Please wait'):
                    preprocess_pipe_foldername = params['preprocess']['preprocess_pipe_foldername']
                    preprocess_pipe_filename = params['preprocess']['preprocess_pipe_filename']
                    le_transformer_filename = params['preprocess']['le_transformer_filename']
                    model_foldername = params['model']['model_foldername']
                    model_name = params['model']['model_name']

                    # Loading saved preprocess pipeline
                    st.cache_data
                    def load_preprocess(preprocess_pipe_foldername, preprocess_pipe_filename, le_transformer_filename):
                        with open(os.path.join(preprocess_pipe_foldername, preprocess_pipe_filename), 'rb') as f:
                            preprocess_pipeline = dill.load(f)
                        with open(os.path.join(preprocess_pipe_foldername, le_transformer_filename), 'rb') as f:
                            le_transformer = dill.load(f)
                        return preprocess_pipeline, le_transformer

                    preprocess_pipeline, le_transformer = load_preprocess(
                        preprocess_pipe_foldername, preprocess_pipe_filename, le_transformer_filename)

                    # Loading the saved machine learning model
                    st.cache_data
                    def load_model(model_foldername, model_name):
                        model = joblib.load(os.path.join(
                            model_foldername, model_name))
                        return model

                    model = load_model(model_foldername, model_name)

                    # Preprocessing the input provided by the user
                    transformed_input = preprocess_pipeline.transform(input)

                    # Making predictions using the saved model and the preprocessed data
                    prediction = model.predict(transformed_input)
                    prediction = le_transformer.inverse_transform(prediction)

                    # making the predictions understandable for the user
                    thyroid_condition_dict = dict()
                    thyroid_condition_dict['A'] = 'Hyperthyroid'
                    thyroid_condition_dict['B'] = 'T3 Toxic'
                    thyroid_condition_dict['C'] = 'Toxic Goitre'
                    thyroid_condition_dict['D'] = 'Secondary Toxic'
                    thyroid_condition_dict['E'] = 'Hypothyroid'
                    thyroid_condition_dict['F'] = 'Primary Hypothyroid'
                    thyroid_condition_dict['G'] = 'Compensated Hypothyroid'
                    thyroid_condition_dict['H'] = 'Secondary Hypothyroid'
                    thyroid_condition_dict['I'] = 'Increased Binding Protein'
                    thyroid_condition_dict['J'] = 'Decreased Binding Protein'
                    thyroid_condition_dict['K'] = 'Concurrent non-thyroidal illness'
                    thyroid_condition_dict['L'] = 'Consistent with Replacement Therapy'
                    thyroid_condition_dict['M'] = 'Underreplaced'
                    thyroid_condition_dict['N'] = 'Overreplaced'
                    thyroid_condition_dict['O'] = 'Antithyroid Drugs'
                    thyroid_condition_dict['P'] = 'I131 Treatment'
                    thyroid_condition_dict['Q'] = 'Surgery'
                    thyroid_condition_dict['R'] = 'Discordant Assay Results'
                    thyroid_condition_dict['S'] = 'Elevated TBG'
                    thyroid_condition_dict['T'] = 'Elevated Thyroid Hormones'
                    thyroid_condition_dict['Negative'] = 'Patient is most likely not suffering from Thyroid Disease.'

                    prediction = thyroid_condition_dict[prediction[0]]

                    # Showing the prediction made to the user
                    st.subheader(
                        f"Patient's predicted condition:   {prediction}")

        except Exception as e:
            raise e


if __name__ == "__main__":
    wa = WebApp()
    wa.webapp()
