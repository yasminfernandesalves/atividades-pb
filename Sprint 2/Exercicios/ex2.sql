--Exercício 02
--Apresente a query para listar os 10 livros mais caros. 
--Ordenar as linhas pela coluna valor, em ordem decrescente.  
--Atenção às colunas esperadas no resultado final:  titulo, valor.

SELECT 
    titulo, 
    valor 
FROM livro l 
ORDER BY valor DESC 
LIMIT 10


