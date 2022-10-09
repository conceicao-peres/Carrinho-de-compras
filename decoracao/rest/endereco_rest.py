import email
from fastapi import APIRouter, status, Response

from decoracao.modelos.modelos_endereco import Endereco
from decoracao.persistencia.endereco_persistencia import cadastrar_endereco

# Minha rota API de enderecos
rota_enderecos = APIRouter(
    # Prefixo para o caminho da rota
    prefix=""
)


@rota_enderecos.post(
    "/endereco/{email_cliente}", 
    response_model=Endereco,
    status_code=status.HTTP_200_OK
)
async def criar_endereco(endereco: Endereco, email_cliente: str, response: Response):
    req = {
        'rua': endereco.rua,
        'numero': endereco.numero,
        'cep': endereco.cep,
        'cidade': endereco.cidade,
        'estado': endereco.estado
    }

    response = cadastrar_endereco(req, email_cliente)

    return response
