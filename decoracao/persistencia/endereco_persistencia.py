from decoracao.persistencia.obter_colecoes import colecao_endereco
import urllib.parse

def create_new_address(req):
    colecao_endereco.insert_one(req)

def get_address_email(email: str):
    req = urllib.parse.unquote(email)
    result = colecao_endereco.find_one({"email": req})
    return result

def delete_address(email):
    colecao_endereco.delete_one({"email": email})