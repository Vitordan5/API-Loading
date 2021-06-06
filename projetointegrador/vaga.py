from db import DatabaseManager
from flask import jsonify

class VagaDatabase:
    def insertVaga(self, lat, long, vars):
        database = DatabaseManager()
        
        query="INSERT INTO vaga (nomeVaga, idUsuario, idConhecimento, idIdiomaVaga, cepVaga, latitudeVaga, longitudeVaga, nivelEscolaridade, pcdVaga, vt) VALUES ('{}', {}, {}, {}, {}, {}, {}, '{}', {}, {})".format(vars["nomeVaga"], vars["idUsuario"], vars["idConhecimento"],vars["idIdiomaVaga"], vars["cepVaga"], lat, long, vars["nivelEsc"], vars["pcdVaga"], vars["vt"])
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

    def filtrarVagaPeso(self,order, id):
        result = self.filtrarVaga(id)

        
        for c in result:
            query="select candidato.nomeCandidato,candidato.emailCandidato,(6371 * acos(cos(radians({})) * cos(radians(candidato.latitudeCandidato)) * cos(radians({}) - radians(candidato.longitudeCandidato)) + sin(radians({})) * sin(radians(candidato.latitudeCandidato)) )) AS distance from candidato".format(c["latitudeVaga"], c["longitudeVaga"], c["latitudeVaga"])
            item = 1
            for x in c:            
                if x == "idConhecimento":
                    if c["idConhecimento"] != None: 
                        query = query + " inner join conhecimento on conhecimento.idConhecimento = {} inner join candidato_conhecimento on candidato_conhecimento.cpfCandidato = candidato.cpfCandidato and candidato_conhecimento.idConhecimento = conhecimento.idConhecimento".format(c["idConhecimento"])
                if x == "idIdiomaVaga":
                    if c["idIdiomaVaga"] != None: 
                        query = query + " inner join idioma on idioma.idIdioma = {} inner join candidato_idioma on candidato_idioma.cpfCandidato = candidato.cpfCandidato and candidato_idioma.idIdioma = idioma.idIdioma".format(c["idIdiomaVaga"])
                if x == "nivelEscolaridade":
                    if c["nivelEscolaridade"] != None: 
                        item = " where candidato.nivelEscolaridade = '{}'".format(c["nivelEscolaridade"])
                        query = query + item
                        item = 0
                if x == "pcdVaga":
                    if c["pcdVaga"] != None:
                        if item == 0:
                            item = " and candidato.pcdCandidato = {}".format(c["pcdVaga"])
                            query = query + item
                        else:
                            item = " where candidato.pcdCandidato = {}".format(c["pcdVaga"])
                            query = query + item
                            print(query)
                if x == "vt":
                    if c["vt"] != None: 
                        if c["vt"] == 0:
                            query = query + " having distance <= 3"
                        else:
                            query = query + " having distance > 3"

        for c in order["order"]:
            dd = []
            dd.append(c) 
        dd = ','.join(dd)
        query = query + " order by "+ dd
        print(query)
                                   
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