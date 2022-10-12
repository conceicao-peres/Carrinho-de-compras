from decoracao.modelos.modelos_carrinho import OrderCarrinho
from decoracao.persistencia.db import connect_db
from decoracao.persistencia.cliente_persistencia import valida_email
from decoracao.persistencia.carrinho_persistencia import lista_carrinho_por_usuario
from fastapi import status
from bson.json_util import dumps
import json


def add_to_cart(id_usuario, id_produto, db_usuario, db_produto, db_carrinho):
    if id_usuario not in db_usuario:
        return False
    if id_produto not in db_produto:
        return False
    if id_usuario not in db_carrinho:
        db_carrinho[id_usuario] = OrderCarrinho()
        db_carrinho[id_usuario].id_produto.append(id_produto)
    return True


def get_cart(id_usuario, db_carrinho):
    if id_usuario in db_carrinho:
        return False
    return db_carrinho[id_usuario]


def get_total_price(id_usuario, db_carrinho):
    if id_usuario not in db_carrinho:
        return False
    return db_carrinho[id_usuario].total_price


def update_total_price(id_usuario, db_carrinho, db_produto):
    total = 0
    for item in db_carrinho[id_usuario].id_produto:
        total += db_produto[item].price
    return total


def get_total_quantity(id_usuario, db_carrinho):
    if id_usuario not in db_carrinho:
        return False
    return db_carrinho[id_usuario].total_quantity


def update_total_quantity(id_usuario, db_carrinho, db_produto):
    total_quantity = 0
    for item in db_carrinho[id_usuario].id_produto:
        total_quantity += db_produto[item].quantity
    return total_quantity
    
    
def delete_cart(id_usuario, db_carrinho):
    if id_usuario not in db_carrinho:
        return False
    del db_carrinho[id_usuario]
    return True

def pesquisa_carrinho_por_cliente(req, response):
    # valida se cliente existe
    _cliente = valida_email(req)
    if _cliente is None:
        response.status_code = status.HTTP_409_CONFLICT
    else:
        # lista produtos do carrinho
        doc_itens_carrinho = lista_carrinho_por_usuario(_cliente['email'])
        # converte cursor para json
        list_cursor = list(doc_itens_carrinho)
        list_data = dumps(list_cursor)
        res = json.loads(list_data)

        return res
