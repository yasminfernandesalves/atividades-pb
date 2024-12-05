import hashlib

while True:
    entrada = input("Digite una string para mascarar ou 'sair' para encerrar: ")
    if entrada.lower() == 'sair':
        print("Encerrando o programa...", flush=True)
        break

# gerando o hash da str
    hash_obj = hashlib.sha1(entrada.encode())
    hash_hex = hash_obj.hexdigest()
    print (f"Hash SAH-1: {hash_hex}", flush=True)
