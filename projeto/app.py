from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL,MySQLdb 
 
app = Flask(__name__)
        
app.secret_key = "caircocoders-ednalan"
        
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '29031993'
app.config['MYSQL_DB'] = 'mydb'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)
      
@app.route('/')
def index():
    return render_template('index.html')
 
@app.route("/search",methods=["POST","GET"])
def search():
    idade = request.form["idade"]
    idioma = request.form["idioma"]
    escolaridade = request.form["escolaridade"]
    dependentes = request.form["dependentes"]
    pcd = request.form["pcd"]
    genero = request.form["genero"]
    cursor = mysql.connection.cursor()
    query = "SELECT * from cdd WHERE data_nascimento LIKE '%{}%' AND idiomas LIKE '%{}%' AND nivel_escoladidade LIKE '%{}%' AND dependentes LIKE '%{}%' AND pcd LIKE '%{}%' AND genero LIKE '%{}%'".format(idade,idioma,escolaridade, dependentes, pcd,genero)
    cursor.execute(query)
    numrows = int(cursor.rowcount)
    result = cursor.fetchall()
    return jsonify({'htmlresponse': render_template('response.html', cdd=result,numrows=numrows)})

if __name__ == "__main__":
    app.run(debug=True)