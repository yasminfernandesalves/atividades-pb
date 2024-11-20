# exercício 03
# Escreva um código Python para imprimir os números pares de 0 até 20 (incluso).
# Importante: Aplique a função range() em seu código.

numeros = list(range(0, 21))

for n in numeros:
    if n % 2 == 0:
        print(n)