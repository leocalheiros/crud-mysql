#flask - utilizado pra criar as rotas, Response - retorno api, request - qnd vir os dados
from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy #tratar o banco de dados
import mysql.connector
import json

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/crud'     #definindo banco de dados

db = SQLAlchemy(app) #pra funcionar combinado com o flask

#CRUD - Selecionar Tudo, Selecionar Um, Cadastrar, Atualizar, Deletar

class Usuario(db.Model):    #nome final da tabela
    id = db.Column(db.Integer, primary_key = True)   #key primária
    nome = db.Column(db.String(50))
    email = db.Column(db.String(100))

    def to_json(self):   #função pra criar json
        return {"id": self.id, "nome": self.nome, "email": self.email}

#Selecionar Tudo
@app.route("/usuarios", methods=["GET"])
def seleciona_usuarios():
    usuarios_objetos = Usuario.query.all()  #seleciona todos usuários - faz uma query na class que está ligada a tabela no banco de dados
    usuarios_json = [usuario.to_json() for usuario in usuarios_objetos] #pra cada usuario em usuario_objetos ele vai executar a função to json pra pegar os dados
    return gera_response(200, "usuarios", usuarios_json)

def gera_response(status, nome_do_conteudo, conteudo, mensagem=False):
    body = {}          #criamos uma dict vazia pra inputar o nome do nosso conteúdo no json e o conteúdo dentro dela
    body[nome_do_conteudo] = conteudo

    if(mensagem):   #se tiver uma mensagem, ele vai colocar logo abaixo da dict no json, se não tiver ele vai direto pro return
        body[mensagem] = mensagem

    return Response(json.dumps(body), status=status, mimetype="application/json") #precisamos fazer um dump pra ele conseguir retornar

#Selecionar Individual
@app.route("/usuario/<id>", methods=["GET"])
def seleciona_usuario(id):
    usuario_objeto = Usuario.query.filter_by(id=id).first()   #filtrar a query pelo primeiro id, que é a primary key, vai retornar somente a que o usuário colocou na url
    usuario_json = usuario_objeto.to_json()

    return gera_response(200, "usuario", usuario_json)

#Cadastrar
@app.route("/usuario/", methods=["POST"])
def cria_usuario():
    body = request.get_json()
    #Validar se veio os parâmetros ou utilizar um try exception pra gerar erro
    try:
        usuario = Usuario(nome=body["nome"], email= body["email"]) #aqui criamos um usuário passando como parametro nome e email
        db.session.add(usuario)   #aqui criamos a sessão e adicionamos essa classe - sqlalchemy faz esse processo
        db.session.commit()     #commitar o que aconteceu
        return gera_response(201, "usuario", usuario.to_json(), "Criado com suceso!")
    except Exception as e:
        print(e)
        return gera_response(400, "usuario", {}, "Erro ao cadastrar!")

#Atualizar
@app.route("/usuario/<id>", methods=["PUT"])   #mesmo endereço do seleciona apenas um - método PUT - usado pra substituir algo
def atualiza_usuario(id):
    #pega o usuário
    usuario_objeto = Usuario.query.filter_by(id=id).first()
    #pega as modificações
    body = request.get_json()

    try:
        if('nome' in body):
            usuario_objeto.nome = body['nome']
            usuario_objeto.email = body['email']
        if('email' in  body):
            usuario_objeto.email = body['email']
        db.session.add(usuario_objeto)
        db.session.commit()
        return gera_response(201, "usuario", usuario_objeto.to_json(), "Atualizado com suceso!")
    except Exception as e:
        print(e)
        return gera_response(400, "usuario", {}, "Erro ao atualizar")

#Deletar
@app.route("/usuario/<id>", methods=["DELETE"]) #mesmo caminho também
def deleta_usuario(id):
    usuario_objeto = Usuario.query.filter_by(id=id).first()

    try:
        db.session.delete(usuario_objeto)
        db.session.commit()
        return gera_response(200, "usuario", usuario_objeto.to_json(), "Usuário deletado com sucesso!")
    except Exception as e:
        print(e)
        return gera_response(400, "usuario", {}, "Erro ao deletar usuário!")

app.run()



