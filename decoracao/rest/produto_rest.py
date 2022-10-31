from bson import ObjectId
from fastapi import APIRouter, status, Response
from decoracao.modelos.modelos_produtos import Product
from decoracao.persistencia.produto_persistencia import add_product, get_product_id,check_product_name, remove_product_id

product = APIRouter(
    prefix="",
    tags=["Product"]
)

@product.post(
    "/product/",
    response_model=Product,
    status_code=status.HTTP_201_CREATED
)
async def new_product(produto: Product, response: Response):
    req = {
        'nome_produto': produto.nome_produto,
        'descricao_produto': produto.descricao_produto,
        'qtde_produto': produto.qtde_produto,
        'preco_produto': produto.preco_produto,
        'qtde_estoque': produto.qtde_estoque,
        'material_produto': produto.material_produto
    }
    if check_product_name(req['nome_produto']) is not None:
        response.status_code = status.HTTP_409_CONFLICT
    else:
        add_product(req)
    return req

@product.get(
    "/product_id/{_id}",
    response_model=Product,
    status_code=status.HTTP_200_OK
)
async def get_id(_id: str):
    result = get_product_id(_id)
    return result

@product.get(
    "/product_name/{product_name}",
    response_model=Product,
    status_code=status.HTTP_200_OK
)
async def get_name(product_name: str):
    result = check_product_name(product_name)
    return result

@product.delete(
    "/product/{_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def remove_id(_id: str):
    result = get_product_id(_id)
    if result is not None:
        remove_product_id(_id)
