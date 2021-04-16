from flask import Flask,jsonify, request
from flask_mysqldb import MySQL,MySQLdb

app = Flask("JETSOFT")

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'mydb2'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

@app.route("/candidatos", methods=["GET"])
def showcandidatos():
    cursor = mysql.connection.cursor()
    query = "SELECT * from candidato "
    cursor.execute(query)
    numrows = int(cursor.rowcount)
    result = cursor.fetchall()
    return jsonify(numrows=numrows,result=result)

@app.route("/candidato/<id>", methods=["GET"])
def showcandidato(id):
    cursor = mysql.connection.cursor()
    query = "SELECT * from candidato where idCandidato = {}".format(id)
    cursor.execute(query)
    result = cursor.fetchall()
    return jsonify(result=result)

@app.route("/vagas", methods=["GET"])
def showvagas():
    cursor = mysql.connection.cursor()
    query = "SELECT * from vaga"
    cursor.execute(query)
    numrows = int(cursor.rowcount)
    result = cursor.fetchall()
    return jsonify(numrows=numrows,result=result)

@app.route("/vaga/<id>", methods=["GET"])
def showvaga(id):
    cursor = mysql.connection.cursor()
    query = "SELECT * from vaga where idVaga = {}".format(id)
    cursor.execute(query)
    result = cursor.fetchall()
    return jsonify(result=result)

@app.route("/candidato/gender=<genero>/pcd=<pcd>/dep=<dependentes>/nivel=<nivelEscolaridade>",methods=["GET"])
def filterCandidato(genero,pcd,dependentes,nivelEscolaridade):
    cursor = mysql.connection.cursor()
    query = "SELECT * FROM candidato where generoCandidato = '{}' and pcdCandidato = {} and dependentesCandidato = {} and nivelEscolaridade = '{}' ".format(genero,pcd,dependentes,nivelEscolaridade)
    cursor.execute(query)
    numrows = int(cursor.rowcount)
    result = cursor.fetchall()
    return jsonify(numrows=numrows,result=result)

@app.route("/candidato/gender=<genero>",methods=["GET"])
def filterGenCandidato(genero):
    cursor = mysql.connection.cursor()
    query = "SELECT * FROM candidato where generoCandidato = '{}' ".format(genero)
    cursor.execute(query)
    numrows = int(cursor.rowcount)
    result = cursor.fetchall()
    return jsonify(numrows=numrows,result=result)

app.run()