-- Exercício 09
-- Apresente a query para listar o código e nome do produto mais vendido entre as datas de 
-- 2014-02-03 até 2018-02-02, e que estas vendas estejam com o status concluída.
-- As colunas presentes no resultado devem ser cdpro e nmpro.

SELECT 
    v.cdpro,
    v.nmpro
FROM tbvendas v
JOIN tbestoqueproduto t ON v.cdpro = t.cdpro
WHERE 
    v.status = 'Concluído'
    AND v.dtven BETWEEN '2014-02-03' AND '2018-02-02'
GROUP BY v.cdpro, v.nmpro
ORDER BY COUNT(v.cdpro) DESC
LIMIT 1
