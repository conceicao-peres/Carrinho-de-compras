# Atividade API Carrinho de Compras - Itens de Decoração

![alt text](https://www.dhresource.com/0x0/f2/albu/g21/M00/86/54/rBNaOWDVPnuANs7kAADAHSGqFlc785.jpg)


## Projeto Final do treinamento de Python para o < LuizaCode >
Atividade para elaboração de um carrinho de compras, cadastro de produtos de decoração e cadastro de clientes (com endereço), usando [FastAPI](https://fastapi.tiangolo.com/) e [MongoDB](https://www.mongodb.com/).

## Descrição

### Cadastro de Clientes
- `Cadastrar um cliente`
- `Pesquisar um cliente`
- `Remover um cliente`

### Cadastro de Endereço
- `Cadastrar um endereço`
- `Pesquisar um endereço`
- `Remover um endereço`

### Gerenciamento de Produtos
- `Cadastrar um produto`
- `Atualizar um produto`
- `Pesquisar um produto pelo código`
- `Pesquisar um produto pelo nome`
   
### Carrinho de Compras
- `Criar um carrinho de compras`
- `Adicionar produtos ao carrinho`
- `Alterar a quantidade de itens no carrinho`
- `Consultar um carrinho de compras aberto`
- `Remover o carrinho do cliente`


### Environment
| name_env | value |
|------------|------------|
| DB_HOST | ****|
| DB_USER | ****|
| DB_PASSWD | ****|
| DB_NAME | ****|


### Como executar

* Criar venv
    ```bash
    virtualenv venv --python=3.10
    ```
    
    > Ativar venv no Linux
    ```bash
    source venv/bin/activate
    ```
   > Ativar venv no Windows
    ```bash
    .\venv\Scripts\activate
    ```
* Instalar requerimentos
     ```bash
     pip install -r requirements.txt
     ```
* Executar no Linux
  ```bash
  bash run.sh
  ```
* Executar testes unitário
  ```bash
  pytest
  ```

![alt text](https://www.mtitecnologia.com.br/wp-content/uploads/2021/03/mtitecnologia-luiza-labs.jpg)
  

