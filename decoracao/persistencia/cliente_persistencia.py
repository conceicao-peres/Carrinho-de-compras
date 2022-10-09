from decoracao.persistencia.obter_colecoes import colecao_cliente
import urllib.parse

def cadastrar_cliente(req):
    colecao_cliente.insert_one(req)

def valida_email(req):
    result = colecao_cliente.find_one({
        "email": req['email']
    })
    return result

def busca_por_email(email: str):
    req = urllib.parse.unquote(email)
    result = colecao_cliente.find_one({"email": req})
    return result