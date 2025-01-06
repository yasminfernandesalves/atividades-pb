
# Resumo

O conteúdo para essa sprint foi bem extenso e informativo, com um total de 9 cursos da AWS introduzindo serviços importantes para análise de dados.

**Noções básicas de Analytics na AWS (Parte 1 E 2)** - trouxe os principais conceitos de analytics, como: machine learning, Inteligência Artificial, os 5 V's de BigData, arquiteturas e os serviços da AWS que atendem isso.
- Anotações: [Notion - Fundamentos de análise na AWS [part 1 e 2]](https://www.notion.so/Fundamentos-de-an-lise-na-AWS-part-1-e-2-1689bf04327c806a966eefc44b0dfbd7?pvs=4)


**Serverless Analytics** - um video simples e objetivo que traz o poder de ferramentas como AWS IoT Analytics, Amazon Cognito, AWS Lambda e Amazon SageMaker, entre outras. Ensina como agregar, processar, armazenar e disponibilizar dados úteis.


**Introduction to Amazon Athena** - um video que apresenta o serviço Amazon Athena com uma visão geral do ambiente operacional, implementação do serviço e realizado uma demonstração da criação de um banco de dados para executar consultas SQL para validação.


**AWS Glue Getting Started** - o curso aborda seus conceitos principais e os serviços que podem ser integrado com ele, como o AWS glue data catalog, studio, databrew e notebooks interativos entre outros. Ele também traz como ele é usado para arquitetar uma solução de nuvem.
- Anotações: [Notion - AWS Glue Getting Started](https://www.notion.so/AWS-Glue-Getting-Started-16c9bf04327c80088115df41276eef4a?pvs=4)


**AWS EMR Getting Started** - aborda o onjetivo do serviço, seus beneficios, implantação, arquitetura do EMR Serverless e usando clusters.
- Anotações: [Notion - AWS EMR Getting Started](https://www.notion.so/Amazon-EMR-Getting-Started-16c9bf04327c80d1978ce4bfe1736b7a?pvs=4)


**Getting Started with Amazon Redshift** - aborda o onjetivo do serviço, seus beneficios, custos, arquitetura e como usar o serviço de uma forma detalhada.
- Anotações: [Notion - Getting Started with Amazon Redshift](https://www.notion.so/RedShift-16c9bf04327c800996dce79f5c9fee2a?pvs=4)

**Amazon QuickSight - Getting Started** - informações gerais do serviço de visualização, seus beneficios, custo e como usa-lo.


[...]

# Exercícios

**Lab AWS S3:**
-   [nomes.csv](../Sprint%206/Exercicios/lab-s3/nomes.csv)

-   [404.html](../Sprint%206/Exercicios/lab-s3/404.html)

-   [index.html](../Sprint%206/Exercicios/lab-s3/index.html)


**Lab AWS Athena:**
-    [código das queries realizadas](../Sprint%206/Exercicios/lab-athena/consultas.txt)

-   [resultado - teste do banco de dados](../Sprint%206/Exercicios/lab-athena/query_teste_meubanco.csv)

-   [resultado - nomes mais usados](../Sprint%206/Exercicios/lab-athena/resultado_nomes_mais_usados.csv)


**Lab AWS Lambda:**
-    [lambda_function.py](../Sprint%206/Exercicios/lab-lambda/lambda_function.py)

-   [Dockerfile](../Sprint%206/Exercicios/lab-lambda/Dockerfile)

-   [camada_pandas.zip](../Sprint%206/Exercicios/lab-lambda/minha-camada-pandas.zip)


[...]

# Evidências

**Lab AWS S3:**
 
- criando o bucket:

![evi](../Sprint%205/Exercicios/Evidencias/bucket-criado.png)



- site funcionando:

![evi](../Sprint%205/Exercicios/Evidencias/site-funcionando.png)


[...]


**Lab AWS Athena:** 

-   etapa 1 - criando a pasta queries e configurando ela:
    
![evi](../Sprint%206/Exercicios/evidencias/athena1.1-pasta-queries.png)


-   etapa 2 - criando banco de dados:

![evi](../Sprint%206/Exercicios/evidencias/athena2.1-bancoDados-criando.png)


-   etapa 3.1 - criando tabela a partir do arquivo "nome.csv":

![evi](../Sprint%206/Exercicios/evidencias/athena3.1-tabela-criando.png)


-   etapa 3.2 - tabela criada:

![evi](../Sprint%206/Exercicios/evidencias/athena3.2-tabela-resultado.png)

-   etapa 3.4 - testando os dados com a consulta que traz os 15 nomes em que o ano seja 1999:

![evi](../Sprint%206/Exercicios/evidencias/athena3.4-teste-dados.png)


-   etapa 3.5 - criando uma consulta que lista os 3 nomes mais usados em cada década desde o 1950 até hoje:

![evi](../Sprint%206/Exercicios/evidencias/athtena3.5-consulta-nomes.png)


[...]

**Lab AWS Lambda**:

-   etapa 1 - criando uma função:
    
![evi](../Sprint%206/Exercicios/evidencias/lambda1-criando-funcao.png)


-   etapa 2 - construindo e testando o código: 

![evi](../Sprint%206/Exercicios/evidencias/lambda2-criando-testando-cod.png)


-   etapa 3.1 - após criar o dockerfile, construi a imagem amazonlinuxpython39:
    
![evi](../Sprint%206/Exercicios/evidencias/lambda3.1-criando-imagem.png)


-   etapa 3.2 - executando e acessando o shell do container: 
    
![evi](../Sprint%206/Exercicios/evidencias/lambda3.2-executando-container.png)


-   etapa 3.3 - instalando o pandas:
    
![evi](../Sprint%206/Exercicios/evidencias/lambda3.3-install-pandas.png)


-   etapa 3.4 - campactando os arquivos em um arquivo zip:
    
![evi](../Sprint%206/Exercicios/evidencias/lambda3.4-compactando-arq.png)


-   etapa 3.5 - copiando o arquivo do container na máquina local:
    
![evi](../Sprint%206/Exercicios/evidencias/lambda3.5-copiando-arq.png)


-   etapa 3.6 - criando camada para armazenar o arquivo zip:

![evi](../Sprint%206/Exercicios/evidencias/lambda3.6-criando-camada.png)


-   etapa 4 - utilizando a camada:
    
![evi](../Sprint%206/Exercicios/evidencias/lambda4-utilizando-camada.png)


[...]


**Lab AWS - Limpeza de recursos:**

- antes da limpeza:

![evi](../Sprint%206/Exercicios/evidencias/antes-limpeza.png)

- depois da limpeza:

![evi](../Sprint%206/Exercicios/evidencias/depois-limpeza.png)


[...]

# Certificados

- [Noções básicas de Analytics na AWS – Parte 1](../Sprint%206/Certificados/certf-fundamentos-analytics-part1.pdf)

- [Noções básicas de Analytics na AWS – Parte 2](../Sprint%206/Certificados/certf-fundamentos-analytics-part2.pdf)

- [Serverless Analytics](../Sprint%206/Certificados/certf-serverless-analytics.pdf)

- [Introduction to Amazon Athena ](../Sprint%206/Certificados/certf-amazon-athena.pdf)

- [AWS Glue Getting Started](../Sprint%206/Certificados/certf-amazon-glue.pdf)

- [Amazon EMR Getting Started](../Sprint%206/Certificados/certf-amazon-emr.pdf)

- [Getting Started with Amazon Redshift](../Sprint%206/Certificados/certf-amazon-redshift.pdf)

- [Best Practices for Data Warehousing with Amazon
Redshift](../Sprint%206/Certificados/certf-warehousing-redshift.pdf)

- [Amazon QuickSight - Getting Started](../Sprint%206/Certificados/certf-amazon-quicksight.pdf)


