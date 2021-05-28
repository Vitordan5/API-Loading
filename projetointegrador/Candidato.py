from db import DatabaseManager
from flask import jsonify

class CandidatoDatabase:
    def insertCandidato(self, lat, long, vars):
        database = DatabaseManager()
        
        query="INSERT INTO candidato (nomeCandidato, cpfCandidato, dataNascimentoCandidato, emailCandidato, pcdCandidato, cepCandidato, latitudeCandidato, longitudeCandidato, telResCandidato, telCelCandidato, nivelEscolaridade) VALUES ('{}', '{}', {}, '{}', {}, {}, {}, {}, {}, {}, '{}')".format(vars["nomeCandidato"], vars["cpfCandidato"], vars["dataNascimentoCandidato"], vars["emailCandidato"], vars["pcdCandidato"], vars["cepCandidato"], lat, long, vars["telResCandidato"], vars["telCelCandidato"], vars["nivelEsc"])
        database.Insert_Drop(query)
        
        for c in vars:
            if c == "conhecimento":
                for i in range(len(vars[c])):
                    query ="INSERT INTO candidato_conhecimento (idConhecimento, cpfCandidato) VALUES ({}, {})".format(vars[c][i], vars["cpfCandidato"])
                    database.Insert_Drop(query)

        for c in vars:
            if c == "idioma":
                for i in range(len(vars[c])):
                    query ="INSERT INTO candidato_idioma (idIdioma, cpfCandidato) VALUES ({}, {})".format(vars[c][i], vars["cpfCandidato"])
                    database.Insert_Drop(query)

        for c in vars:
            if c == "experiencia":
                for i in range(len(vars[c])):
                    query ="INSERT INTO experiencia_profissional (empresa, cargo, cpfCandidato, tempo) VALUES ('{}', '{}', {}, {})".format(vars[c][i]["empresa"], vars[c][i]["cargo"], vars["cpfCandidato"], vars[c][i]["tempo"])
                    database.Insert_Drop(query)

        return True

    def dropCandidato (self,cpf):
        query = "DELETE FROM candidato WHERE cpfCandidato = '{}'".format(cpf)
        database = DatabaseManager()
        database.Insert_Drop(query)

    def filtrarCandidato(self,latuser,longuser,vars):
        print(latuser[0])
        query="select candidato.nomeCandidato,candidato.emailCandidato,(6371 * acos(cos(radians({})) * cos(radians(candidato.latitudeCandidato)) * cos(radians({}) - radians(candidato.longitudeCandidato)) + sin(radians({})) * sin(radians(candidato.latitudeCandidato)) )) AS distance from candidato".format(latuser[0],longuser[0],latuser[0])
        for x in vars:
            if x == "conhecimento":
                query = query + " inner join conhecimento on conhecimento.descConhecimento = '{}' inner join candidato_conhecimento on candidato_conhecimento.idCandidato = candidato.idCandidato and candidato_conhecimento.idConhecimento = conhecimento.idConhecimento".format(vars[x])
            if x == "idioma":
                query = query + " inner join idioma on idioma.descIdioma = '{}' inner join candidato_idioma on candidato_idioma.idCandidato = candidato.idCandidato and candidato_idioma.idIdioma = idioma.idIdioma".format(vars[x])
            where = []
            if x == "nivelEsc":
                item = "candidato.nivelEscolaridade = '{}'".format(vars[x])
                where.append(item)
            if x == "pcd":
                item = "candidato.pcdCandidato = {}".format(vars[x])
                where.append(item)
            if len(where) != 0:
                where = ' AND '.join(where)
                query = query + " where " + where
            if x == "vt":
                if vars[x] == 0:
                    query = query + " having distance <= 3"
                else:
                    query = query + " having distance > 3"
            if x == "order":
                if vars[x] == "distance":
                    query = query + " order by distance"
                elif vars[x] == "nivel desc":
                    query = query + " order by field(nivelEscolaridade,'sem escolaridade','tecnico','medio completo','ensino superior','pos graduado')"
                elif vars[x] == "nivel asc":
                    query = query + " order by field(nivelEscolaridade,'pos graduado','ensino superior','tecnico','medio completo','sem escolaridade')"
                
        database = DatabaseManager()
        result = database.Filtrar(query)
        print(result)
        return jsonify(result=result)

    def updateCandidato (self, vars, cpf):
        database = DatabaseManager()
        for c in vars:
            if c == "conhecimento":
                for i in range(len(vars[c])):
                    query ="INSERT INTO candidato_conhecimento (idConhecimento, cpfCandidato) VALUES ({}, {})".format(vars[c][i], cpf)
                    database.Insert_Drop(query)
