from fastapi import APIRouter, status, Response
from decoracao.modelos.modelos_produtos import Product
from decoracao.persistencia.produto_persistencia import cadastrar_produto

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
        'nome_produto': produto.nome_produto,
        'descricao_produto': produto.descricao_produto,
        'qtde_produto': produto.qtde_produto,
        'preco_produto': produto.preco_produto,
        'qtde_estoque': produto.qtde_estoque,
        'material_produto': produto.material_produto,
    }
    # try:
    #     if valida_codigo_produto(req) is not None:
    #         response.status_code = status.HTTP_409_CONFLICT
    #     else:
    #         print("passei aqui 3")
    cadastrar_produto(req)
    # except connect_db.errosproduto.ConnectionFailure:
    #     print("Não pode se conectar ao servidor.")

    return req

