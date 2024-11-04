-- Exercício 13
-- Apresente a query para listar os 10 produtos menos vendidos pelos canais de E-Commerce 
-- ou Matriz (Considerar apenas vendas concluídas).  
-- As colunas presentes no resultado devem ser cdpro, nmcanalvendas, nmpro e quantidade_vendas.

SELECT 
	cdpro, 
	nmcanalvendas, 
	nmpro,
	SUM(v.qtd) AS quantidade_vendas
FROM tbvendas v 
WHERE v.status = 'Concluído' AND nmcanalvendas IN ('Ecommerce', 'Matriz')
GROUP BY v.cdpro, v.nmcanalvendas, v.nmpro
ORDER BY quantidade_vendas  
LIMIT 10