--Exercício 11
--Apresente a query para listar o código e nome cliente com maior gasto na loja.
-- As colunas presentes no resultado devem ser cdcli, nmcli e gasto, 
-- esta última representando o somatório das vendas (concluídas) atribuídas ao cliente.

SELECT 
	v.cdcli,
	v.nmcli, 
	SUM(v.vrunt * v.qtd) gasto
FROM tbvendas v 
WHERE v.status = 'Concluído'
GROUP BY v.cdcli, v.nmcli
ORDER BY gasto DESC 
LIMIT 1 