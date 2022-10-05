from unittest import result
from decoracao.persistencia.db_produtos import connect_db_produtos


def valida_codigo_produto(req):
    result = connect_db_produtos.produto.find_one({
        "codigo": req['codigo']
    })

    return result