from flask import Flask,jsonify, request
from flask_mysqldb import MySQL,MySQLdb

app = Flask("JETSOFT")

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '97855818'
app.config['MYSQL_DB'] = 'mydb'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

class DatabaseManager(object):

    @staticmethod
    def consultarTodos(db, tabela):
        sql = "SELECT * FROM {}".format(tabela)
        cursor = db.connection.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

    @staticmethod
    def consultar(db,tabela,id):
        sql = "SELECT * FROM {} WHERE ID{} = {}".format(tabela,tabela,id)
        cursor =  db.connection.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

    @staticmethod
    def consultarCandidato(db,tabela,id):
        sql = "SELECT * FROM {} WHERE ID{} = {}".format(tabela,tabela,id)
        cursor =  db.connection.cursor()
        cursor.execute(sql)
        
        return cursor.fetchall()

    @staticmethod
    def filtrar(db, tabela, vars):   
        where = []
        for c in vars:
            item = "{} = '{}'".format(c, vars[c])
            where.append(item)
        
        where = ' AND '.join(where)
        print(where)
        sql = "SELECT * FROM {} WHERE {}".format(tabela, where)
        print(sql)
        cursor = db.connection.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

    @staticmethod
    def inserir(db,tabela,vars):
        where = []
        for c in vars:
            item = "'{}'".format(vars[c])
            where.append(item)

        where = ','.join(where)
        print(where)
        return where
    @staticmethod
    def delete(db,tabela,id):
        sql = "DELETE FROM {} WHERE id{} = '{}'".format(tabela,tabela,id)
        print(sql)
        cursor=db.connection.cursor()
        cursor.execute(sql)
        db.connection.commit()
        return {"id": id ,"status":"Excluido com Sucesso" }

    @staticmethod
    def update(db,tabela,vars,id):
        
        for c in vars:
            column = (c)
            newUp = (vars[c])
            print(column,newUp)
            cursor= db.connection.cursor()
            sql = "UPDATE {} SET {} = '{}' WHERE ID{} = {}".format(tabela,column,newUp,tabela,id)
            cursor.execute(sql)
            db.connection.commit()
        return{"status": "Atualizado com Sucesso!"}


        