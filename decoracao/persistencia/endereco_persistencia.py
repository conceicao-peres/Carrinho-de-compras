from decoracao.persistencia.obter_colecoes import colecao_endereco
from decoracao.persistencia.cliente_persistencia import busca_por_email

def cadastrar_endereco(req, email_cliente):
    dados_cliente = busca_por_email(email_cliente)
    endereco_cliente = {
        "email_cliente": email_cliente,
        "endereco": req
    }

    result = colecao_endereco.insert_one(endereco_cliente)
    return result