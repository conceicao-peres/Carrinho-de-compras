from pydantic import BaseModel

class Endereco(BaseModel):
    rua: str
    numero: int
    cep: str
    cidade: str
    estado: str
