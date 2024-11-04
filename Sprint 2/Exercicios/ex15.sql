-- Exercício 15
-- Apresente a query para listar os códigos das vendas identificadas como deletadas. 
-- Apresente o resultado em ordem crescente.

SELECT v.cdven
FROM tbvendas v 
WHERE v.deletado = '1'
ORDER BY v.cdven ASC
