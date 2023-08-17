# CRUD em Flask - Documentação

Este é um projeto simples de CRUD (Create, Read, Update, Delete) em Flask com integração de banco de dados MySQL (persistência de dados).

## Requisitos

- Python 3.x
- Flask
- Flask-SQLAlchemy
- MySQL Server

## Configuração

1. Clone este repositório para sua máquina local:

```sh
git clone https://github.com/leocalheiros/crud-mysql.git
```

2.Instale as dependências:
```
pip install -r requirements.txt
```

3.Configure o banco de dados na máquina:
```
Crie um banco de dados MySQL chamado 'crud'.
Abra o arquivo app.py e atualize a configuração SQLALCHEMY_DATABASE_URI para corresponder às suas configurações do MySQL.
```


## Endpoints da API
- **GET /usuarios: Retorna a lista de todos os usuários cadastrados.**
- **GET /usuario/id: Retorna os detalhes de um usuário específico.**
- **POST /usuario/: Cadastra um novo usuário.**
- **PUT /usuario/id: Atualiza os dados de um usuário existente.**
- **DELETE /usuario/id: Deleta um usuário existente.**
- **Modelo para criar e editar usuário em .json:**

{
    "nome": "Adriano Imperador",
    "email": "didico@gmail.com"
}

