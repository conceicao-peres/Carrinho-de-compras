from decoracao.persistencia.obter_colecoes import colecao_carrinho

def add_cart(req):
    colecao_carrinho.insert_one(req)

def check_email_cart(req):
    result = colecao_carrinho.find_one({
        "email": req['email']
    })
    return result

def add_item_carrinho(req):
    colecao_carrinho.insert_many(req)