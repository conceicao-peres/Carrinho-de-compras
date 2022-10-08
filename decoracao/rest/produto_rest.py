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

    req = {
        'nome': produto.nome_produto,
        'descricao': produto.descricao_produto,
        'quantidade produto': produto.qtde_produto,
        'preço': produto.preco_produto,
        'estoque': produto.qtde_estoque,
        'material': produto.material_produto
    }
    try:
        if valida_codigo_produto(req) is not None:
            response.status_code = status.HTTP_409_CONFLICT
        else:
            connect_db.produto.insert_one(req).inserted_id
    except connect_db.errosproducts.ConnectionFailure:
            print("Não pode se conectar ao servidor.")

    return req
