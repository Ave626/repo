from typing import TypeVar,Generic
from pydantic import BaseModel,ValidationError

T = TypeVar("V")

class DataContainer(BaseModel,Generic[T]):
    data : T