# API-Loading

## Menu

<p align="center">
   <a href="#-visao">Visão do Projeto</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-tecnologia">Tecnologias Utilizadas</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-requisitos">Requisitos</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-rotas">Rotas Disponíveis</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-backlog">Backlog</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-diagrama">Diagrama</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-equipe">Equipe</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;

</p>

# Apresentação do Projeto</br>

## Visão do Projeto</br> <a name="-visao"/></a>
O projeto consiste na criação de uma api web simples para busca de candidatos e vagas de emprego, com foco na otimização na seleção de candidatos.
</br></br>

## Tecnologias Utilizadas</br> <a name="-tecnologias"/></a>
•    Python 3.9</br>
•    MySQL</br>
•    Flask</br>
•    Workbench</br>
•    Postman</br>

# Requisitos</br> <a name="-requisitos"/></a>
## Requisitos Funcionais</br>
•    Definir filtros personalizados para busca de candidatos ;</br>
•    Visualização resumida e/ou completa dos candidatos e vagas;</br>
•    Submissão de currículos na interface;</br>

## Requisitos Não Funcionais</br>
•    Documentação do projeto;</br>
•    Diagramas e Modelo Relacional;</br></br>


## Rotas Disponíveis <a name="-rotas"/></a>

|  ROTA EXEMPLO | METHOD | RESPOSTA |
|--------|----------|----------|
| "/candidatos" ; "/vagas" ; "/user" | "GET" | Listar objeto requisitado  |
| "/candidato/<id>" ; "/vagas/<id>" ; "/user/<id>" | "GET" | Overview do objeto requisitado  |
| "/candidato" ; "/user" ; "/vaga" | "POST" | Cadastrar do objeto |
| "/candidato" ; "/user" ; "/vaga" | "DELETE" | Deletar do objeto |
| "/candidato" ; "/user" ; "/vaga" | "PUT" | Atualizar do objeto | 
 |"/candidato/gender=<genero>/pcd=<pcd>/dep=<dependentes>/nivel=<nivelEscolaridade>"| "GET' | Lista de candidatos filtrada |


# Backlog</br> <a name="-backlog"/></a>
- Sprint 0 - Aplicação onde é possivel ser feito busca dos candidatos e filtrá-los pelos parâmetros: PCD, dependentes, gênero, idioma e nivel de escolaridade.</br>
- Sprint 1 - Desenvolvimento das rotas de CRUD (usuários, vagas e candidatos) e rotas das listas.</br>

# Diagrama e Modelo Relacional</br> <a name="-diagrama"/></a>
 ![alt text](https://github.com/Vitordan5/API-Loading/blob/main/gifs/ModeloBanco.JPG)
</br></br>

# Equipe</br> <a name="-equipe"/></a>
Daniel Bolognesi </br>
Fernanda Salles </br>
Gabriel Angelo </br>
Isis Moraes </br>
Igor Augusto </br>
Nathan Nascimento </br>
Vitor Silva </br>
