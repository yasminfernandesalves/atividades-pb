-- Exercício 16
-- Apresente a query para listar a quantidade média vendida de cada produto agrupado por estado da federação. 
-- As colunas presentes no resultado devem ser estado e nmprod e quantidade_media. 
-- Considere arredondar o valor da coluna quantidade_media na quarta casa decimal. 
-- Ordene os resultados pelo estado (1º) e nome do produto (2º).
-- Obs: Somente vendas concluídas.

SELECT 
	v.estado, 
	v.nmpro,
	ROUND(AVG(v.qtd), 4) as quantidade_media
FROM tbvendas v 
WHERE v.status = 'Concluído'
GROUP BY v.estado, v.nmpro 
ORDER BY v.estado, v.nmpro 