from decoracao.persistencia.obter_colecoes import colecao_produto
from bson import ObjectId
import urllib.parse
 

def cadastrar_produto(req):
    colecao_produto.insert_one(req)
 


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


def remover_produto(_id):
    colecao_produto.delete_one({"_id": ObjectId(_id)})


def atualizar_produto(_id, nome_produto):
    print('3')
    result = colecao_produto.update_one(
        {'_id': ObjectId(_id)},
        {'$set': {'nome_produto': nome_produto}}
        )
    print('4')

    return result
