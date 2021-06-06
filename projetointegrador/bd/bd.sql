create database mydb;
use mydb;

CREATE TABLE IF NOT exists candidato (
    idCandidato INT UNIQUE AUTO_INCREMENT,
    nomeCandidato VARCHAR(100) NOT NULL,
    cpfCandidato VARCHAR(11) NOT NULL,
    dataNascimentoCandidato DATE NOT NULL,
    emailCandidato VARCHAR(100) NOT NULL,
    pcdCandidato TINYINT NOT NULL,
    cepCandidato VARCHAR(8) NOT NULL,
    latitudeCandidato FLOAT(10,7),
    longitudeCandidato FLOAT(10,7),
    telResCandidato VARCHAR(12) NOT NULL,
    telCelCandidato VARCHAR(12) NOT NULL,
    nivelEscolaridade ENUM('Sem Escolaridade','Tecnico','Medio Completo','Ensino Superior','Pos Graduado'),
    PRIMARY KEY (cpfCandidato),
    INDEX (latitudeCandidato ASC),
    INDEX (longitudeCandidato ASC)
);

CREATE TABLE IF NOT exists experiencia_profissional (
    idExpProf INT AUTO_INCREMENT,
    empresa VARCHAR(50) NOT NULL,
    cargo VARCHAR(50) NOT NULL,
    cpfCandidato VARCHAR(11) NOT NULL,
    tempo INT NOT NULL,
    PRIMARY KEY (idExpProf),
    FOREIGN KEY (cpfCandidato)
        REFERENCES candidato (cpfCandidato) ON DELETE CASCADE,
    INDEX (cpfCandidato ASC)
);

CREATE TABLE IF NOT exists idioma (
    idIdioma INT AUTO_INCREMENT,
    descIdioma VARCHAR(20) NOT NULL,
    PRIMARY KEY (idIdioma),
    INDEX (descIdioma ASC)
);

CREATE TABLE IF NOT exists conhecimento (
    idConhecimento INT AUTO_INCREMENT,
    descConhecimento VARCHAR(50) NOT NULL UNIQUE,
    PRIMARY KEY (idConhecimento),
    INDEX (descConhecimento ASC)
);

CREATE TABLE IF NOT exists candidato_idioma (
    idIdioma INT AUTO_INCREMENT,
    cpfCandidato VARCHAR(11) NOT NULL,
    FOREIGN KEY (cpfCandidato)
        REFERENCES candidato (cpfCandidato) ON DELETE CASCADE,
	FOREIGN KEY (idIdioma)
        REFERENCES idioma (idIdioma)
);

CREATE TABLE IF NOT exists candidato_conhecimento (
    idConhecimento INT AUTO_INCREMENT,
    cpfCandidato VARCHAR(11) NOT NULL,
    FOREIGN KEY (cpfCandidato)
        REFERENCES candidato (cpfCandidato) ON DELETE CASCADE,
	FOREIGN KEY (idConhecimento)
        REFERENCES conhecimento (idConhecimento)
);

CREATE TABLE IF NOT EXISTS USUARIO (
	idUsuario INT AUTO_INCREMENT,
    nomeUsuario VARCHAR(200) NOT NULL,
    senhaUsuario VARCHAR(50) NOT NULL,
    emailUsuario VARCHAR(100) NOT NULL UNIQUE,
    PRIMARY KEY (idUsuario)
);

CREATE TABLE IF NOT exists vaga (
    idVaga INT AUTO_INCREMENT,
    nomeVaga VARCHAR(200) NOT NULL,
    idUsuario INT NOT NULL,
    idConhecimento INT,
    idIdiomaVaga INT,
    cepVaga VARCHAR(8) NOT NULL,
    latitudeVaga FLOAT(20,12),
    longitudeVaga FLOAT(20,12),
    nivelEscolaridade ENUM('sem escolaridade','medio completo','ensino superior','pos graduado'),
    pcdVaga INT,
    vt INT,
    PRIMARY KEY (idVaga),
    FOREIGN KEY (idUsuario)
        REFERENCES usuario (idUsuario),
    INDEX (idUsuario ASC)
);