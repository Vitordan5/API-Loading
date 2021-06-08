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

O usuário poderá selecionar candidato atráves de filtros, sendo ele: pcd, conhecimento, idioma, vale transporte (vt), nível de escolaridade. Os filtros foram alinhados juntamente com o cliente, sendo fixado o vt < 3 quilômetros da instituição como vt =0. Todos os filtros são ordenados conforme necessidade e relevancia do usuário para a busca do candidado "ideal". Ao criar uma vaga, a mesma irá trazer os candidatos, assim como, a pesquisa isolada dos candidatos também será permitido. 

## Tecnologias Utilizadas</br> <a name="-tecnologias"/></a>
•    [Python 3.9](https://www.python.org/)</br>
•    [MySQL](https://www.mysql.com/)</br>
•    [Flask 2.0](https://flask.palletsprojects.com/en/2.0.x/)</br>
•    [Postman](https://www.postman.com/)</br>


As escolhas das tecnologias foram baseadas em performance e redução de complexidade. A escolha de um banco relacional MySQL possibilitou a criação de indices que aumentaram a performance do próprio banco com um número volumoso de dados, assim como o MySQL se tornou o mais popular banco de dados Open Source do mundo.

## Bibliotecas Utilizadas</br> <a name="-bibliotecas"/></a>
•    requests </br>
•    ast</br>
•    flask_mysqldb</br>
•    sqlalchemy</br>

As bibliotecas utilizadas facilitaram na comunicação com o banco de dados, assim como cálculos de localização e aproximação dos candidatos. 


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
| "/insertUsuario" | "POST" | Criação de usuários que são capazes de criar vagas |
| "/insertVaga | "POST" | Inserção de vaga no banco de dados|
| "/updateVaga/informe o id" | "PUT" | Update das descrições da vaga |
| "/dropVaga/informe o id"| "DELETE" | Deletar Vaga |
| "/filterVaga/informe o id" | "GET" | Filtrar as informações da vaga |
| "/filterVaga" | "GET" | Listar todas as vagas disponíveis | 
| "/filterVagaPeso/informe o id" | "GET" | Filtro da vaga retornando os candidatos | 
| "/insertCandidato" | "POST" | Inserir candidatos |
| "/updateCandidato/informe o cpf" | "PUT" | Atualização dos dados do candidato |
| "/dropCandidato/informe o cpf"| "DELETE" | Deletar candidato |
| "/filterCandidato/cep=informe o cep" | "GET" | Filtra candidatos |
| "/filterCandidato" | "GET" | Filtrar todos os candidatos | 
   
##  Exemplos de inserção das rotas disponíveis
   
Informar os dados para inserção do Candidato:</br>
· É necessário informar todas os dados;</br>
· O nível de escolaridade é formado por um ENUM com os seguintes dados (Sem Escolaridade, Tecnico, Medio Completo, Ensino Superior, Pos Graduado);</br>
· Caso só tenha um idioma e um conhecimento é necessário manter dentro de [ ] conforme o exemplo;</br>
· Caso só tenha uma experiencia é necessário manter dentro de [ { } ] conforme o exemplo;</br>
   
```
/insertCandidato
{ 
    "nomeCandidato":"João",
    "cpfCandidato":"0000000000",
    "dataNascimentoCandidato":"01/01/1999",
    "emailCandidato":"joao@hotmail.com",
    "pcdCandidato": 2,
    "cepCandidato":"12335130",
    "telResCandidato":"988888888",
    "telCelCandidato":"988888888",
    "nivelEsc": "Medio Completo",
    "conhecimento": [1, 2, 3],
    "idioma": [1, 2, 3],
    "experiencia": [{"empresa":"EXPERIENCIA", "cargo":"DEV", "tempo": 19},
   {"empresa":"EXPERIENCIA1", "cargo":"DEV", "tempo": 10},
   {"empresa":"EXPERIENCIA2", "cargo":"DEV", "tempo": 4}]
}
```

Para realizar o Update:</br>
· Informar o CPF do candidato na rota e o JSON com as informações a serem atualizadas no exemplo serão atualizados apenas o conhecimento e o idioma.</br>

```
/updateCandidato/informar o CPF
{
    "conhecimento": [2],
    "idioma": [2],
} 
```

Para excluir um candidato informar apenas o CPF do candidato na rota:

```
/dropCandidato/informar o CPF
```

Informar o CEP da "VAGA" na rota para calcular as distancias e o JSON com os filtros caso não queira utilizar algum filtro basta remover a chave:

```
/filterCandidato/cep= informar o CEP
{
    "pcdCandidato": 2,
    "nivelEsc": "Medio Completo",
    "conhecimento": 3,
    "idioma": 2
}
```

Para listar todos os candidatos cadastrados utilize apenas a rota:

```
/filterCandidato
```

Informar os dados para inserção da Vaga:</br>
· Nome , IdUsuario e  CEP são essenciais.</br>

```
/insertVaga
{
    "nomeVaga":"Vaga",
    "idUsuario":1,
    "idConhecimento": 1,
    "pesoConhecimento": 2,
    "idIdiomaVaga": 1,
    "pesoIdioma": 1,
    "cepVaga":"12335130",
    "nivelEsc": "Medio Completo",
    "pesoEscolaridade": 4,
    "pcdVaga": 2,
    "pesoPCD": 3,
    "vt":1
}
```

Informar a ID da vaga na rota e o JSON com as informações a serem atualizadas, no exemplo serão atualizados apenas o conhecimento, idioma e o VT:

```
/updateVaga/<id>
{
    "idConhecimento": 2,
    "idIdiomaVaga": NULL,
    "vt":0
}
 ```
   
Para excluir uma vaga utilize apenas a ID da vaga na rota:   
   
   ```  
/dropVaga/<id>
  ```
 
Para filtrar as informações de uma vaga, utilize apenas a ID da vaga na rota:
  
  ``` 
/filterVaga/<id>
  ``` 
  
Para listar todas as vagas cadastradas use apenas a rota:
 
 ```
/filterVaga
```

Para exibir a vaga com os candidatos filtrados:</br>
· Informe a ID da vaga na rota e o JSON com a ordenação desejada do s candidatos;</br>
· No exemplo ele esta ondenando primeiramente  os candidatos com PCD igual a sim e posteriormente pelo idioma e assim por diante.</br>
   
   ``` 
   /filterVagaPeso/<id>
{
    "order":["pcdCandidato","idioma.idIdioma", "nivelEscolaridade", "conhecimento.idConhecimento"]
}
  
  ``` 
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
- [] Deploy da aplicação
- [x] Documentação de implementação do projeto

# Arquitetura do Projeto <a name="-arquitetura"/></a>
![alt text](https://github.com/Vitordan5/API-Loading/blob/main/gifs/arquitetura.jpeg)
</br></br>


# Diagrama e Modelo Relacional</br> <a name="-diagrama"/></a>
 ![alt text](https://github.com/Vitordan5/API-Loading/blob/main/gifs/bancodedados.jpeg)
</br></br>

# Equipe</br> <a name="-equipe"/></a>
[Fernanda Salles - Product Owner](https://github.com/ferpsalles)</br>
[Gabriel Angelo - Developer](https://github.com/angelog)</br>
[Isis Moraes  - Developer](https://github.com/IsisMoraes)</br>
[Igor Augusto  - Developer](https://github.com/IgorAugustoAlmeida)</br>
[Nathan Nascimento  -Developer](https://github.com/N4htan)</br>
[Vitor Silva - Scrum Master](https://github.com/Vitordan5)</br>
