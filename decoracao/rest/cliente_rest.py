from fastapi import APIRouter

# Minha rota API de cliente
rota_cliente = APIRouter(
    # Prefixo para o caminho da rota
    prefix="/api/cliente"
)


# Cria novo cliente
@rota_cliente.post("/")
def criar_novo_cliente(cliente: dict):
    print("Salvar cliente", cliente)

