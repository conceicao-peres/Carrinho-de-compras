from fastapi import APIRouter, status, Response
from fastapi.responses import JSONResponse
from decoracao.modelos.modelos_endereco import Endereco
from decoracao.persistencia.endereco_persistencia import create_new_address, get_address_email, delete_address
from decoracao.persistencia.cliente_persistencia import check_user

address = APIRouter(
    prefix="",
    tags=["Address"]
)

@address.post(
    "/address/{email}",
    response_model=Endereco,
    status_code=status.HTTP_201_CREATED
)
async def new_address(endereco: Endereco, email: str, response: Response):
    req = {
        'email': email,
        'rua': endereco.rua,
        'numero': endereco.numero,
        'cep': endereco.cep,
        'cidade': endereco.cidade,
        'estado': endereco.estado
    }
    if check_user(req) is not None:
        create_new_address(req)
    else:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={'message': 'Email nao cadastrado.'})
    return req

@address.get(
    "/address/{email}",
    response_model=Endereco,
    status_code=status.HTTP_200_OK
)
async def get_address(email: str):
    if check_user({"email": email}) is not None:
        result = get_address_email(email)
        return result
    else:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={'message': 'Email nao cadastrado.'})
    return req

@address.delete(
    "/address/{email}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def remove_address(email):
    if check_user({"email": email}) is not None:
        delete_address(email)
    else:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={'message': 'Email nao cadastrado.'})
