from fastapi import FastAPI
from decoracao.rest.cliente_rest import rota_cliente
from decoracao.rest.principal_rest import rota_principal


def configurar_rotas(app: FastAPI):
    # Publicando as rotas para o FastAPI.
    app.include_router(rota_principal)
    app.include_router(rota_cliente)


def criar_aplicacao_fastapi():
    # Crio a aplicação FastAPI
    app = FastAPI()

    # ... e configuro suas rotas
    configurar_rotas(app)

    return app