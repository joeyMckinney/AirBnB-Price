import logging
import random

from fastapi import APIRouter
import pandas as pd
from pydantic import BaseModel, Field, validator

log = logging.getLogger(__name__)
router = APIRouter()


class Item(BaseModel):
    """Use this data model to parse the request body JSON."""

    Description: str 
    City: str 
    Country: str 
    Property_Type: str 
    Room_Type: str
    Accomodates: float
    Bathrooms: float
    Bedrooms: float
    Beds: float
    Amenities: str 
    Price: float
    Cancellation_Policy: str


    def to_df(self):
        """Convert pydantic object to pandas dataframe with 1 row."""
        return pd.DataFrame([dict(self)])

    # @validator('x1')
    # def x1_must_be_positive(cls, value):
    #     """Validate that x1 is a positive number."""
    #     assert value > 0, f'x1 == {value}, must be > 0'
    #     return value


@router.post('/predict')
async def predict(item: Item):
    """
    Making predictions for AirBnB rental prices using particular features🔮

    ### Request Body
    - `x1`: positive float
    - `x2`: integer
    - `x3`: string

    ### Response
    - `prediction`: boolean, at random
    - `predict_proba`: float between 0.5 and 1.0, 
    representing the predicted class's probability

    Replace the placeholder docstring and fake predictions with your own model.
    """

    # input will be a dictionary, (item :Item)
    return '{}$ per night is an optimal AirBnB price.'.format(random.randrange(50, 550, 10))

