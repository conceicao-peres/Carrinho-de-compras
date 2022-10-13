from decoracao.persistencia.obter_colecoes import colecao_carrinho

def cadastrar_carrinho(req):
    colecao_carrinho.insert_one(req)

def valida_email_carrinho(req):
    result = colecao_carrinho.find_one({
        "email": req['email']
    })
    return result

def add_item_carrinho(req):
    colecao_carrinho.insert_many(req)