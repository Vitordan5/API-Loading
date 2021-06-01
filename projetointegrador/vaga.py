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

    def filtrarVaga(self, vars):
        print

    def updateVaga (self, lat, long, vars, id):
        database = DatabaseManager()

        for c in vars:
            if c == "nomeVaga":
                query="UPDATE vaga SET nomeVaga = {} WHERE idVaga = {}".format(vars[c], id)
                database.Insert_Drop(query)

        for c in vars:
            if c == "idIdiomaVaga":
                query="UPDATE vaga SET idIdiomaVaga = {} WHERE idVaga = {}".format(vars[c], id)
                database.Insert_Drop(query)

        for c in vars:
            if c == "pcdVaga":
                query="UPDATE vaga SET pcdVaga = {} WHERE idVaga = {}".format(vars[c], id)
                database.Insert_Drop(query)

        for c in vars:
            if c == "cepVaga":
                query="UPDATE vaga SET cepVaga = {}, latitudeVaga = {}, longitudeVaga = {}  WHERE idVaga = {}".format(vars[c], lat, long, id)
                database.Insert_Drop(query)

        for c in vars:
            if c == "nivelEscolaridade":
                query="UPDATE vaga SET nivelEscolaridade = {} WHERE idVaga = {}".format(vars[c], id)
                database.Insert_Drop(query)