--Exercício 08
-- Apresente a query para listar o código e o nome do vendedor com maior número de vendas (contagem),
-- e que estas vendas estejam com o status concluída.  
-- As colunas presentes no resultado devem ser, portanto, cdvdd e nmvdd.

SELECT
    ven.cdvdd,
    ven.nmvdd
FROM tbvendedor ven
INNER JOIN tbvendas v ON ven.cdvdd = v.cdvdd
WHERE v.status = 'Concluído'
GROUP BY ven.cdvdd, ven.nmvdd
HAVING
    COUNT(*) = (
        SELECT COUNT(*)
        FROM tbvendedor ven
        INNER JOIN tbvendas v2 ON ven.cdvdd = v2.cdvdd
        WHERE v2.status = 'Concluído'
        GROUP BY ven.cdvdd
        ORDER BY COUNT(*) DESC
        LIMIT 1
    )