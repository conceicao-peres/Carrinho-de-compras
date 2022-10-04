import pytest

from decoracao.rest.principal_rest import dizer_ola


@pytest.mark.asyncio
async def test_principal():
    resultado = await dizer_ola()
    assert resultado == ({"mensagem": "Ok"})

