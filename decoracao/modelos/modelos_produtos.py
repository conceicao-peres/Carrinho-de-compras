from lib2to3.pytree import Base
from pydantic import BaseModel, confloat, conint
from typing import Optional


class Product(BaseModel):
    nome_produto: str
    descricao_produto: str
    qtde_produto: int
    preco_produto: confloat(gt=0.01)
    qtde_estoque: conint(gt=0)
    material_produto: str
    codigo_produto: int