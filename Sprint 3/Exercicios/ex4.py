# exercício 04
# Escreva um código Python para imprimir todos os números primos entre 1 até 100. 
# Lembre-se que você deverá desenvolver o cálculo que identifica se um número é primo ou não.
# Importante: Aplique a função range().

numeros = list(range(1, 100))

for n in numeros:
    if n > 1:
        for m in range(2, n):
            if (n % m) == 0:
                break
        else:
            print(n)