from fastapi import APIRouter, status, Response

from decoracao.modelos.modelos_endereco import Endereco
from decoracao.persistencia.endereco_persistencia import cadastrar_endereco
from decoracao.persistencia.cliente_persistencia import valida_email

# Minha rota API de enderecos
rota_enderecos = APIRouter(
    # Prefixo para o caminho da rota
    prefix=""
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
        response.status_code = status.HTTP_409_CONFLICT
    else:
        cadastrar_endereco(req)
    return req

##Pesquisar Endereços

@rota_enderecos.get(
    "/endereco/{email_cliente}",
    response_model=Endereco,
    status_code=status.HTTP_200_OK
)
async def pesquisar_pelo_email(email: str):
    result = busca_por_email(email)
    return result


@rota_enderecos.delete(
    "/endereco/{email_cliente}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def remove_endereco(email):
    if valida_email({"email": email}) is not None:
        colecao_endereco.delete_one({"email": email})
