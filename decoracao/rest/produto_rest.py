from bson import ObjectId
from fastapi import APIRouter, status, Response
from decoracao.modelos.modelos_produtos import Product
from decoracao.persistencia.produto_persistencia import cadastrar_produto, busca_por_id,valida_nome_produto, remover_produto

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
        'material_produto': produto.material_produto
    }


    if valida_nome_produto(req['nome_produto']) is not None:
        response.status_code = status.HTTP_409_CONFLICT
    else:
        cadastrar_produto(req)
 


    return req

@rota_produto.get(
    "/api/busca/produto/{_id}",
    response_model=Product,
    status_code=status.HTTP_200_OK
)
async def pesquisar_pelo_id(_id: str):
    result = busca_por_id(_id)
    return result
 
 
 
 
@rota_produto.get(
    "/api/busca/produto/nome/{nome_produto}",
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
async def remove_produto_pelo_id(_id: str):
    result = busca_por_id(_id)
    if result is not None:
        remover_produto(_id)