# API-Loading

Aplicação desenvolvida para seleção de candidatos através da compatibilidade com critérios

## Tabela de conteúdos
=================
<!--ts-->
   * [Sobre](###Sobre)
   * [Como usar](###Como-usar)
   * [Instalação](###Instalacao)
   * [Tecnologias](###Tecnologias)
   * [Contribuintes](###Contribuintes)
<!--te-->

### Sobre

> O projeto consiste a criação de uma plataforma para otimizar a seleção de candidatos.

A construção será através de uma plataforma web que auxilie o usuário a definir a suas próximas contratações dentro do banco de dados através dos parâmetros: idade, localidade, gênero, idioma, habilidades, PCD, dependentes, setor de atuação e nivel de escolaridade;

### Como Usar

O cliente pode fazer uma pesquisa de possíveis candidatos de filtros otimizados.

### Instalação

A implementação do projeto será necessário o usuário ter instalado Python na versão 3.9 ou superior, assim como instalar as frameworks:

  pip install flask
  pip install flask_mysqldb
  pip install request
  
Após realizar o clone do projeto em sua maquina, execute o Script "cdd.sql" no Mysql para criar o banco, tabelas, clounas e inserir alguns dados. É necessário criar uma conexão com o banco local, foi utilizado a porta 3306 padrão da instalão. Caso seu banco possua uma senha, fazer a alteração no arquivo "app.py" na configuração de password:
 
 ![1](https://github.com/Vitordan5/API-Loading/blob/main/gifs/1.png)

Após importar as bibliotecas abra o arquivo "app.py" na IDE e execute a aplicação:

![2](https://github.com/Vitordan5/API-Loading/blob/main/gifs/2.gif)

A aplicação irá abrir uma guia no seu navegador padrão:

![3](https://github.com/Vitordan5/API-Loading/blob/main/gifs/3.gif)

### Tecnologias
* Python 3.9.2 
* MySQL
* Flask
* Bootstrap

### Contribuintes
* [<img src="https://avatars.githubusercontent.com/u/53946335?s=400&v=4" width=60><br><sub>Daniel Bolognesi</sub>](https://github.com/yaybolognesi)
* [<img src="https://avatars.githubusercontent.com/u/55774508?s=400&u=976ce0c58ffb78a832f85cde22b11d2ff9147a1c&v=4" width=60><br><sub>Fernanda Salles</sub>](https://github.com/ferpsalles)
* [<img src="https://avatars.githubusercontent.com/u/73532594?s=400&u=1f8b9362464a88d2551ce0081fe39504709ee0ea&v=4" width=60><br><sub>Gabriel Angelo</sub>](https://github.com/angelog)
* [<img src="https://avatars.githubusercontent.com/u/19509794?s=400&u=c8e3b179223f4af7ed84b484ba70d6377f116c8f&v=4" width=60><br><sub>Nathan Nascimento</sub>](https://github.com/N4htan)
* [<img src="https://avatars.githubusercontent.com/u/55815066?s=400&u=40d9563310eb45bc3daaa829ed56e81758606a2f&v=4" width=60><br><sub>Vitor Silva</sub>](https://github.com/Vitordan5)
