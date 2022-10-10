from decoracao.persistencia.obter_colecoes import colecao_endereco
import urllib.parse

def cadastrar_endereco(req): colecao_endereco.insert_one(req)


def busca_por_email(email: str):
    req = urllib.parse.unquote(email)
    result = colecao_endereco.find_one({"email": req})
    return result