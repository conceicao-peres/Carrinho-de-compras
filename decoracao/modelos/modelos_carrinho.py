from pydantic import BaseModel, Field
from typing import List

class Cart(BaseModel):
    email: str
    lista_produtos: List