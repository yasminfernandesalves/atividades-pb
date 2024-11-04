--Exercício 12
--Apresente a query para listar código, nome e data de nascimento dos dependentes do vendedor com menor valor total bruto em vendas (não sendo zero). As colunas presentes no resultado devem ser cddep, nmdep, dtnasc e valor_total_vendas.
--Observação: Apenas vendas com status concluído.

SELECT 
    d.cddep, 
    d.nmdep, 
    d.dtnasc,
    SUM(v.qtd * v.vrunt) AS valor_total_vendas
FROM tbdependente d
INNER JOIN tbvendedor ven ON d.cdvdd = ven.cdvdd 
INNER JOIN tbvendas v ON ven.cdvdd = v.cdvdd 
WHERE v.status = 'Concluído'
GROUP BY d.cddep, d.nmdep, d.dtnasc
HAVING SUM(v.qtd * v.vrunt) > 0
ORDER BY valor_total_vendas ASC
LIMIT 1