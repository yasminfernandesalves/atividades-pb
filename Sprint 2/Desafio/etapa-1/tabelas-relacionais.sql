-- CRIAÇÃO E INSERÇÃO DE DADOS DAS TABELAS RELACIONAIS

-- Ativando o suporte para chaves estrangeiras
PRAGMA foreign_keys = ON;


-- parte 1: Criando as tabelas relacionais

CREATE TABLE IF NOT EXISTS tb_Vendedor (
   idVendedor INT PRIMARY KEY,
   nomeVendedor VARCHAR,
   sexoVendedor INT,
   estadoVendedor VARCHAR
);

CREATE TABLE IF NOT EXISTS tb_Cliente (
   idCliente INT PRIMARY KEY,
   nomeCliente VARCHAR,
   cidadeCliente VARCHAR,
   estadoCliente VARCHAR,
   paisCliente VARCHAR
);

CREATE TABLE IF NOT EXISTS tb_Combustivel (
   idCombustivel INT PRIMARY KEY,
   tipoCombustivel VARCHAR
);

CREATE TABLE IF NOT EXISTS tb_Carro (
   idCarro INT PRIMARY KEY,
   idCombustivel INT,
   kmCarro INT,
   classiCarro VARCHAR,
   marcaCarro VARCHAR,
   modeloCarro VARCHAR,
   anoCarro INT,
   FOREIGN KEY (idCombustivel) REFERENCES tb_Combustivel(idCombustivel)
);

CREATE TABLE IF NOT EXISTS fato_Locacao (
   idLocacao INT PRIMARY KEY,
   idVendedor INT,
   idCliente INT,
   idCarro INT,
   dataLocacao DATE,
   horaLocacao TIME,
   qtdLocacao INT,
   vlrLocacao FLOAT,
   dataEntrega DATE,
   horaEntrega TIME,
   FOREIGN KEY (idVendedor) REFERENCES tb_Vendedor(idVendedor),
   FOREIGN KEY (idCliente) REFERENCES tb_Cliente(idCliente),
   FOREIGN KEY (idCarro) REFERENCES tb_Carro(idCarro)
);


-- parte2: Inserindo os dados nas tabelas criadas

INSERT INTO tb_Vendedor (idVendedor, nomeVendedor, sexoVendedor, estadoVendedor)
SELECT DISTINCT idVendedor, nomeVendedor, sexoVendedor, estadoVendedor
FROM tb_locacao_antiga 
WHERE idVendedor IS NOT NULL;

INSERT INTO tb_Cliente (idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente)
SELECT DISTINCT idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente
FROM tb_locacao_antiga
WHERE idCliente IS NOT NULL;

INSERT INTO tb_Combustivel (idcombustivel, tipoCombustivel)
SELECT DISTINCT idcombustivel, tipoCombustivel
FROM tb_locacao_antiga
WHERE idcombustivel IS NOT NULL;

INSERT INTO tb_Carro (idCarro, idCombustivel, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro)
SELECT  idCarro, idcombustivel, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro
FROM tb_locacao_antiga
WHERE idCarro IS NOT NULL
  AND (idCarro, kmCarro) IN (
       SELECT idCarro, MAX(kmCarro)
       FROM tb_locacao_antiga
       GROUP BY idCarro
     );

INSERT INTO fato_Locacao (idLocacao, idVendedor, idCliente, idCarro, dataLocacao, horaLocacao, qtdLocacao, vlrLocacao, dataEntrega, horaEntrega)
SELECT  idLocacao, idVendedor, idCliente, idCarro, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega
FROM tb_locacao_antiga
WHERE idLocacao IS NOT NULL;


-- consulta das novas tabelas:

SELECT * FROM tb_Vendedor tv

SELECT * FROM tb_Cliente tc

SELECT * FROM tb_Combustivel tc

SELECT * FROM tb_Vendedor tv

SELECT * FROM fato_Locacao fl

SELECT * FROM tb_Carro tc

