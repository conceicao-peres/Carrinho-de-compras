import datetime
from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, Field
from typing import List

# aguardando finalização endereço from modelos.modelos_address import Address
# aguardando finalização produto from modelos.modelos_produto import Protudo
from decoracao.modelos.modelos_cliente import Item

#Classe com o carrinho de compras com um cliente, lista de produtos, total dos produtos e total do valor; se está pago ou não
class OrderCarrinho(BaseModel):
    user: Item
    id_produto: List[int] = []
    total_price: float = 0 
    total_quantity: int = 0