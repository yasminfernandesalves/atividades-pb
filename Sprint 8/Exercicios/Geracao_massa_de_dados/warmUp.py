import random

#  gerar lista contendo 250 inteiros obtidos de forma aleatória e inverter a ordem deles
numeros_int = [random.randint(1, 10000) for _ in range(250)]
numeros_int.reverse()
print(numeros_int)



# gerar uma lista contendo o nome de 20 animais, ordenar em ordem crescente e itere sobre os itens, imprimindo um a um
# armazer o resultado em arq de texto, um item em cada linha, format csv
animais = ["gato", "cachorro", "leão", "tigre", "elefante", "girafa", "urso", "panda", "zebra", "macaco", 
"jacaré", "tartaruga", "cavalo", "coelho", "lobo", "raposa", "foca", "ornitorrinco", "pinguim", "cervo"]

animais.sort()
[print(animal) for animal in animais]

with open("warmup_animais.csv", "w") as file:
    file.write("\n".join(animais))