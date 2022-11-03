import pytest
import requests
import json

@pytest.mark.asyncio
async def test_criar_novo_cliente():
    payload = json.dumps({'nome': 'juju', 'email': 'juju@hotmail.com'})
    response = requests.post('http://localhost:8000/user', payload)
    status_code = response.status_code
    assert status_code == 201

@pytest.mark.asyncio
async def test_pesquisar_pelo_email():
    response = requests.get('http://localhost:8000/user/maria@hotmail.com')
    status_code = response.status_code
    assert status_code == 200

@pytest.mark.asyncio
async def test_pesquisar_por_email_inexistente():
    response = requests.get('http://localhost:8000/user/xpto@hotmail.com')
    status_code = response.status_code
    assert status_code == 404

@pytest.mark.asyncio
async def test_criar_novo_cliente_email_existente():
    payload = json.dumps({'nome': 'juju', 'email': 'maria@hotmail.com'})
    response = requests.post('http://localhost:8000/user', payload)
    status_code = response.status_code
    assert status_code == 409

@pytest.mark.asyncio
async def test_remove_cliente_inexistente():
    response = requests.delete('http://localhost:8000/user/xpto@hotmail.com')
    status_code = response.status_code
    assert status_code == 404

@pytest.mark.asyncio
async def test_remove_cliente():
    response = requests.delete('http://localhost:8000/user/juju@hotmail.com')
    status_code = response.status_code
    assert status_code == 204

