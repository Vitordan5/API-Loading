from flask import Flask,jsonify, request
from flask_mysqldb import MySQL,MySQLdb
from db import DatabaseManager

app = Flask("JETSOFT")

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '97855818'
app.config['MYSQL_DB'] = 'mydb'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

#Busca tabela candidatos
@app.route("/candidatos", methods=["GET"])
def showcandidatos():
    result = DatabaseManager.consultarTodos(mysql, 'candidato')
    return jsonify(numrows=len(result), result=result)
#Busca candidato
@app.route("/candidato/<id>", methods=["GET"])
def showcandidato(id):
    result = DatabaseManager.consultar(mysql,'candidatos',id)
    return jsonify(result=result)
#Busca tabela vaga
@app.route("/vagas", methods=["GET"])
def showvagas():
    result = DatabaseManager.consultarTodos(mysql,'vaga')
    return jsonify(numrows=len(result), result=result)
#Filtra candidato
@app.route("/candidatos/filter",methods=["GET"])
def filterCandidato():
    vars = request.get_json()
    result = DatabaseManager.filtrar(mysql, 'candidato', vars)
    print(result)
    return jsonify(numrows=len(result), result=result)


#INSERE UM NOVO CANDIDATO
@app.route("/cadastro/candidato", methods=["POST"])
def insertCandidato():
    vars = request.get_json()
    result = DatabaseManager.inserir(mysql,'candidato',vars)
    sql = "INSERT INTO candidato (nomeCandidato,cpfCandidato,dataNascimentoCandidato,emailCandidato,generoCandidato,pcdCandidato,dependentesCandidato,cepCandidato,telResCandidato,telCelCandidato,nivelEscolaridade) VALUES ({})".format(result)
    print(sql)
    cursor = mysql.connection.cursor()
    cursor.execute(sql)
    mysql.connection.commit()
    return{"nome":vars['nomeCandidato'],"status": "INSERIDO COM SUCESSO"}

#EXCLUI CANDIDATO
@app.route("/dropCandidato/<id>", methods=["DELETE"])
def dropCandidatos(id):
    result = DatabaseManager.delete(mysql,'candidato',id)
    return result


#ATUALIZA OS DADOS DO CANDIDATO
@app.route("/upCandidato/<id>",methods=['PUT'])
def updateCandidato (id):
    vars = request.get_json()
    result = DatabaseManager.update(mysql,'candidato',vars,id)
    return result

app.run()