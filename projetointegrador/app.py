from flask import Flask,jsonify, request
from flask_mysqldb import MySQL,MySQLdb

app = Flask("JETSOFT")

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'mydb2'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

#==============================================================================================
#Listar candidatos
@app.route("/candidatos", methods=["GET"])
def showcandidatos():
    cursor = mysql.connection.cursor()
    query = "SELECT nomeCandidato, cpfCandidato, emailCandidato, telResCandidato, telCelCandidato from candidato"
    cursor.execute(query)
    numrows = int(cursor.rowcount)
    result = cursor.fetchall()
    return jsonify(numrows=numrows,result=result)
#==============================================================================================
#Acessar candidato
@app.route("/candidato/<id>", methods=["GET"])
def showcandidato(id):
    cursor = mysql.connection.cursor()
    queryinfoCand = "SELECT * from candidato where candidato.idCandidato = {}".format(id)
    cursor.execute(queryinfoCand)
    infoCandidato = cursor.fetchone()
    queryconheCand = "SELECT descConhecimento from conhecimento where idCandidato = {}".format(id)
    cursor.execute(queryconheCand)
    con = cursor.fetchall()
    conhecimentos = []
    for item in con:
        conhecimentos.append(item)
    queryidiomaCand = "SELECT descIdioma from idioma where idCandidato = {}".format(id)
    cursor.execute(queryidiomaCand)
    con = cursor.fetchall()
    idiomas = []
    for item in con:
        idiomas.append(item)
    queryXpAcad = "SELECT instituicao, curso, tempo from experienciaacad where idCandidato = {}".format(id)
    cursor.execute(queryXpAcad)
    xpAcad = cursor.fetchall()
    queryXpProf = "SELECT empresa, cargo, tempo from experienciaprof where idCandidato = {}".format(id)
    cursor.execute(queryXpProf)
    xpProf = cursor.fetchall()
    return jsonify(experienciaProf=xpProf,experienciaAcad=xpAcad,idiomasCandidato=idiomas,conhecimentosCandidato=conhecimentos,infoCandidato=infoCandidato)

#Atualizar candidato
@app.route("/candidato/<id>",methods=['PUT'])
def updateCandidato (nome,cpf,idade,email,genero,pcd,dependetes,cep,telres,telcel,nivel,id):
    cursor = mysql.connection.cursor()
    body = request.get_json()
    nome = body["nomeCandidato"]
    cpf = body["cpfCandidato"]
    idade = body["dataNascimentoCandidato"]
    email = body["emailCandidato"]
    genero = body["generoCandidato"]
    pcd = body["pcdCandidato"]
    dependetes = body["dependentesCandidato"]
    cep = body["cepCandidato"]
    telres = body["telResCandidato"]
    telcel = body["telCelCandidato"]
    nivel = body["nivelEscolaridade"]
    query = "UPDATE candidato set nomeCandidato='{}', cpfCandidato='{}',dataNascimentoCandidato='{}',emailCandidato='{}',generoCandidato='{}',pcdCandidato='{}',dependentesCandidato='{}',cepCandidato='{}',telResCandidato='{}',telCelCandidato='{}',nivelEscolaridade='{}' where idCandidato='{}'". format(nome,cpf,idade,email,genero,pcd,dependetes,cep,telres,telcel,nivel,id)
    cursor.execute(query)
    mysql.connection.commit()
    return{"status": "Registro Atualizado com Sucesso!"}

#Cadastrar  candidato
@app.route("/candidato", methods=["POST"])
def insertCandidato():
    body = request.get_json()
    candidato = createCandidato(body["nome"],body["cpf"],body["idade"],body["email"],body["genero"],body["pcd"],body["dependentes"],body["cep"],body["telres"],body["telcel"],body["escolaridade"])
    return candidato
def createCandidato(nome,cpf,idade,email,genero,pcd,dependentes,cep,telres,telcel,escolaridade):
    cursor = mysql.connection.cursor()
    query = "INSERT INTO candidato (nomeCandidato,cpfCandidato,dataNascimentoCandidato,emailCandidato,generoCandidato,pcdCandidato,dependentesCandidato,cepCandidato,telResCandidato,telCelCandidato,nivelEscolaridade) VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(nome,cpf,idade,email,genero,pcd,dependentes,cep,telres,telcel,escolaridade)
    cursor.execute(query)
    mysql.connection.commit()
    return {"nome":nome,"status":"Candidato cadastrado",}

#Deletar candidato
@app.route("/dropCandidato/<id>", methods=["DELETE"])
def dropCandidatos(id):
    cursor = mysql.connection.cursor()
    query = "DELETE FROM candidato WHERE idCandidato='{}'".format(id)
    cursor.execute(query)
    mysql.connection.commit()
    return {"status":"Candidato excluido"}
#==============================================================================================
#Filtrar candidatos
@app.route("/candidato/gender=<genero>/pcd=<pcd>/dep=<dependentes>/nivel=<nivelEscolaridade>",methods=["GET"])
def filterCandidato(genero,pcd,dependentes,nivelEscolaridade):
    cursor = mysql.connection.cursor()
    query = "SELECT cpfCandidato, nomeCandidato FROM candidato where generoCandidato = '{}' and pcdCandidato = {} and dependentesCandidato = {} and nivelEscolaridade = '{}' ".format(genero,pcd,dependentes,nivelEscolaridade)
    cursor.execute(query)
    numrows = int(cursor.rowcount)
    result = cursor.fetchall()
    return jsonify(numrows=numrows,result=result)
#==============================================================================================
#Listar vagas
@app.route("/vagas", methods=["GET"])
def showvagas():
    cursor = mysql.connection.cursor()
    query = "SELECT * from vaga"
    cursor.execute(query)
    numrows = int(cursor.rowcount)
    result = cursor.fetchall()
    return jsonify(numrows=numrows,result=result)
#==============================================================================================
#Acessar vaga
@app.route("/vaga/<id>", methods=["GET"])
def showvaga(id):
    cursor = mysql.connection.cursor()
    query = "SELECT * from vaga where idVaga = {}".format(id)
    cursor.execute(query)
    result = cursor.fetchall()
    return jsonify(result=result)

#Deletar vaga
@app.route("/vaga/<id>", methods=["DELETE"])
def dropVaga(id):
    cursor = mysql.connection.cursor()
    query = "delete from vaga where idVaga = '{}'".format(id)
    cursor.execute(query)
    mysql.connection.commit()
    return {"status":"Excluido com Sucesso"}

#Cadastrar vaga
@app.route("/vaga", methods=["POST"])
def insertVaga():
    body = request.get_json()
    vaga = createVaga(body["nomeVaga"],body["idUsuario"],body["idiomaVaga"],body["pcdVaga"],body["dependenteVaga"],body["conhecimentoVaga"],body["setorVaga"],body["nivelEscolaridade"])
    return vaga
def createVaga(nome,idUser,idioma,pcd,dependentes,conhecimento,setor,escolaridade):
    cursor = mysql.connection.cursor()
    query = "INSERT INTO vaga (nomeVaga,idUsuario,idiomaVaga,pcdVaga,dependenteVaga,conhecimentoVaga,setorVaga,nivelEscolaridade) VALUES('{}','{}','{}','{}','{}','{}','{}','{}')".format(nome,idUser,idioma,pcd,dependentes,conhecimento,setor,escolaridade)
    cursor.execute(query)
    mysql.connection.commit()
    return {"nomeVaga":nome,"setorVaga":setor}

#Atualizar vaga
@app.route("/vaga/<id>",methods=["PUT"])
def updateVaga(id,nomeVaga,idiomaVaga,pcdVaga,dependenteVaga,conhecimentoVaga,setorVaga,nivelEscolaridade):
    cursor = mysql.connection.cursor()
    body = request.get_json()
    nomeVaga = body["nomeVaga"]
    idiomaVaga = body["idiomaVaga"]
    pcdVaga = body["pcdVaga"]
    dependenteVaga = ["dependenteVaga"]
    conhecimentoVaga = body["conhecimentoVaga"]
    setorVaga = body["setorVaga"]
    nivelEscolaridade = body["nivelEscolaridade"]
    query = "UPDATE vaga set nomeVaga='{}',idiomaVaga='{}',pcdVaga='{}',dependenteVaga='{}',conhecimentoVaga='{}',setorVaga='{}',nivelEscolaridade='{}' where idVaga = '{}'".format(id,nomeVaga,idiomaVaga,pcdVaga,dependenteVaga,conhecimentoVaga,setorVaga,nivelEscolaridade)
    cursor.execute(query)
    mysql.connection.commit()
    return {"status": "Vaga atualizada"}
#==============================================================================================
#listar usuarios
@app.route("/user", methods=["GET"])
def showusuarios():
    cursor = mysql.connection.cursor()
    query = "SELECT * from usuario "
    cursor.execute(query)
    numrows = int(cursor.rowcount)
    result = cursor.fetchall()
    return jsonify(numrows=numrows,result=result)
#==============================================================================================
#Cadastra usuario
@app.route("/cadastro/user", methods=["POST"])
def insertUser():
    body = request.get_json()
    Usuario = createUser(body["login"],body["senha"])
    return Usuario
def createUser(login,senha):
    cursor = mysql.connection.cursor()
    query = "INSERT INTO usuario (login,senha) VALUES('{}','{}')".format(login,senha)
    cursor.execute(query)
    mysql.connection.commit()
    return {"Status":"Usuario Cadastrado" }

#Acessar usuario
@app.route("/user/<id>", methods=["GET"])
def showusuario(id):
    cursor = mysql.connection.cursor()
    query = "SELECT * from usuario where idUsuario = {}".format(id)
    cursor.execute(query)
    result = cursor.fetchall()
    return jsonify(result=result)

#update usuario
@app.route("/user/<id>",methods=['PUT'])
def updateUsuario (id):
    cursor = mysql.connection.cursor()
    body = request.get_json()
    newSenha = body["senha"]
    query = "UPDATE usuario set senha= '{}' where idUsuario='{}'". format(newSenha, id)
    cursor.execute(query)
    mysql.connection.commit()
    return{"status": "Senha Atualizada com Sucesso!"}

#delete Usuario
@app.route("/user/<id>", methods=["DELETE"])
def dropUser(id):
    cursor = mysql.connection.cursor()
    query = "delete from usuario where idUsuario = '{}'".format(id)
    cursor.execute(query)
    mysql.connection.commit()
    return {"id": id ,"status":"Excluido com Sucesso"}
app.run()