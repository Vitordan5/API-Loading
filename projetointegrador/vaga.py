from db import DatabaseManager
from flask import jsonify

class VagaDatabase:
    def insertVaga(self, lat, long, vars):
        database = DatabaseManager()
        
        query="INSERT INTO vaga (nomeVaga, idUsuario, idIdiomaVaga, pcdVaga, cepVaga, latitudeVaga, longitudeVaga, nivelEscolaridade) VALUES ('{}', {}, {}, {}, {}, {}, {}, '{}')".format(vars["nomeVaga"], vars["idUsuario"], vars["idIdiomaVaga"], vars["pcdVaga"], vars["cepVaga"], lat, long, vars["nivelEsc"])
        database.Insert_Drop(query)

        return True

    def dropVaga (self, id):
        query = "DELETE FROM vaga WHERE idVaga = '{}'".format(id)
        database = DatabaseManager()
        database.Insert_Drop(query)

    def filtrarVaga(self, id):
        query="select * from vaga where idVaga = {}".format(id)
        database = DatabaseManager()
        result = database.Filtrar(query)
        return jsonify(result=result)
    
    def listarVaga(self):
        query="select * from vaga"
        database = DatabaseManager()
        result = database.Filtrar(query)
        return jsonify(result=result)

    def updateVaga (self, vars, id):
        database = DatabaseManager()

        for c in vars:
            query="UPDATE vaga SET {} = '{}' WHERE idVaga = {}".format(c , vars[c], id)
            database.Insert_Drop(query)