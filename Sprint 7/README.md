
# Resumo

 O conteúdo obrigatório para esse sprint foi bem curto e informativo, porém, as informações necessárias para realizar o desafio foi bem extenso e difícil de achar.

 **Formação Spark com Pyspark** - foi um curso essencial para realizar o exercício, cobrindo todo o conteúdo desde os conceitos basicos, como a instalção e configuração no linux, data frames e RDDs, entre outros. Até a sua otimização e informações adicionais. 


[...]

# Exercícios


**Apache Spark - contador de palavras**

- [contando_palavras.py ](../Sprint%207/Exercicios/Spark/contando_palavras.py) -> código executado na linha de comando

- [resultado.txt](../Sprint%207/Exercicios/Spark/resultado.txt)  -> resultado do script printado no terminal


**TMDB**

- [extracao-dados-tmdb.py](../Sprint%207/Exercicios/TMDB/extracao-dados-tmdb.py) -> extraindo os dados do filme do shrek com a API do TMDB


**Lab AWS glue**

- [job_aws_glue_lab4.py](../Sprint%207/Exercicios/Glue/job_aws_glue_lab4.py) -> praticando no glue e cumprindo com os requisitos pedidos

- [frequencia_registro_nomes_eua.csv](../Sprint%207/Exercicios/Glue/frequencia_registro_nomes_eua.csv) -> resultado da query feita no Athena



# Evidências

Apache Spark - contador de palavras

- Realizando o pull da imagem jupyter/all-spark-notebook

    ![evi-1](../Sprint%207/Exercicios/evidencias/spark1.png)


- Lista de imagens docker

    ![evi-2](../Sprint%207/Exercicios/evidencias/spark2.png)


- Criando o container a partir da imagem e executando ele no modo interativo. (Passei o arquivo README como volume do container)

    ![evi-3](../Sprint%207/Exercicios/evidencias/spark3.png)


- Jupyter notebook com o arquivo

    ![evi-4](../Sprint%207/Exercicios/evidencias/spark4.png)


- Em outro terminal, executando o container e abrindo o powershell

    ![evi-5](../Sprint%207/Exercicios/evidencias/spark5.png)


- abrindo o terminal do Pyspark e o rodando o código para realizar a contagem das palavras do README

    ![evi-6](../Sprint%207/Exercicios/evidencias/spark6.png)



TMDB

- Resultado da execução do script:

    ![evi-1](../Sprint%207/Exercicios/evidencias/tmdb-resultado.png)


Lab AWS glue

- Criando uma função no I AM com as funções necessárias para realizar o exercício

    ![evi-1](../Sprint%207/Exercicios/evidencias/glue1.png)


- Função criada:

    ![evi-2](../Sprint%207/Exercicios/evidencias/glue2.png)


- Rodando o job do glue:

    ![evi-3](../Sprint%207/Exercicios/evidencias/glue3.png)


- Após algumas tentativas o job foi executado com sucesso

    ![evi-4](../Sprint%207/Exercicios/evidencias/glue4.png)


- Estrutura das pastas geradas com o resultado do job

    ![evi-5](../Sprint%207/Exercicios/evidencias/glue5.0.png)


- Pasta com o arquivo csv com os nomes (input)

    ![evi-5.1](../Sprint%207/Exercicios/evidencias/glue5.1.png)


- pasta de output para armazenar os resultados, dividindo em pastas com os nomes femininos e masculinos

    ![evi-5.2](../Sprint%207/Exercicios/evidencias/glue5.2.png)


- na pasta com os nomes femininos separados por ano 

    ![evi-5.3](../Sprint%207/Exercicios/evidencias/glue5.3.png)


- na pasta com os nomes masculinos separados por ano 

    ![evi-5.4](../Sprint%207/Exercicios/evidencias/glue5.4.png)


- criando um crawler

    ![evi-6](../Sprint%207/Exercicios/evidencias/glue6.0.png)


- rodando ele

    ![evi-6.1](../Sprint%207/Exercicios/evidencias/glue6.1.png)


- testando a tabela criada no Athena e realizando um select nesses dados:

    ![evi-7](../Sprint%207/Exercicios/evidencias/glue7.png)



[...]


# Certificados

N/A 

