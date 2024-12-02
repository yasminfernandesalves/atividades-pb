# Você está recebendo um arquivo contendo 10.000 números inteiros, um em cada linha. 
# Utilizando lambdas e high order functions, apresente os 5 maiores valores pares e a soma destes.
# Você deverá aplicar as seguintes funções no exercício:
# map, filter, sorted, sum

def processa_numeros(arquivo: str):
    with open(arquivo, 'r') as f:
        numeros = map(int, f)
        pares = filter(lambda x: x % 2 == 0, numeros)
        maiores_pares = sorted(pares, reverse=True)[:5]
        soma = sum(maiores_pares)
        
        print(maiores_pares)
        print(soma)

processa_numeros('number.txt')