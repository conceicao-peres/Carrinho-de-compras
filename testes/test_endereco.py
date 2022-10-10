import pytest
import requests
import json

@pytest.mark.asyncio
async def test_criar_endereco():
    payload = json.dumps({ 
        "email": "maria@gmail.com", 
        "rua": "Rua Afonso", 
        "numero": 33, 
        "cep": "20000000", 
        "cidade": "Rio de Janeiro", 
        "estado": "RJ"
        })
    response = requests.post('http://localhost:8000/endereco/maria@gmail.com', payload)
    status_code = response.status_code
    assert status_code == 201