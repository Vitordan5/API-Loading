create database mydb;
use mydb;

CREATE TABLE IF NOT exists candidato (
    idCandidato INT AUTO_INCREMENT,
    nomeCandidato VARCHAR(100) NOT NULL,
    cpfCandidato VARCHAR(11) NOT NULL UNIQUE,
    dataNascimentoCandidato DATE NOT NULL,
    emailCandidato VARCHAR(100) NOT NULL UNIQUE,
    pcdCandidato TINYINT NOT NULL,
    cepCandidato VARCHAR(8) NOT NULL,
    latitudeCandidato FLOAT(10,7),
    longitudeCandidato FLOAT(10,7),
    telResCandidato VARCHAR(10) NOT NULL,
    telCelCandidato VARCHAR(11) NOT NULL,
    nivelEscolaridade ENUM('sem escolaridade','tecnico','medio completo','ensino superior','pos graduado'),
    PRIMARY KEY (idCandidato),
    INDEX (latitudeCandidato ASC),
    INDEX (longitudeCandidato ASC)
);

CREATE TABLE IF NOT exists experiencia_profissional (
    idExpProf INT AUTO_INCREMENT,
    empresa VARCHAR(50) NOT NULL,
    cargo VARCHAR(50) NOT NULL,
    idCandidato INT NOT NULL,
    tempo INT NOT NULL,
    PRIMARY KEY (idExpProf),
    FOREIGN KEY (idCandidato)
        REFERENCES candidato (idCandidato),
    INDEX (idCandidato ASC)
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
    idCandidato INT NOT NULL,
    FOREIGN KEY (idCandidato)
        REFERENCES candidato (idCandidato),
	FOREIGN KEY (idIdioma)
        REFERENCES idioma (idIdioma)
);

CREATE TABLE IF NOT exists candidato_conhecimento (
    idConhecimento INT AUTO_INCREMENT,
    idCandidato INT NOT NULL,
    FOREIGN KEY (idCandidato)
        REFERENCES candidato (idCandidato),
	FOREIGN KEY (idConhecimento)
        REFERENCES conhecimento (idConhecimento)
);
