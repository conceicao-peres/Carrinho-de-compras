from decoracao.persistencia.obter_colecoes import colecao_cliente
import urllib.parse

def check_user(req):
    result = colecao_cliente.find_one({
        "email": req['email']
    })
    return result

def add_user(req):
    colecao_cliente.insert_one(req)

def get_user_email(email: str):
    req = urllib.parse.unquote(email)
    result = colecao_cliente.find_one({"email": req})
    return result

def remove_user_email(email):
    colecao_cliente.delete_one({"email": email})
