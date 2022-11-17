from fastapi import APIRouter, status, Response
from fastapi.responses import JSONResponse
from decoracao.modelos.modelos_carrinho import Cart
from decoracao.modelos.modelos_produtos import Product
from decoracao.regras.carrinho_regras import product_list
from decoracao.persistencia.cliente_persistencia import check_user
from decoracao.persistencia.carrinho_persistencia import delete_cart, add_cart, check_email_cart, add_item_carrinho
from decoracao.persistencia.produto_persistencia import check_product_name

cart = APIRouter(prefix="",
                          tags=["Cart"])

@cart.post(
    "/cart/{email}/{nome}",
    response_model=Cart,
    status_code=status.HTTP_201_CREATED
)
async def new_cart(nome: str, email: str):
    product_cart = product_list(nome)
    req = {
        'email': email,
        "lista_produtos": product_cart
    }
    if check_user(req) is not None and check_email_cart(req) is None:
        add_cart(req)
    else:
        if check_user(req) is None:
            return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={'message': 'Email nao cadastrado.'})
        if check_email_cart(req) is not None:
            return JSONResponse(status_code=status.HTTP_409_CONFLICT, content={'message': 'Cliente ja possui carrinho aberto.'})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={'message': 'Carrinho aberto para o cliente '+ email})

@cart.delete(
    "/cart{email}/",
    status_code=status.HTTP_204_NO_CONTENT
)
async def remove_cart(email):
    if check_user({"email": email}) is not None:
        result = delete_cart(email)
    else:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={'message': 'Carrinho nao encontrado.'}
            )