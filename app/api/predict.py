import logging
import random
import pickle
import joblib
import numpy as np
import pandas as pd

from category_encoders import OneHotEncoder
from sklearn import pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from xgboost.sklearn import XGBClassifier
from fastapi import APIRouter
from pydantic import BaseModel, Field, validator

log = logging.getLogger(__name__)
router = APIRouter()

# classifier = load('api\mvp_model.joblib')

# filename = 'api\mvp_model.joblib'
# model = joblib.load(filename)

# loaded = pickle.load(open(filename, 'rb'))
# filepath = 'C:\Users\dabor\OneDrive\Desktop\mvp_model.pkl'
# pickle_in = open(r'')



filename = 'app/api/mvp_model.joblib'

with open(filename, 'rb') as f:
    joblib.load(f)

class Item(BaseModel):
    """Use this data model to parse the request body JSON."""


    Country: str = Field (...)
    Property_Type: str = Field(...)
    Room_Type: str = Field(...)
    Accomodates: float = Field (...)
    Bathrooms: float = Field (...)
    Bedrooms: float = Field (...)
    Beds: float = Field (...)
    Cancellation_Policy: str = Field (...)


    def to_df(self):
        """Convert pydantic object to pandas dataframe with 1 row."""
        return pd.DataFrame([dict(self)])

    # @validator('x1')
    # def x1_must_be_positive(cls, value):
    #     """Validate that x1 is a positive number."""
    #     assert value > 0, f'x1 == {value}, must be > 0'
    #     return value


@router.post('/predict')
async def predict(Price: Item):
    #(Price: float):
    """
    Making predictions for AirBnB rental prices using particular features🔮

    ### Request Body
  "Country": "string",
  "Property_Type": "string",
  "Room_Type": "string",
  "Accomodates": 0,
  "Bathrooms": 0,
  "Bedrooms": 1,
  "Beds": 0,
  "Cancellation_Policy": "string"

    ### Response
    - `prediction`: boolean, at random
    - `predict_proba`: float between 0.5 and 1.0, 
    representing the predicted class's probability

    Replace the placeholder docstring and fake predictions with your own model.
    """

    # input will be a dictionary, (item :Item)
    return '{}$ per night is an optimal AirBnB price.'.format(random.randrange(50, 550, 10))

# f.close()