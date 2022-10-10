from decoracao.persistencia.cliente_persistencia import valida_email, cadastrar_cliente
from fastapi import Response

def cadastrar_novo_cliente(req):
    if valida_email(req) is not None:
        response.status_code = status.HTTP_409_CONFLICT
    else:
        cadastrar_cliente(req)




