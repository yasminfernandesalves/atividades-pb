--Exercício 06
--Apresente a query para listar o autor com maior número de livros publicados. 
--O resultado deve conter apenas as colunas codautor, nome, quantidade_publicacoes.

SELECT 
    a.codautor, 
    a.nome, 
    COUNT(l.cod) AS quantidade_publicacoes
FROM autor a
INNER JOIN livro l ON a.codautor = l.autor 
GROUP BY a.codautor, a.nome
ORDER BY COUNT(l.cod) DESC
LIMIT 1