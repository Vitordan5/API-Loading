from db import DatabaseManager
from flask import Flask,jsonify, request

class CandidatoDatabase:
    def insertCandidato(self,vars):
       
        where = []
        for c in vars:
            item = "'{}'".format(vars[c])
            where.append(item)

        where = ','.join(where)
        query="INSERT INTO candidato (nomeCandidato, cpfCandidato, dataNascimentoCandidato, emailCandidato, pcdCandidato, cepCandidato, latitudeCandidato, longitudeCandidato, telResCandidato, telCelCandidato, nivelEscolaridade) VALUES ({})".format(where)
        database = DatabaseManager()
        database.Insert_Drop(query)
        return True

    def dropCandidato (self,id):
        query = "DELETE FROM candidato WHERE idCandidato = '{}'".format(id)
        database = DatabaseManager()
        database.Insert_Drop(query)

    def filtrarCandidato(self,latuser,longuser,vars):
        query="select candidato.nomeCandidato,candidato.emailCandidato,(6371 * acos(cos(radians(@latempresa)) * cos(radians(candidato.latitudeCandidato)) * cos(radians(@lonempresa) - radians(candidato.longitudeCandidato)) + sin(radians(@latempresa)) * sin(radians(candidato.latitudeCandidato)) )) AS distance from candidato".format(latuser,longuser,latuser)
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
        return jsonify(result=result)
