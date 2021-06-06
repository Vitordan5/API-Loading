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
O projeto realizado está na área de recrutamento de candidatos, na qual consiste na criação de uma api web simples para criação de vaga e busca do candidato, com foco na otimização da seleção. A estruturação de um eficiente processo de recrutamento facilita a seleção de talentos e competências necessárias para a continuidade e o sucesso das instituições.
</br></br>

## Funcionalidade </br>

O usuário poderá selecionar candidato atráves de filtros 

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

 > Crie o banco de dados 
 1. Utilizar o script SQL que está na pasta "API-Loading/projetointegrador/bd/bd.sql" para ter o modelo do banco.
 
 > Como rodar a aplicação:
 1. Alterar as configurações do banco de dados nos arquivos "bd.py" e "app.py"
 2. Para [configurar e executar o ambiente virtual](https://www.youtube.com/watch?v=hA2l0TgaZhM), a pasta do ambiente virtual criado para este projeto se encontra na pasta "venv" 
 4. Com o ambiente virtual ativado execute o arquivo "app.py"
 5. Recomendamos que utilize o software [Postman](https://www.postman.com/downloads/) para testar a rotas disponiveis no projeto.

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
|"/filterCandidato/cep=<cep>" |"GET" | Lista de candidatos filtrada|


# Backlog</br> <a name="-backlog"/></a>

* **SPRINT 1 - 28/03**

- [x] Modelo do banco: Modelo Lógica e Física 
- [x] Interface para filtros 
- [x] Parametrização dos filtros: PCD, dependentes, gênero, idioma e nivel de escolaridade

* **SPRINT 2  -  18-04** 
- [x] Desenvolvimento das rotas de CRUD (usuários, vagas e candidatos) 
- [x] Desenvolvimento dos indices no banco de dados - otimização de performance no banco de dados 
- [x] Melhorias na documentação do projeto 

* **SPRINT 3 - 16-05** 
- [x] Melhorias na arquitetura 
- [x] Reestruturação do banco de dados - adicionar colunas na otimização de filtro de localização 
- [x] Desenvolvimento de rotas de filtros otimizados e ordenados: localização, nivel de escolaridade, pcd, idioma  

* **SPRINT 4 - 05-06** 
- [x] Otimização do filtro nivel de escolaridade 
- [x] Otimização do filtro de vaga - trazer como resultado candidatos 
- [x] Otimização do filtro de candidatos - capacidade de ordenação dos filtros estabelecidos 
- [x] Documentação de implementação do projeto

# Arquitetura do Projeto <a name="-arquitetura"/></a>
![alt text](https://github.com/Vitordan5/API-Loading/blob/main/gifs/arquitetura.jpeg)
</br></br>


# Diagrama e Modelo Relacional</br> <a name="-diagrama"/></a>
 ![alt text](https://github.com/Vitordan5/API-Loading/blob/main/gifs/EER.png)
</br></br>

# Equipe</br> <a name="-equipe"/></a>
Fernanda Salles </br>
Gabriel Angelo </br>
Isis Moraes </br>
Igor Augusto </br>
Nathan Nascimento </br>
Vitor Silva </br>
