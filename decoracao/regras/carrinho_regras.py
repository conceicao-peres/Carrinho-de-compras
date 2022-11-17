from decoracao.persistencia.produto_persistencia import check_product_name

def product_list(item):
    lista_produto = []
    produto = check_product_name(item)
    lista_produto.append(produto)
    return lista_produto