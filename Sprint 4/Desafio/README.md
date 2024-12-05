# Objetivo do desafio

Praticar python com containers docker.

**Entregáveis:**

- arquivo dockerfile
- comandos utilizados para execução de container
- respostas para os questionamentos no formato markdown
- evidências (prints) da execução bem sucedida

# Etapas

### **Preparação**:

___

## 1.  Etapa I

Foi pedido para criar uma imagem docker utilizando o arquivo [carguro.py](../Desafio/etapa-1/carguru.py), que possuí um código que retorna de forma aleatória uma marca de carro da lista. Para a criação dessa imagem criei um arquivo Dockerfile: [Código da imagem](../Desafio/etapa-1/Dockerfile).

[...]

O comando FROM especifica qual a tecnologia que estará sendo usada, que nesse caso é o python 3. Utilizei a imagem oficial disponibilizada no repositório do próprio docker, porém na versão slim por ser mais leve.

```dockerfile
FROM python:3.9-slim
```


Então o comando WORKDIR que especifica qual o caminho do diretório que será realizado, que nesse caso é a etapa1 do desafio da sprint 4 mas eu usei somente o caminho relativo.

```dockerfile
WORKDIR /etapa-1
```


E então copiei o arquivo python para essa pasta de trabalho.

```dockerfile
COPY carguro.py /etapa-1
```


E por fim utilizei o comando CMD para rodar o script quando o container iniciar.

```dockerfile
CMD ["python", "carguro.py"]
```


[...]


Após isso, foi necessário contruir a imagem, para isso utilizei o próprio terminal do VS Code e rodei o comando e coloquei o mesmo nome do script python.

```shell
docker built image -t carguro-image .
```


- ![execução do comando](../Evidencias/build-carguru.png)


Para checar a imagem, utilizei o comando: docker imge ls e ela ja estava constando na lista de imagens.
- ![execução do comando](../Evidencias/imagem-carguro.png)


E então executei o comando para criar um container a partir da imagem e mantendo o mesmo nome:

```shell
docker run --name carguro-container carguro-image
```

.

- ![execução do comando](../Evidencias/container-carguro.png)



___

## 2. Etapa II
 
   #### **É possível reutilizar containers?**

Se for no caso de containers que foram *parados*, sim, para reutilizá-los só seria necessário reiniciá-los utilizando o comando:

```shell
docker start <ID ou nome do container>
```

Nesse caso, só não seria possível caso o container já tenha sido removido ou a imagem não exista mais (tenha sido excluida), então seria preciso criar um novo container.




 ___

## 3. Etapa III


    



