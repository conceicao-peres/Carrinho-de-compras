from decoracao.modelos.modelos_carrinho import OrderCarrinho
from fastapi import APIRouter, status, Response
from fastapi.responses import JSONResponse
from decoracao.persistencia.db import connect_db
from decoracao.modelos.modelos_cliente import Item
from decoracao.regras import carrinho_regras
from decoracao.persistencia.cliente_persistencia import valida_email
import datetime

# Minha rota API de carrinho
rota_carrinho = APIRouter(
    # Prefixo para o caminho da rota
    prefix=""
)

# Cria novo carrinho
@rota_carrinho.post(
    "/api/carrinho/",
    response_model=OrderCarrinho,
    # Ajustado o código HTTP de retorno
    status_code=status.HTTP_201_CREATED
)
async def new_cart(new: OrderCarrinho, response: Response):

    req = {
        'user': new.user,
    }
    
    return req

# pesquisar todos os produtos do carrinho
@rota_carrinho.get(
    "/api/carrinho/{email}/",
    status_code=status.HTTP_200_OK
)
async def pesquisar_carrinho_pelo_email(email: str, response: Response):
   
    if valida_email({"email": email}) is not None:
        result = carrinho_regras.pesquisa_carrinho_por_cliente({"email": email}, response)

        return JSONResponse(content=result)
    else:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND, 
            content={'message': 'Email nao cadastrado.'}
            )


