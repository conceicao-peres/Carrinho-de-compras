from pydantic import BaseModel, Field
from typing import List

class Carrinho(BaseModel):
    email: str
    lista_produtos: List