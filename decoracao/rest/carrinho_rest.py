from fastapi import APIRouter

# Minha rota API de carrinho
rota_carrinho = APIRouter(
    # Prefixo para o caminho da rota
    prefix="/api/carrinho"
)


# Cria novo carrinho
