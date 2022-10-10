from fastapi import APIRouter, status, Response

from decoracao.modelos.modelos_cliente import Item
from decoracao.regras.cliente_regras import cadastrar_novo_cliente
from decoracao.persistencia.cliente_persistencia import (
    valida_email, busca_por_email, remover_cliente)

import datetime

rota_cliente = APIRouter(prefix="")

@rota_cliente.post(
    "/api/cliente",
    response_model=Item,
    status_code=status.HTTP_201_CREATED
)
async def criar_novo_cliente(item: Item, response: Response):
    req = {
        'nome': item.nome,
        'email': item.email,
        'criacao': datetime.datetime.utcnow()
    }
    cadastrar_novo_cliente(req, response)

    return req

@rota_cliente.get(
    "/api/busca/cliente/{email}",
    response_model=Item,
    status_code=status.HTTP_200_OK
)
async def pesquisar_pelo_email(email: str):
    result = busca_por_email(email)
    return result

@rota_cliente.delete(
    "/api/remove/cliente/{email}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def remove_cliente(email):
    if valida_email({"email": email}) is not None:
        remover_cliente(email)
