# exerecicio 13
# Escreva um programa que lê o conteúdo do arquivo texto arquivo_texto.txt e imprime o seu conteúdo.
# Dica: leia a documentação da função open(...)

with open("arquivo_texto.txt", "r") as arquivo:
    conteudo = arquivo.read()

print(conteudo, end="")