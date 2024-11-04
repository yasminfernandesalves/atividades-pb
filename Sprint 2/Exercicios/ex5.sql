--Exercício 05
--Apresente a query para listar o nome dos autores que publicaram livros através de editoras NÃO situadas na região sul do Brasil.
--Ordene o resultado pela coluna nome, em ordem crescente. Não podem haver nomes repetidos em seu retorno.

SELECT DISTINCT a.nome
FROM autor a
JOIN livro l ON a.codautor = l.autor
JOIN editora e ON l.editora = e.codeditora
JOIN endereco en ON e.endereco = en.codendereco
WHERE en.estado NOT IN ('RIO GRANDE DO SUL', 'PARANÁ', 'SANTA CATARINA')
ORDER BY a.nome ASC