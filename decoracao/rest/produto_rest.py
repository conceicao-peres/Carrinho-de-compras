from fastapi import APIRouter, status, Response
from decoracao.modelos.modelos_produtos import Product
from decoracao.persistencia.produto_persistencia import busca_por_id,valida_nome_produto

# Minha rota API de produto
rota_produto = APIRouter(
    # Prefixo para o caminho da rota
    prefix=""
)


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


