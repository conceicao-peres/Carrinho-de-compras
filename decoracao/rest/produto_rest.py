from fastapi import APIRouter, status, Response
from decoracao.persistencia.db import connect_db
from decoracao.modelos.modelos_produtos import Product
from decoracao.regras.produto_regras import valida_codigo_produto

# Minha rota API de produto
rota_produto = APIRouter(
    # Prefixo para o caminho da rota
    prefix=""
)


@rota_produto.post(
    "/api/produto/",
    response_model=Product,
    # Ajustado o código HTTP de retorno
    status_code=status.HTTP_201_CREATED
)
async def criar_novo_produto(produto: Product, response: Response):
    print("passsei por aqui 1")
    req = {
        'nome_produto': produto.nome_produto,
        'descricao_produto': produto.descricao_produto,
        'qtde_produto': produto.qtde_produto,
        'preco_produto': produto.preco_produto,
        'qtde_estoque': produto.qtde_estoque,
        'material_produto': produto.material_produto
    }
    print("passsei por aqui 2")
    try:
        if valida_codigo_produto(req) is not None:
            response.status_code = status.HTTP_409_CONFLICT
        else:
            print("passei aqui 3")
            connect_db().produto.insert_one(req)
    except connect_db.errosproduto.ConnectionFailure:
        print("Não pode se conectar ao servidor.")

    return req
