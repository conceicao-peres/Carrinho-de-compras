from decoracao.modelos.modelos_carrinho import OrderCarrinho

def test_modelo_carrinho(nome: OrderCarrinho):
    cadastro = nome.user
    assert cadastro == ("Ok")