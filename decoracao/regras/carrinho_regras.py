from decoracao.persistencia.produto_persistencia import valida_nome_produto



def cria_lista_produtos(item):
    lista_produto = []
    produto = valida_nome_produto(item)
    lista_produto.append(produto)
    return lista_produto