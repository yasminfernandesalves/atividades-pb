-- Exercício 07
-- Apresente a query para listar o nome dos autores com nenhuma publicação. 
-- Apresentá-los em ordem crescente.

SELECT a.nome 
FROM autor a 
LEFT JOIN livro l ON a.codautor = l.autor 
WHERE l.autor IS NULL 
ORDER BY a.nome ASC 