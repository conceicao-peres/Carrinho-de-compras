from decoracao.persistencia.obter_colecoes import colecao_produto


def cadastrar_produto(req):
    colecao_produto.insert_one(req).inserted_id


