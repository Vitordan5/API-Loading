from cepCoords import cepCoord
from userClass import Usuario
from flask import Flask,jsonify, request
from flask_mysqldb import MySQL,MySQLdb
from userClass import Usuario
from db import *

app = Flask("JETSOFT")
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'mydb'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app) 

@app.route("/insertUsuario", methods=["POST"])
def teste():
    vars = request.get_json()
    user = Usuario(vars['nome_usuario'], vars['senha'])
    return {"nome":vars['nome_usuario']}

@app.route("/insertVaga", methods = ["POST"])
def insertvaga():
    vars = request.get_json()
    Usuario.insertVaga(vars)
    return {"Vaga":vars['nomeVaga'],"Status":"Inserido com sucesso"}

@app.route("/insertCandidato",methods = ["POST"])
def insertcandidato():
    vars = request.get_json()
    Usuario.insertCandidato(vars)
    return {"nome":vars['nomeCandidato'],"Status":"inserido com sucesso"}

#EXCLUI CANDIDATO
@app.route("/dropCandidato/<cpf>", methods=["DELETE"])
def dropCandidatos(cpf):
    Usuario.dropCandidato(cpf)
    return {"Status":"Excluido com sucesso"}

@app.route("/dropVaga/<id>", methods=["DELETE"])
def dropVaga(id):
    Usuario.dropVaga(id)
    return {"Status":"Excluido com sucesso"}

#Filtra candidato
@app.route("/filterCandidato/cep=<cep>",methods=["GET","POST"])
def filterCandidato(cep):
    vars = request.get_json()
    result = Usuario.filtrarCandidato(cep,vars)
    return result

@app.route("/updateCandidato/<cpf>", methods=["PUT"])
def updateCandidato(cpf):
    vars = request.get_json()
    Usuario.updateCandidato(vars, cpf) 
    return {"Status":"Atualizado com sucesso"}  

app.run()