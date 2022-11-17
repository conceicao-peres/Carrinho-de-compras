from decoracao.persistencia.obter_colecoes import colecao_produto
from bson import ObjectId
import urllib.parse

def add_product(req):
    colecao_produto.insert_one(req)

def get_product_id(_id: str):
    req = urllib.parse.unquote(_id)
    result = colecao_produto.find_one({
        "_id": ObjectId(req)
    })
    return result

def check_product_name(nome_produto: str):
    req = urllib.parse.unquote(nome_produto)
    result = colecao_produto.find_one({
        "nome_produto": req
    })
    return result

def remove_product_id(_id):
    colecao_produto.delete_one({"_id": ObjectId(_id)})
