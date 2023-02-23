
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
            # Adding the title to the page
            st.title('Thyroid Disease Detection')

            # Adding a author name to the project
            st.caption('A project by Shivam Shinde')

            # Adding the metadata to the page
            st.header('Metadata')

            # Metadata 1: Feature Information
            with st.expander('Expand to see the feature information'):
                st.markdown("""**Feature information:**  
                            1. age - age of the patient (int)  
                            2. sex - sex patient identifies (str)  
                            3. on_thyroxine - whether patient is on thyroxine (bool)  
                            4. query on thyroxine - whether patient is on thyroxine (bool)  
                            5. on antithyroid meds - whether patient is on antithyroid meds (bool)  
                            6. sick - whether patient is sick (bool)  
                            7. pregnant - whether patient is pregnant (bool)  
                            8. thyroid_surgery - whether patient has undergone thyroid surgery (bool)  
                            9. I131_treatment - whether patient is undergoing I131 treatment (bool)  
                            10. query_hypothyroid - whether patient believes they have hypothyroid (bool)  
                            11. query_hyperthyroid - whether patient believes they have hyperthyroid (bool)  
                            12. lithium - whether patient * lithium (bool)  
                            13. goitre - whether patient has goitre (bool)  
                            14. tumor - whether patient has tumor (bool)  
                            15. hypopituitary - whether patient * hyperpituitary gland (float)  
                            16. psych - whether patient * psych (bool)  
                            17. TSH - TSH level in blood from lab work (float)  
                            18. T3 - T3 level in blood from lab work (float)  
                            19. TT4 - TT4 level in blood from lab work (float)  
                            20. T4U - T4U level in blood from lab work (float)  
                            21. FTI - FTI level in blood from lab work (float)  
                            22. TBG - TBG level in blood from lab work (float)  
                            23. referral_source - (str)  
                            2. target - hyperthyroidism medical diagnosis (str)""")

            # Metadata 2: Target Column Values Information
            with st.expander('Expand to see the prediction information'):
                st.markdown("""**Target metadata**  
                    The diagnosis consists of a string of letters indicating diagnosed conditions.
                    A diagnosis "Other" indicates no condition requiring comment.  A diagnosis of the
                    form "X|Y" is interpreted as "consistent with X, but more likely Y".  The
                    conditions are divided into groups where each group corresponds to a class of
                    comments.

                    Letter  Diagnosis
                    ------  ---------

                    hyperthyroid conditions:

                    A   hyperthyroid
                    B   T3 toxic
                    C   toxic goitre
                    D   secondary toxic

                    hypothyroid conditions:

                    E   hypothyroid
                    F   primary hypothyroid
                    G   compensated hypothyroid
                    H   secondary hypothyroid

                    binding protein:

                    I   increased binding protein
                    J   decreased binding protein

                    general health:

                    K   concurrent non-thyroidal illness

                    replacement therapy:

                    L   consistent with replacement therapy
                    M   underreplaced
                    N   overreplaced

                    antithyroid treatment:

                    O   antithyroid drugs
                    P   I131 treatment
                    Q   surgery

                    miscellaneous:

                    R   discordant assay results
                    S   elevated TBG
                    T   elevated thyroid hormones""")

            # Making Predictions
            st.header('Make Prediction')

            # Creating an interfact to get inputs from the user
            with st.expander('Expand to enter the feature values'):
                col1, col2, col3 = st.columns(3)

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
                TBG = col1.slider('TBG', min_value=0.1,
                                  max_value=200.0, step=0.01, value=100.0)

                I131_treatment = col2.selectbox(
                    'I131_treatment', ['True', 'False'])
                query_hypothyroid = col2.selectbox(
                    'query_hypothyroid', ['True', 'False'])
                query_hyperthyroid = col2.selectbox(
                    'query_hyperthyroid', ['True', 'False'])
                lithium = col2.selectbox('lithium', ['True', 'False'])
                goitre = col2.selectbox('goitre', ['True', 'False'])
                tumor = col2.selectbox('tumor', ['True', 'False'])
                hypopituitary = col2.selectbox(
                    'hypopituitary', ['True', 'False'])
                psych = col2.selectbox('psych', ['True', 'False'])

                sex = col3.selectbox('sex', ['Male', 'Female'])
                on_thyroxine = col3.selectbox(
                    'on_thyroxine', ['True', 'False'])
                query_on_thyroxine = col3.selectbox(
                    'query_on_thyroxine', ['True', 'False'])
                on_antithyroid_meds = col3.selectbox(
                    'on_antithyroid_meds', ['True', 'False'])
                sick = col3.selectbox('sick', ['True', 'False'])
                if sex == 'Male':
                    pregnant = col3.selectbox('pregnant', ['False'])
                else:
                    pregnant = col3.selectbox('pregnant', ['True', 'False'])

                thyroid_surgery = col3.selectbox(
                    'thyroid_surgery', ['True', 'False'])
                referral_source = col3.selectbox(
                    'referral_source', ['SVI', 'SVHC', 'STMW', 'SVHD', 'WEST', 'other'])

                input = np.array([[age, sex, on_thyroxine, query_on_thyroxine, on_antithyroid_meds, sick,
                                   pregnant, thyroid_surgery, I131_treatment, query_hypothyroid, query_hyperthyroid,
                                   lithium, goitre, tumor, hypopituitary, psych, TSH, T3, TT4, T4U, FTI,
                                   TBG, referral_source]])

                input = pd.DataFrame(input, columns=['age', 'sex', 'on_thyroxine', 'query_on_thyroxine', 'on_antithyroid_meds', 'sick',
                                                     'pregnant', 'thyroid_surgery', 'I131_treatment', 'query_hypothyroid', 'query_hyperthyroid',
                                                     'lithium', 'goitre', 'tumor', 'hypopituitary', 'psych', 'TSH', 'T3', 'TT4', 'T4U', 'FTI',
                                                     'TBG', 'referral_source'])

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
                    thyroid_condition_dict['A'] = 'hyperthyroid'
                    thyroid_condition_dict['B'] = 'T3 toxic'
                    thyroid_condition_dict['C'] = 'toxic goitre'
                    thyroid_condition_dict['D'] = 'secondary toxic'
                    thyroid_condition_dict['E'] = 'hypothyroid'
                    thyroid_condition_dict['F'] = 'primary hypothyroid'
                    thyroid_condition_dict['G'] = 'compensated hypothyroid'
                    thyroid_condition_dict['H'] = 'secondary hypothyroid'
                    thyroid_condition_dict['I'] = 'increased binding protein'
                    thyroid_condition_dict['J'] = 'decreased binding protein'
                    thyroid_condition_dict['K'] = 'concurrent non-thyroidal illness'
                    thyroid_condition_dict['L'] = 'consistent with replacement therapy'
                    thyroid_condition_dict['M'] = 'underreplaced'
                    thyroid_condition_dict['N'] = 'overreplaced'
                    thyroid_condition_dict['O'] = 'antithyroid drugs'
                    thyroid_condition_dict['P'] = 'I131 treatment'
                    thyroid_condition_dict['Q'] = 'surgery'
                    thyroid_condition_dict['R'] = 'discordant assay results'
                    thyroid_condition_dict['S'] = 'elevated TBG'
                    thyroid_condition_dict['T'] = 'elevated thyroid hormones'
                    thyroid_condition_dict['Others'] = 'no condition requiring comment'

                    prediction = thyroid_condition_dict[prediction[0]]

                    # Showing the prediction made to the user
                    st.subheader(
                        f"Patient's predicted condition:   {prediction}")

        except Exception as e:
            raise e


if __name__ == "__main__":
    wa = WebApp()
    wa.webapp()
