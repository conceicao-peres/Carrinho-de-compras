from fastapi import APIRouter, status, Response

from decoracao.persistencia.db import connect_db
from decoracao.persistencia.obter_colecoes import colecao_cliente
from decoracao.modelos.modelos_cliente import Item, ItemEmail
from decoracao.persistencia.cliente_persistencia import valida_email, busca_por_email, cadastrar_cliente

import urllib.parse
import datetime

# Minha rota API de cliente
rota_cliente = APIRouter(
    # Prefixo para o caminho da rota
    prefix=""
)

# Cria novo cliente
@rota_cliente.post(
    "/api/cliente",
    response_model=Item,
    # Ajustado o código HTTP de retorno
    status_code=status.HTTP_201_CREATED
)
async def criar_novo_cliente(item: Item, response: Response):
    req = {
        'nome': item.nome,
        'email': item.email,
        'criacao': datetime.datetime.utcnow()
    }

    if valida_email(req) is not None:
        response.status_code = status.HTTP_409_CONFLICT
    else:
        cadastrar_cliente(req)
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
        colecao_cliente.delete_one({"email": email})