from decoracao.persistencia.produto_persistencia import check_product_name

def cria_lista_produtos(item):
    lista_produto = []
    produto = valida_nome_produto(item)
    lista_produto.append(produto)
    return lista_produto