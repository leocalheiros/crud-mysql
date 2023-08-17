#flask - utilizado pra criar as rotas, Response - retorno api, request - qnd vir os dados
from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy #tratar o banco de dados
import json
import mysql.connector

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/crud'     #definindo banco de dados

db = SQLAlchemy(app) #pra funcionar combinado com o flask