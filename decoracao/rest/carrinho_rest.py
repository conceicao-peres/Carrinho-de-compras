from decoracao.modelos.modelos_carrinho import OrderCarrinho
from fastapi import APIRouter, status, Response
from decoracao.persistencia.db import connect_db
from decoracao.modelos.modelos_cliente import Item
from decoracao.regras import carrinho_regras
import datetime

# Minha rota API de carrinho
rota_carrinho = APIRouter(
    # Prefixo para o caminho da rota
    prefix="/api/carrinho"
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