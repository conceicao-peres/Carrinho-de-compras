from decoracao.persistencia.obter_colecoes import colecao_produto
import urllib.parse


def valida_nome_produto(nome_produto: str):
    req = urllib.parse.unquote(nome_produto)
    result = colecao_produto.find_one({
        "nome_produto": req
    })

    return result