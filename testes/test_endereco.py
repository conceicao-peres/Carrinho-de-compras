import pytest
import requests
import json

@pytest.mark.asyncio
async def test_criar_endereco():
    payload = json.dumps({ 
        "email": "juju@hotmail.com",
        "rua": "Rua Afonso", 
        "numero": 33, 
        "cep": "20000000", 
        "cidade": "Rio de Janeiro", 
        "estado": "RJ"
        })
    response = requests.post('http://localhost:8000/address/juju@hotmail.com', payload)
    status_code = response.status_code
    assert status_code == 201

@pytest.mark.asyncio
async def test_criar_endereco_email_nao_existe():
    payload = json.dumps({
        "email": "jujuba@hotmail.com",
        "rua": "Rua Afonso",
        "numero": 33,
        "cep": "20000000",
        "cidade": "Rio de Janeiro",
        "estado": "RJ"
        })
    response = requests.post('http://localhost:8000/address/jujuba@hotmail.com', payload)
    status_code = response.status_code
    assert status_code == 404

@pytest.mark.asyncio
async def test_pesquisar_endereco():
    response = requests.get('http://localhost:8000/address/juju@hotmail.com')
    status_code = response.status_code
    assert status_code == 200

@pytest.mark.asyncio
async def test_pesquisar_endereco_emai_nao_existe():
    response = requests.get('http://localhost:8000/address/jujuba@hotmail.com')
    status_code = response.status_code
    assert status_code == 404

@pytest.mark.asyncio
async def test_remove_endereco():
    response = requests.delete('http://localhost:8000/address/juju@hotmail.com')
    status_code = response.status_code
    assert status_code == 204

@pytest.mark.asyncio
async def test_remove_endereco_email_nao_existe():
    response = requests.delete('http://localhost:8000/address/jujuba@hotmail.com')
    status_code = response.status_code
    assert status_code == 404

