# exerecicio 16
# Escreva uma função que recebe uma string de números separados por vírgula e retorne a soma de todos eles. 
# Depois imprima a soma dos valores.
# A string deve ter valor "1,3,4,6,10,76"

def soma_numeros(string_numeros):
    numeros = map(int, string_numeros.split(","))
    return sum(numeros)

string_numeros = "1,3,4,6,10,76"
soma = soma_numeros(string_numeros)
print(soma)