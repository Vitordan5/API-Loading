<h1 align="center">API - LOADING</h1>

## Menu

<p align="center">
   <a href="#-visao">Visão do Projeto</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-tecnologias">Tecnologias Utilizadas</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-bibliotecas">Bibliotecas</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-instrucao">Implementação</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
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
•    Postman</br>

## Bibliotecas Utilizadas</br> <a name="-bibliotecas"/></a>
•    requests </br>
•    ast</br>
•    flask_mysqldb</br>



## Instruções de implementação </br> <a name="-instrucao"/></a>
 > Como rodar a aplicação:
 
 1. Criar um database mydb no banco de dados
 2. Alterar as configurações do banco de dados
 3. Rodar arquivo app.py
 4. Postman: atribuir a rota desejada, com o respectivo método.
 


# Requisitos</br> <a name="-requisitos"/></a>
## Requisitos Funcionais</br>

· Criar interface de submissão de currículos que recebam, de forma padronizada e adequada ao processo, os candidatos; </br>
· Busca de candidatos por vagas; </br>
· Utilizar filtros configuráveis nas buscas de cada vaga; </br>


## Requisitos Não Funcionais</br>
· Arquitetura do BD;</br>
· Desempenho;</br>
· Segurança (Safety);</br>
· Documentação específica;</br>


## Rotas Disponíveis <a name="-rotas"/></a>

|  ROTAS  CRUD | METHOD | RESPOSTA |
|--------|----------|----------|
| "/candidatos" ; "/vagas" ; "/user" | "GET" | Listar objeto requisitado  |
| "/candidato/<id>" ; "/vagas/<id>" ; "/user/<id>" | "GET" | Overview do objeto requisitado  |
| "/candidato" ; "/user" ; "/vaga" | "POST" | Cadastrar do objeto |
| "/candidato" ; "/user" ; "/vaga" | "DELETE" | Deletar do objeto |
| "/candidato" ; "/user" ; "/vaga" | "PUT" | Atualizar do objeto | 
   
| ROTAS FILTROS | METHOD | RESPOSTA |
|--------|----------|----------|
|""/candidato/origem=<cep>/pcd=<pcd>/idioma=<idioma>/nivel=<nivelEscolaridade>/order=<order>" |"GET" | Lista de candidatos filtrada|


# Backlog</br> <a name="-backlog"/></a>

* **SPRINT 0 - 28/03**

- [x] Modelo do banco: Modelo Lógica e Física 
- [x] Interface para filtros 
- [x] Parametrização dos filtros: PCD, dependentes, gênero, idioma e nivel de escolaridade

* **SPRINT 1  -  18-04** 
- [x] Desenvolvimento das rotas de CRUD (usuários, vagas e candidatos) 
- [x] Desenvolvimento dos indices no banco de dados - otimização de performance no banco de dados 
- [x] Melhorias na documentação do projeto 

* **SPRINT 2 - 16-05** 
- [x] Melhorias na arquitetura 
- [x] Reestruturação do banco de dados - adicionar colunas na otimização de filtro de localização 
- [x] Desenvolvimento de rotas de filtros otimizados e ordenados: localização, nivel de escolaridade, pcd, idioma  

* **SPRINT 3 - 05-06** 
- [ ] Melhorias na arquitetura - atribuição do padrão Facade
- [ ] Otimização do filtro nivel de escolaridade 
- [ ] Otimização do filtro de vaga - trazer como resultado candidatos 
- [ ] Documentação de implementação do projeto 

# Arquitetura do Projeto <a name="-arquitetura"/></a>
![alt text](https://github.com/Vitordan5/API-Loading/blob/main/gifs/arquitetura.jpeg)
</br></br>


# Diagrama e Modelo Relacional</br> <a name="-diagrama"/></a>
 ![alt text](https://github.com/Vitordan5/API-Loading/blob/main/gifs/EER.png)
</br></br>

# Equipe</br> <a name="-equipe"/></a>
Daniel Bolognesi </br>
Fernanda Salles </br>
Gabriel Angelo </br>
Isis Moraes </br>
Igor Augusto </br>
Nathan Nascimento </br>
Vitor Silva </br>
