from decoracao.persistencia.db import connect_db

def obter_colecao(nome_colecao: str):
    bd = connect_db()
    colecao = bd[nome_colecao]

    return colecao

colecao_cliente = obter_colecao('cliente')
colecao_endereco = obter_colecao('endereco')
colecao_produto = obter_colecao('produto')
colecao_carrinho = obter_colecao('carrinho')

