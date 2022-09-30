from fastapi import APIRouter

# Minha rota API de produto
rota_produto = APIRouter(
    # Prefixo para o caminho da rota
    prefix="/api/produto"
)


# Cria novo produto

