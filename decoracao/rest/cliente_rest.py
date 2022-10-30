from fastapi import APIRouter, status, Response
from fastapi.responses import JSONResponse
from decoracao.modelos.modelos_cliente import Item
from decoracao.regras.cliente_regras import create_new_user
from decoracao.persistencia.cliente_persistencia import (
    check_user, get_user_email, remove_user_email)

import datetime

user = APIRouter(prefix="", tags=["User"])

@user.post(
    "/api/user",
    description=""" Para cadastrar um novo usuario:
- nome: dever ter ao menos 3 caracteres 
- e-mail: deve ser unico (nao pode haver outro usuario com o mesmo email); deve ser valido (conter @)""",
    response_model=Item,
    status_code=status.HTTP_201_CREATED
)
async def new_user(item: Item, response: Response):
    req = {
        'nome': item.nome,
        'email': item.email,
        'criacao': datetime.datetime.utcnow()
    }
    create_new_user(req, response)
    return req

@user.get(
    "/api/user/{email}",
    response_model=Item,
    status_code=status.HTTP_200_OK
)
async def get_user(email: str):
    if get_user_email(email) is None:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={'message': email+ ' not found.'})
    result = get_user_email(email)
    return result

@user.delete(
    "/api/user/{email}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def remove_user(email):
    if get_user_email(email) is None:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={'message': email+ ' not found.'})
    if get_user_email(email) is not None:
        remove_user_email(email)
