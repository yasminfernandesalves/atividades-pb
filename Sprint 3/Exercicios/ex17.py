# exerecicio 17
# Escreva uma função que recebe como parâmetro uma lista e retorna 3 listas: a lista recebida dividida em 3 partes iguais. 
# Teste sua implementação com a lista abaixo
# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

def dividir_lista(lista):
    parte = len(lista) // 3
    parte1 = lista[:parte]
    parte2 = lista[parte:parte*2]
    parte3 = lista[parte*2:] 
    return parte1, parte2, parte3

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
parte1, parte2, parte3 = dividir_lista(lista)
print(parte1, parte2, parte3)