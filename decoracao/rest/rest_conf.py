from fastapi import FastAPI
from decoracao.rest.cliente_rest import user
from decoracao.rest.produto_rest import product
from decoracao.rest.carrinho_rest import cart
from decoracao.rest.endereco_rest import address

def configurar_rotas(app: FastAPI):
    app.include_router(user)
    app.include_router(product)
    app.include_router(cart)
    app.include_router(address)

def criar_aplicacao_fastapi():
    app = FastAPI(title="Shop Cart",
                  version="01")
    configurar_rotas(app)
    return app
