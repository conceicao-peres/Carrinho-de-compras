from fastapi import APIRouter, status, Response
from fastapi.responses import JSONResponse
from decoracao.modelos.modelos_endereco import Endereco
from decoracao.persistencia.endereco_persistencia import cadastrar_endereco, busca_por_email, remover_endereco
from decoracao.persistencia.cliente_persistencia import valida_email

rota_enderecos = APIRouter(
    prefix="",
    tags=["Address"]
)

@rota_enderecos.post(
    "/endereco/{email_cliente}",
    response_model=Endereco,
    status_code=status.HTTP_201_CREATED
)
async def criar_endereco(endereco: Endereco, email_cliente: str, response: Response):
    req = {
        'email': email_cliente,
        'rua': endereco.rua,
        'numero': endereco.numero,
        'cep': endereco.cep,
        'cidade': endereco.cidade,
        'estado': endereco.estado
    }
    if valida_email(req) is not None:
        cadastrar_endereco(req)
    else:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={'message': 'Email nao cadastrado.'})
    return req

@rota_enderecos.get(
    "/endereco/{email}",
    response_model=Endereco,
    status_code=status.HTTP_200_OK
)
async def pesquisar_pelo_email(email: str):
    if valida_email({"email": email}) is not None:
        result = busca_por_email(email)
        return result
    else:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={'message': 'Email nao cadastrado.'})
    return req

@rota_enderecos.delete(
    "/endereco/{email}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def remove_endereco(email):
    if valida_email({"email": email}) is not None:
        remover_endereco(email)
    else:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={'message': 'Email nao cadastrado.'})
