
where = ['candidato.nivelEscolaridade = "medio completo"', 'candidato.pcdCandidato = 2']
query = "select * from candidato"

for i in range(len(where) != 0):
    separador = " and "
    newWhere = separador.join(where)
    query = query + " where " + newWhere
    print(query)
