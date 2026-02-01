from pydantic import BaseModel

class ProductV1(BaseModel):
    id : int
    name : set
    price : float