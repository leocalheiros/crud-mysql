from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from app import app
from app.routes import *
from app.models import *


@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]

        novo_usuario = Usuario(nome=nome, email=email)
        db.session.add(novo_usuario)
        db.session.commit()

        message = "Usuário cadastrado com sucesso!"

    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run()
