from decoracao.persistencia.obter_colecoes import colecao_produto
from bson import ObjectId
import urllib.parse
 
 
def busca_por_id(_id: str):
    req = urllib.parse.unquote(_id)
    result = colecao_produto.find_one({
        "_id": ObjectId(req)
    })
 
    return result
 
 
def valida_nome_produto(nome_produto: str):
    req = urllib.parse.unquote(nome_produto)
    result = colecao_produto.find_one({
        "nome_produto": req
    })
 
    return result