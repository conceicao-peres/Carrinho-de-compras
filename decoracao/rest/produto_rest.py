from fastapi import APIRouter, status, Response
from typing import Union

from requests import ReadTimeout
from decoracao.persistencia.db import connect_db
from decoracao.persistencia.obter_colecoes import colecao_produto
from decoracao.modelos.modelos_produtos import Product
from decoracao.regras.produto_regras import valida_nome_produto, valida_id_produto

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
    colecao_produto.insert_one(req).inserted_id
    # except connect_db.errosproduto.ConnectionFailure:
    #     print("Não pode se conectar ao servidor.")

    return req




########################## REVISAR
@rota_produto.get(
    "/api/produto/",
    # response_model=Product,
    # Ajustado o código HTTP de retorno
    status_code=status.HTTP_200_OK
)
async def pesquisar_todos_produtos():
    print(colecao_produto.find())

########################## REVISAR


@rota_produto.get(
    "/api/busca/produto/{_id}",
    response_model=Product,
    status_code=status.HTTP_200_OK
)
async def pesquisar_pelo_id(_id: str):
    result = valida_id_produto(_id)
    return result




@rota_produto.get(
    "/api/busca/produto/{nome_produto}",
    response_model=Product,
    status_code=status.HTTP_200_OK
)
async def pesquisar_pelo_nome(nome_produto: str):
    result = valida_nome_produto(nome_produto)
    return result


@rota_produto.delete(
    "/api/remove/produto/{_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def remove_produto(_id: str):
    if valida_id_produto(_id) is not None:
        colecao_produto.delete_one({"_id": _id})