from pydantic import BaseModel, Field
from typing import List

class Client(BaseModel):
    Age: int = Field(ge=18, le=100)
    Days_Since_Last_Login: int = Field(ge=0)
    Customer_Service_Calls: int = Field(ge=0)
    Monthly_Spend: float = Field(ge=0)


class ModelResponse(BaseModel):
    prediction: int
    probability: float
    shap_values: List[float]
