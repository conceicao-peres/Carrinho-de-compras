from fastapi import APIRouter, status, Response
from fastapi.responses import JSONResponse
from decoracao.modelos.modelos_cliente import Item
from decoracao.regras.cliente_regras import cadastrar_novo_cliente
from decoracao.persistencia.cliente_persistencia import (
    valida_email, busca_por_email, remover_cliente)

import datetime

rota_cliente = APIRouter(prefix="",
                        tags=["User"])

@rota_cliente.post(
    "/api/cliente",
    description=""" Para cadastrar um novo usuario:
- nome: dever ter ao menos 3 caracteres 
- e-mail: deve ser unico (nao pode haver outro usuario com o mesmo email); deve ser valido (conter @)""",
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
    if busca_por_email(email) is None:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={'message': email+ ' not found.'})
    result = busca_por_email(email)
    return result

@rota_cliente.delete(
    "/api/remove/cliente/{email}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def remove_cliente(email):
    if busca_por_email(email) is None:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={'message': email+ ' not found.'})
    if busca_por_email(email) is not None:
        remover_cliente(email)
