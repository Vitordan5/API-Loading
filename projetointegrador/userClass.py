from db import DatabaseManager
from vaga import VagaDatabase
from Candidato import CandidatoDatabase
from cepCoords import cepCoord
class Usuario:

    def insertUsuario(self):
        query = "INSERT INTO usuario(nome_usuario,senha) VALUES('{}','{}')".format(self.usuario,self.senha)
        database = DatabaseManager()
        database.Insert(query)
        return True

    def __init__(self,usuario,senha):
        self.usuario = usuario
        self.senha = senha
        self.insertUsuario()

    def insertVaga(vars):
        vaga = VagaDatabase()
        print(vars)
        vaga.insertVaga(vars)

    def insertCandidato(vars):
        candidato = CandidatoDatabase()
        candidato.insertCandidato(vars)

    def dropCandidato(id):
        candidato = CandidatoDatabase()
        candidato.dropCandidato(id)

    def filtrarCandidato(cep,vars):
        buscep= cepCoord(cep)
        lat = buscep[0]
        long = buscep[1]
        candidato = CandidatoDatabase()
        result = candidato.filtrarCandidato(lat,long,vars)
        return result