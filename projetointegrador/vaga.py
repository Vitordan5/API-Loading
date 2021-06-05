from db import DatabaseManager
from flask import jsonify

class VagaDatabase:
    def insertVaga(self, lat, long, vars):
        database = DatabaseManager()
        
        query="INSERT INTO vaga (nomeVaga, idUsuario, idConhecimento, pesoConhecimento, idIdiomaVaga, pesoIdioma, cepVaga, latitudeVaga, longitudeVaga, nivelEscolaridade, pesoEscolaridade, pcdVaga, pesoPCD, vt) VALUES ('{}', {}, {}, {}, {}, {}, {}, {}, {}, '{}', {}, {}, {}, {})".format(vars["nomeVaga"], vars["idUsuario"], vars["idConhecimento"], vars["pesoConhecimento"],vars["idIdiomaVaga"], vars["pesoIdioma"], vars["cepVaga"], lat, long, vars["nivelEsc"], vars["pesoEscolaridade"], vars["pcdVaga"], vars["pesoPCD"], vars["vt"])
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
        return result

    def filtrarVagaPeso(self, id):
        result = self.filtrarVaga(id)
        
        for c in result:
            query="select candidato.nomeCandidato,candidato.emailCandidato,(6371 * acos(cos(radians({})) * cos(radians(candidato.latitudeCandidato)) * cos(radians({}) - radians(candidato.longitudeCandidato)) + sin(radians({})) * sin(radians(candidato.latitudeCandidato)) )) AS distance from candidato".format(c["latitudeVaga"], c["longitudeVaga"], c["latitudeVaga"])
            for x in c:
                if x == "idConhecimento":
                    query = query + " inner join conhecimento on conhecimento.idConhecimento = {} inner join candidato_conhecimento on candidato_conhecimento.cpfCandidato = candidato.cpfCandidato and candidato_conhecimento.idConhecimento = conhecimento.idConhecimento".format(c["idConhecimento"])
                    print(query)
                if x == "idIdiomaVaga":
                    query = query + " inner join idioma on idioma.idIdioma = {} inner join candidato_idioma on candidato_idioma.cpfCandidato = candidato.cpfCandidato and candidato_idioma.idIdioma = idioma.idIdioma".format(c["idIdiomaVaga"])
                    print(query)
                where = []
                if x == "nivelEscolaridade":
                    item = "where candidato.nivelEscolaridade = '{}'".format(c["nivelEscolaridade"])
                    where.append(item)
                if x == "pcdVaga":
                    item = "and candidato.pcdCandidato = {}".format(c["pcdVaga"])
                    where.append(item)
                if x == "vt":
                    if c["vt"] == 0:
                        query = query + " having distance <= 3"
                    else:
                        query = query + " having distance > 3"
                
            print(query)
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