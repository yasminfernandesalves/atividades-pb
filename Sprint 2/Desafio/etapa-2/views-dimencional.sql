-- MODELAGEM DIMENSIONAL

-- criando views baseadas nas tabelas relacionais já criadas

CREATE VIEW dm_Cliente AS
SELECT
	idCliente,
	nomeCliente,
	cidadeCliente,
	estadoCliente,
	paisCliente
FROM tb_Cliente tc;

CREATE VIEW dm_Vendedor AS
SELECT
	idVendedor,
	nomeVendedor,
	sexoVendedor,
	estadoVendedor
FROM tb_Vendedor tv;

CREATE VIEW dm_Carro AS
SELECT 
    tc.idCarro,
    tc.kmCarro,
    tc.classiCarro,
    tc.marcaCarro, 
    tc.modeloCarro,
    tc.anoCarro,
    tc.idCombustivel, 
    combustivel.tipoCombustivel
FROM tb_Carro tc
JOIN tb_Combustivel combustivel ON tc.idCombustivel = combustivel.idCombustivel;


CREATE VIEW fato_Locacao AS
SELECT
	idLocacao,
	idVendedor,
	idCliente,
	idCarro,
	dataLocacao,
	horaLocacao,
	qtdLocacao,
	vlrLocacao,
	dataEntrega,
	horaEntrega
FROM tb_Locacao tl;


-- consultas das views criadas:
SELECT * FROM dm_Cliente

SELECT * FROM dm_Vendedor

SELECT * FROM dm_Carro dc 

SELECT * FROM fato_Locacao


-- consultas das tabelas relacionais:
SELECT * FROM tb_Carro tc 

SELECT * FROM tb_Cliente tc 

SELECT * FROM tb_Vendedor tv 

SELECT * FROM tb_Combustivel tc 

SELECT * FROM tb_Locacao tl 


