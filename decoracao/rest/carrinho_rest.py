from fastapi import APIRouter, status, Response
from fastapi.responses import JSONResponse
from decoracao.modelos.modelos_carrinho import Carrinho
from decoracao.modelos.modelos_produtos import Product
from decoracao.regras.carrinho_regras import cria_lista_produtos
from decoracao.persistencia.cliente_persistencia import valida_email
from decoracao.persistencia.carrinho_persistencia import cadastrar_carrinho, valida_email_carrinho, add_item_carrinho
from decoracao.regras.produto_regras import valida_nome_produto

rota_carrinho = APIRouter(prefix="/api")

@rota_carrinho.post(
    "/criar/carrinho/{email}/{nome}",
    response_model=Carrinho,
    status_code=status.HTTP_201_CREATED
)
async def criar_novo_carrinho(nome: str, email: str):
    produto_carrinho = cria_lista_produtos(nome)
    req = {
        'email': email,
        "lista_produtos": produto_carrinho
    }
    if valida_email(req) is not None and valida_email_carrinho(req) is None:
        cadastrar_carrinho(req)
    else:
        if valida_email(req) is None:
            return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={'message': 'Email nao cadastrado.'})
        if valida_email_carrinho(req) is not None:
            return JSONResponse(status_code=status.HTTP_409_CONFLICT, content={'message': 'Cliente ja possui carrinho aberto.'})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={'message': 'Carrinho aberto para o cliente '+ email})
