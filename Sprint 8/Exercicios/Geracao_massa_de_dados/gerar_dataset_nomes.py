import time
import names
import random

# definindo a semente de aleatoriedade
random.seed(40)
qtd_nomes_unicos = 3000
qtd_nomes_aleatorios = 10000000

# gerando os nomes aleatórios
aux=[]
for i in range(0, qtd_nomes_unicos):
	aux.append(names.get_full_name())
print("Gerando {} nomes aleatórios".format(qtd_nomes_aleatorios))

dados=[]
for i in range(0, qtd_nomes_aleatorios):
	dados.append(random.choice(aux))
	
# salvando os nomes em um arquivo txt
with open("nomes_aleatorios.txt", "w") as file:
	file.write("\n".join(dados))
	print("Arquivo 'nomes_aleatorios.txt' gerado com sucesso.")