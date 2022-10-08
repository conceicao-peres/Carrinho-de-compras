from decoracao.persistencia.db import connect_db


def valida_codigo_produto(req):
    result = connect_db.produto.find_one({
        "codigo": req['_id']
    })

    return result