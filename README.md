# Thyroid-Disease-Detection

![](https://img.shields.io/github/last-commit/shivamshinde123/Thyroid_Disease_Detection_Internship)
![](https://img.shields.io/github/languages/count/shivamshinde123/Thyroid_Disease_Detection_Internship)
![](https://img.shields.io/github/languages/top/shivamshinde123/Thyroid_Disease_Detection_Internship)
![](https://img.shields.io/github/repo-size/shivamshinde123/Thyroid_Disease_Detection_Internship)
![](https://img.shields.io/github/directory-file-count/shivamshinde123/Thyroid_Disease_Detection_Internship)
![](https://img.shields.io/github/license/shivamshinde123/Thyroid_Disease_Detection_Internship)

# Problem Statement:
Thyroid disease is a common cause of medical diagnosis and prediction, with an onset 
that is difficult to forecast in medical research. The thyroid gland is one of our body's 
most vital organs. Thyroid hormone releases are responsible for metabolic regulation. 
Hyperthyroidism and hypothyroidism are one of the two common diseases of the thyroid 
that releases thyroid hormones in regulating the rate of body's metabolism.  
The main goal is to predict the estimated risk on a patient's chance of obtaining thyroid 
disease or not.

# Project Demonstration

Check out the project demo at https://youtu.be/8IcTGZ6nDA0

# Deployed app link

Check out the deployed app at https://shivamshinde123-thyroid-disease-srcstep6-webapp-creation-b25273.streamlit.app/

# Project structure

```bash
*   .gitignore
*   LICENSE
*   params.yaml
*   README.md
*   requirements.txt
*
*               
****.streamlit
*       config.toml
*       
****Data
*   ****Processed_Data
*   *       X_train.csv
*   *       X_val.csv
*   *       y_train.csv
*   *       y_val.csv
*   *       
*   ****Raw_data
*           ThyroidRawData.csv
*           
****docs
*       Problem_Statement.pdf
*       
****Logs
*       data_processing.log
*       data_validation.log
*       make_dataset.log
*       model_creation.log
*       
****Metrics
*       classification_report.csv
*       metrics.json
*       
****mlruns
*   **** many_files_show_in_this_directory
*   
****Models
*       model.joblib
*       
****notebooks
*       EDA.ipynb
*       schema_in.json
*       
****Preprocess_pipeline
*       le_transforme.pkl
*       preprocess_pipeline.pkl
*       
****src
*   *   step0_utility_functions.py
*   *   step1_make_dataset.py
*   *   step2_training_Data_Validation.py
*   *   step3_data_preprocessing_stage1.py
*   *   step4_data_preprocessing_stage2.py
*   *   step5_model_training.py
*   *   step6_webapp_creation.py
*   *   test_data_preprocessing_stage1.py
*   *   test_data_preprocessing_stage2.py
*   *   test_make_dataset.py
*   *   test_model_training.py
*   *   __init__.py

```

# Data used

Get the data from https://archive-beta.ics.uci.edu/dataset/102/thyroid+disease  
Quinlan,Ross. (1987). Thyroid Disease. UCI Machine Learning Repository. https://doi.org/10.24432/C5D010.

# Project Flow

![image](https://user-images.githubusercontent.com/54674972/220857687-5701fd6c-c39e-4802-802b-d2c509fd1b15.png)


# Programming Languages Used
<img src = "https://img.shields.io/badge/-Python-3776AB?style=flat&logo=Python&logoColor=white">


# Python Libraries and tools Used
<img src="http://img.shields.io/badge/-Git-F05032?style=flat&logo=git&logoColor=FFFFFF"> <img src = "https://img.shields.io/badge/-NumPy-013243?style=flat&logo=NumPy&logoColor=white"> <img src = "https://img.shields.io/badge/-Pandas-150458?style=flat&logo=pandas&logoColor=white"> <img src = "https://img.shields.io/badge/-Matplotlib-FF6666?style=flat&logoColor=white"> <img src = "https://img.shields.io/badge/-Seaborn-5A20CB?style=flat&logoColor=white"> <img src="http://img.shields.io/badge/-sklearn-F7931E?style=flat&logo=scikit-learn&logoColor=FFFFFF">  <img src = "https://img.shields.io/badge/-Streamlit-FF4B4B?style=flat&logo=Streamlit&logoColor=white"> <img src = "https://img.shields.io/badge/-mlflow-0194E2?style=flat&logo=mlflow&logoColor=white">

## Run Locally

Clone the project

```bash
    git clone https://github.com/shivamshinde123/Thyroid_Disease_Detection_Internship.git
```

Go to the project directory (let's say Thyroid-disease-detection)

```bash
    cd Thyroid-disease-detection
```

Create a conda environment

```bash
    conda create -n environment_name python=3.10
```

Activate the created conda environment

```bash
    conda activate environment_name
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Load the data

```bash
  python src/step1_make_dataset.py
```
Validate the loaded data

```bash
  python src/step2_training_Data_Validation.py
```
Preprocess the validated data

```bash
  python src/step3_data_preprocessing_stage1.py
```
```bash
  python src/step4_data_preprocessing_stage2.py
```
Training a machine learning model using preprocessed data and also evluating metrics

```bash
  python src/step5_model_training.py
```
Testing the code for
 - Data Loading
 - Data Validation
 - Data Preprocessing
 - Model Training and Evaluation

```bash
  pytest src/
```

Make predictions using trained model

```bash
  streamlit run src/step6_webapp_creation.py
```

## 🚀 About Me
I'm an aspiring data scientist and a data analyst.


## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](http://shivamdshinde.com/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/shivamds92722/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://www.twitter.com/ShivamS64852411)
