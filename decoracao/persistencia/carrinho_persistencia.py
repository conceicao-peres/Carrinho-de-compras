from decoracao.persistencia.obter_colecoes import colecao_carrinho
import urllib.parse

def lista_carrinho_por_usuario(email: str):
    req = urllib.parse.unquote(email)
    result = colecao_carrinho.find({"email": req})

    return result


def remover_carrinho(email):
    try:
        result = colecao_carrinho.delete_one({"email": email})
        return result
    except Exception:
        print (Exception)
