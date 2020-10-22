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
from xgboost.sklearn import XGBRegressor
from fastapi import APIRouter
from pydantic import BaseModel, Field, validator, confloat

log = logging.getLogger(__name__)
router = APIRouter()

filename = "app/api/mvp_model.joblib"

with open(filename, "rb") as f:
    joblib.load(f)


class Item(BaseModel):
    """Use this data model to parse the request body JSON."""

    Country: str = "United States, United Kingdom, Australia, Canada, Ireland \n"
    Property_Type: str = "Apartment, House, Condominium, Townhouse, Bed & Breakfast, Loft, Guesthouse, Bungalow, Villa, Cabin, Dorm, Camper/RV, Boat, Boutique hotel, Other"
    Room_Type: str = "Entire home/apt, Private room, Shared room"
    Accomodates: confloat(gt=1, lt=22) = "1-21"
    Bathrooms: confloat(gt=1, lt=11) = "1-10"
    Bedrooms: confloat(gt=1, lt=11) = "1-10"
    Beds: confloat(gt=0, lt=16) = "0-16"
    Cancellation_Policy: str = "strict, flexible, moderate, super_strict_60, super_strict_30, no_refunds, long_term"

    def to_df(self):
        """Convert pydantic object to pandas dataframe with 1 row."""
        return pd.DataFrame([dict(self)])

    # @validator('x1')
    # def x1_must_be_positive(cls, value):
    #     """Validate that x1 is a positive number."""
    #     assert value > 0, f'x1 == {value}, must be > 0'
    #     return value


@router.post("/predict")
async def predict(Price: Item):
    """
          Input Your Data Below 🔮!
    Country: Choose from: United States, United Kingdom, Australia, Canada, Ireland \n
    Property_Type: Choose from: Apartment, House, Condominium, Townhouse, Bed & Breakfast, Loft, Guesthouse, Bungalow, Villa, Cabin, Dorm, Camper/RV, Boat, Boutique hotel, Other\n
    Room_Type: Choose from: Entire home/apt, Private room, Shared room\n
    Accomodates: Enter INT between 1-21\n
    Bathrooms: Enter FLOAT between 1-10\n
    Bedrooms: Enter FLOAT between 1-10\n
    Beds: Enter FLOAT between 1-16\n
    Cancellation_Policy: Choose from: strict, flexible, moderate, super_strict_60, super_strict_30, no_refunds, long_term\n

          Response yields: Amount, per night (USD)

    """

    # input will be a dictionary, (item :Item)
    return "{}$ per night is an optimal AirBnB price.".format(
        random.randrange(50, 550, 10)
    )


# f.close()