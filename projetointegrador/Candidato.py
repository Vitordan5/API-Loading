from db import DatabaseManager
from cepCoords import cepCoord
from flask import jsonify

class CandidatoDatabase:

#INSERT
    def insertCandidato(self, lat, long, vars):
        database = DatabaseManager()
        
        query="INSERT INTO candidato (nomeCandidato, cpfCandidato, dataNascimentoCandidato, emailCandidato, pcdCandidato, cepCandidato, latitudeCandidato, longitudeCandidato, telResCandidato, telCelCandidato, nivelEscolaridade) VALUES ('{}', '{}', {}, '{}', {}, '{}', {}, {}, {}, {}, '{}')".format(vars["nomeCandidato"], vars["cpfCandidato"], vars["dataNascimentoCandidato"], vars["emailCandidato"], vars["pcdCandidato"], vars["cepCandidato"], lat, long, vars["telResCandidato"], vars["telCelCandidato"], vars["nivelEsc"])
        database.Insert_Drop(query)
        
        for c in vars:
            if c == "conhecimento":
                for i in range(len(vars[c])):
                    query ="INSERT INTO candidato_conhecimento (idConhecimento, cpfCandidato) VALUES ({}, '{}')".format(vars[c][i], vars["cpfCandidato"])
                    database.Insert_Drop(query)

        for c in vars:
            if c == "idioma":
                for i in range(len(vars[c])):
                    query ="INSERT INTO candidato_idioma (idIdioma, cpfCandidato) VALUES ({}, '{}')".format(vars[c][i], vars["cpfCandidato"])
                    database.Insert_Drop(query)

        for c in vars:
            if c == "experiencia":
                for i in range(len(vars[c])):
                    query ="INSERT INTO experiencia_profissional (empresa, cargo, cpfCandidato, tempo) VALUES ('{}', '{}', '{}', {})".format(vars[c][i]["empresa"], vars[c][i]["cargo"], vars["cpfCandidato"], vars[c][i]["tempo"])
                    database.Insert_Drop(query)

        return True

#DROP
    def dropCandidato (self, cpf):
        query = "DELETE FROM candidato WHERE cpfCandidato = '{}'".format(cpf)
        database = DatabaseManager()
        database.Insert_Drop(query)

#FILTER
    def filtrarCandidato(self,latuser,longuser,vars):
        item = 1    
        query="select candidato.nomeCandidato,candidato.emailCandidato,(6371 * acos(cos(radians({})) * cos(radians(candidato.latitudeCandidato)) * cos(radians({}) - radians(candidato.longitudeCandidato)) + sin(radians({})) * sin(radians(candidato.latitudeCandidato)) )) AS distance from candidato".format(latuser, longuser, latuser)
        for x in vars:
            if x == "conhecimento":
                query = query + " inner join conhecimento on conhecimento.descConhecimento = '{}' inner join candidato_conhecimento on candidato_conhecimento.cpfCandidato = candidato.cpfCandidato and candidato_conhecimento.idConhecimento = conhecimento.idConhecimento".format(vars[x])
            if x == "idioma":
                query = query + " inner join idioma on idioma.descIdioma = '{}' inner join candidato_idioma on candidato_idioma.cpfCandidato = candidato.cpfCandidato and candidato_idioma.idIdioma = idioma.idIdioma".format(vars[x])
            order = []
            where = []
            if x == "nivelEsc":
                item = " where candidato.nivelEscolaridade = '{}'".format(vars[x])
                item = 0
            if x == "pcd":
                if item == 0:
                    item = " and candidato.pcdCandidato = {}".format(c["pcd"])
                    query = query + item
                else:
                    item = " where candidato.pcdCandidato = {}".format(c["pcd"])
                    query = query + item
                    print(query)
            if x == "vt":
                if vars[x] == 0:
                    query = query + " having distance <= 3"
                else:
                    query = query + " having distance > 3"
            if x == "order":
                for c in x:
                    order.append(vars[x][c]) 
                order = ','.join(order)
                query = query + "order by "+ order

        database = DatabaseManager()
        result = database.Filtrar(query)
        print(result)
        return jsonify(result=result)

    def listaCandidato(self):
        database = DatabaseManager()
        query = "select * from candidato"
        result = database.Filtrar(query)
        return jsonify(result = result)

#UPDATE
    def updateCandidato (self, vars, cpf):
        database = DatabaseManager()
        
        for c in vars:
            if c == "conhecimento":
                for i in range(len(vars[c])):
                    query ="INSERT INTO candidato_conhecimento (idConhecimento, cpfCandidato) VALUES ({}, '{}')".format(vars[c][i], cpf)
                    database.Insert_Drop(query)

        for c in vars:
            if c == "idioma":
                for i in range(len(vars[c])):
                    query ="INSERT INTO candidato_idioma (idIdioma, cpfCandidato) VALUES ({}, '{}')".format(vars[c][i], cpf)
                    database.Insert_Drop(query)

        for c in vars:
            if c == "experiencia":
                for i in range(len(vars[c])):
                    query ="INSERT INTO experiencia_profissional (empresa, cargo, cpfCandidato, tempo) VALUES ('{}', '{}', '{}', {})".format(vars[c][i]["empresa"], vars[c][i]["cargo"], cpf, vars[c][i]["tempo"])
                    database.Insert_Drop(query)

        for c in vars:
            if c == "nomeCandidato":
                query="UPDATE candidato SET nomeCandidato = '{}' WHERE cpfCandidato = '{}'".format(vars[c], cpf)
                database.Insert_Drop(query)

        for c in vars:
            if c == "dataNascimentoCandidato":
                query="UPDATE candidato SET dataNascimentoCandidato = {} WHERE cpfCandidato = '{}'".format(vars[c], cpf)
                database.Insert_Drop(query)

        for c in vars:
            if c == "emailCandidato":
                query="UPDATE candidato SET emailCandidato = '{}' WHERE cpfCandidato = '{}'".format(vars[c], cpf)
                database.Insert_Drop(query)

        for c in vars:
            if c == "pcdCandidato":
                query="UPDATE candidato SET pcdCandidato = {} WHERE cpfCandidato = '{}'".format(vars[c], cpf)
                database.Insert_Drop(query)

        for c in vars:
            if c == "cepCandidato":
                buscep= cepCoord(vars["cepCandidato"])
                lat = buscep[0]
                long = buscep[1]
                query="UPDATE candidato SET cepCandidato = '{}', latitudeCandidato = {}, longitudeCandidato = {}  WHERE cpfCandidato = '{}'".format(vars[c], lat, long, cpf)
                database.Insert_Drop(query)

        for c in vars:
            if c == "telResCandidato":
                query="UPDATE candidato SET telResCandidato = '{}' WHERE cpfCandidato = '{}'".format(vars[c], cpf)
                database.Insert_Drop(query)

        for c in vars:
            if c == "telCelCandidato":
                query="UPDATE candidato SET telCelCandidato = '{}' WHERE cpfCandidato = '{}'".format(vars[c], cpf)
                database.Insert_Drop(query)

        for c in vars:
            if c == "nivelEscolaridade":
                query="UPDATE candidato SET nivelEscolaridade = '{}' WHERE cpfCandidato = '{}'".format(vars[c], cpf)
                database.Insert_Drop(query)