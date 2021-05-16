from db import DatabaseManager

class VagaDatabase:

    def insertVaga(self,vars):
        where = []
        for c in vars:
            item = "'{}'".format(vars[c])
            where.append(item)

        where = ','.join(where)
        query= "INSERT INTO vaga (nomeVaga,idiomaVaga,conhecimentoVaga,nivelEscVaga,localizacao)values({})".format(where)
        database = DatabaseManager()
        database.Insert(query)
        return True
    
    def dropVaga (self,id):
        query = "DELETE FROM vaga WHERE idVaga = '{}'".format(id)
        database = DatabaseManager()
        database.Drop(query)