from decoracao.persistencia.obter_colecoes import colecao_endereco
from decoracao.persistencia.cliente_persistencia import busca_por_email

def cadastrar_endereco(req): colecao_endereco.insert_one(req)


def busca_por_email(email: str):
    req = urllib.parse.unquote(email)
    result = colecao_cliente.find_one({"email": req})
    return result