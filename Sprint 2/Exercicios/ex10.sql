--Exercício 10
--A comissão de um vendedor é definida a partir de um percentual sobre o total de vendas (quantidade * valor unitário) por ele realizado. O percentual de comissão de cada vendedor está armazenado na coluna perccomissao, tabela tbvendedor. 

-- Com base em tais informações, calcule a comissão de todos os vendedores, considerando todas as vendas armazenadas na base de dados com status concluído.

-- As colunas presentes no resultado devem ser vendedor, valor_total_vendas e comissao. O valor de comissão deve ser apresentado em ordem decrescente arredondado na segunda casa decimal.

SELECT 
    v.cdvdd AS vendedor, 
    SUM(v.qtd * v.vrunt) AS valor_total_vendas,
    ROUND(SUM(v.qtd * v.vrunt) * ven.perccomissao / 100, 2) AS comissao
FROM tbvendas v
JOIN tbvendedor ven ON v.cdvdd = ven.cdvdd 
WHERE v.status = 'Concluído'
GROUP BY v.cdvdd, ven.perccomissao
ORDER BY comissao DESC