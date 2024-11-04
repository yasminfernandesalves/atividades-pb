--Exercício 14
-- Apresente a query para listar o gasto médio por estado da federação. 
-- As colunas presentes no resultado devem ser estado e gastomedio. 
-- Considere apresentar a coluna gastomedio arredondada na segunda casa decimal e ordenado de forma decrescente.
-- Observação: Apenas vendas com status concluído.

SELECT 
	v.estado,
	ROUND(AVG(v.vrunt * v.qtd), 2) AS gastomedio
FROM tbvendas v
WHERE v.status = 'Concluído'
GROUP BY v.estado 
ORDER BY gastomedio DESC 