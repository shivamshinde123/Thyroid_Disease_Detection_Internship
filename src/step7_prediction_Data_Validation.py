
from typing import Optional
from pydantic import BaseModel, confloat, validator, conint


class inp_dict_validator(BaseModel):

    # validating the datatypes of the input features
    age: Optional[conint(gt=0, le=100)]
    sex: Optional[str]
    on_thyroxine: Optional[str]
    query_on_thyroxine: Optional[str]
    on_antithyroid_meds: Optional[str]
    sick: Optional[str]
    pregnant: Optional[str]
    thyroid_surgery: Optional[str]
    I131_treatment: Optional[str]
    query_hypothyroid: Optional[str]
    query_hyperthyroid: Optional[str]
    lithium: Optional[str]
    goitre: Optional[str]
    tumor: Optional[str]
    hypopituitary: Optional[str]
    psych: Optional[str]
    TSH: Optional[confloat(ge=0.005, le=530.0)] 
    T3: Optional[confloat(ge=0.05,le=18.0)] 
    TT4: Optional[confloat(ge=2.0, le=600.0)] 
    T4U: Optional[confloat(ge=0.17, le=2.33)] 
    FTI: Optional[confloat(ge=1.4, le=881.0)] 
    TBG: Optional[confloat(ge=0.1, le=200.0)] 
    referral_source: Optional[str]


    # validating that the user is not entering the sex feature as 'Male' and the pregnant feature as 'True'
    @validator('pregnant')
    def pregnant_feature_validation(cls,field_value, values):
        sex = values['sex']
        if sex == 'M':
            if field_value == 't':
                raise ValueError('You cannot select Male feature as M as pregnant feature as True at the same time.')


    
