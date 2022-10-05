from math import prod
from fastapi import APIRouter, status, Response
from requests import Response
from decoracao.modelos.modelos_produtos import Product
from decoracao.persistencia.db_produtos import connect_db_produtos
from decoracao.regras.produto_regras import valida_codigo_produto

# Minha rota API de produto
rota_produto = APIRouter(
    # Prefixo para o caminho da rota
    prefix="/api/produto"
)


@rota_produto.post(
    "/cadastroproduto/",
    response_model=Product
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
        'material': produto.material_produto,
        'codigo': produto.codigo_produto
    }
    try:
        if valida_codigo_produto(req) is not None:
            response.status_code = status.HTTP_409_CONFLICT
        else:
            connect_db_produtos.produto.insert_one(req).inserted_id
    except connect_db_produtos.errosproducts.ConnectionFailure:
            print("Não pode se conectar ao servidor.")

    return req
