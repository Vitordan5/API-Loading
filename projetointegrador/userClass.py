from db import DatabaseManager
from vaga import VagaDatabase
from Candidato import CandidatoDatabase
from cepCoords import cepCoord
class Usuario:

#--------------USUARIO--------------
#INSERT
    def insertUsuario(self):
        query = "INSERT INTO usuario(nome_usuario,senha) VALUES('{}','{}')".format(self.usuario,self.senha)
        database = DatabaseManager()
        database.Insert(query)
        return True

    def __init__(self,usuario,senha):
        self.usuario = usuario
        self.senha = senha
        self.insertUsuario()

#--------------VAGA--------------

#INSERT
    def insertVaga(vars):
        buscep= cepCoord(vars["cepVaga"])
        lat = buscep[0]
        long = buscep[1]
        vaga = VagaDatabase()
        vaga.insertVaga(lat, long, vars)

#UPDATE
    def updateVaga(vars, id):
        vaga = VagaDatabase()
        vaga.updateVaga(vars, id)

#DROP
    def dropVaga(id):
        vaga = VagaDatabase()
        vaga.dropVaga(id)

#FILTER
    def filtrarVaga(id):
        vaga = VagaDatabase()
        result = vaga.filtrarVaga(id)
        return result

    def listarVaga():
        vaga = VagaDatabase()
        result = vaga.listarVaga()
        return result

    def filtrarVagaPeso(order,id):
        vaga = VagaDatabase()
        result = vaga.filtrarVagaPeso(order,id)
        return result

#--------------CANDIDATO--------------

#INSERT
    def insertCandidato(vars):
        buscep= cepCoord(vars["cepCandidato"])
        lat = buscep[0]
        long = buscep[1]
        candidato = CandidatoDatabase()
        candidato.insertCandidato(lat, long, vars)

#UPDATE
    def updateCandidato(vars, cpf):
        candidato = CandidatoDatabase()
        candidato.updateCandidato(vars, cpf)

#DROP
    def dropCandidato(cpf):
        candidato = CandidatoDatabase()
        candidato.dropCandidato(cpf)

#FILTER
    def filtrarCandidato(cep,vars):
        buscep= cepCoord(cep)
        lat = buscep[0]
        long = buscep[1]
        candidato = CandidatoDatabase()
        result = candidato.filtrarCandidato(lat,long,vars)
        return result

    def listaCandidato():
        candidato = CandidatoDatabase()
        result = candidato.listaCandidato()
        return result