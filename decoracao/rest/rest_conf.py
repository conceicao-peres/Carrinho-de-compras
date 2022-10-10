from fastapi import FastAPI

from decoracao.rest.cliente_rest import rota_cliente
from decoracao.rest.produto_rest import rota_produto
from decoracao.rest.carrinho_rest import rota_carrinho
from decoracao.rest.principal_rest import rota_principal


def configurar_rotas(app: FastAPI):
    # Publicando as rotas para o FastAPI.
    app.include_router(rota_principal)
    app.include_router(rota_cliente)
    app.include_router(rota_produto)
    app.include_router(rota_carrinho)


def criar_aplicacao_fastapi():
    # Crio a aplicação FastAPI
    app = FastAPI()

    # ... e configuro suas rotas
    configurar_rotas(app)

    return app
