# EXERCÍCIO ETL

#  lendo o arquivo
def ler_csv(caminho_csv):
    with open(caminho_csv, "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
    cabecalho = linhas[0].strip().split(',')
    dados = [linha.strip().split(',') for linha in linhas[1:]]
    return cabecalho, dados


# Função para salvar o conteúdo em um arquivo .txt
def salvar_em_txt(nome_arquivo, conteudo):
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        arquivo.write(conteudo)


# Etapas:

def executar_etl(caminho_csv):
    cabecalho, dados = ler_csv(caminho_csv)


  # 1 -> Ator/Atriz com maior número de filmes
    try:
        filmes_validos = [
            linha for linha in dados
            if linha[2].strip().replace('.', '').replace(',', '').isdigit()
        ]
        maior_filmes = max(
            filmes_validos,
            key=lambda x: int(float(x[2].strip().replace(',', '')))
        )
        etapa1 = f"O ator/atriz com maior número de filmes é {maior_filmes[0]}, com {int(float(maior_filmes[2].strip()))} filmes."
    except ValueError as e:
        etapa1 = f"Erro ao processar a etapa 1: {e}"
    salvar_em_txt('etapa1.txt', etapa1)


    # 2 -> Média da receita de bilheteria dos principais filmes
    try:
        valores_gross = [
            float(x[5].strip().replace(',', '').replace(' ', ''))
            for x in dados if x[5].strip().replace(',', '').replace(' ', '').replace('.', '').isdigit()
        ]
        media_gross = sum(valores_gross) / len(valores_gross)
        etapa2 = f"A média da receita de bilheteria dos principais filmes é {media_gross:.2f} milhões de dólares."
    except Exception as e:
        etapa2 = f"Erro ao calcular a média na etapa 2: {e}"
    salvar_em_txt('etapa2.txt', etapa2)


    # 3 -> Ator/Atriz com maior média de receita por filme
    try:
        media_valida = [
            linha for linha in dados if linha[3].strip().replace(',', '').replace('.', '').isdigit()
        ]
        maior_media = max(
            media_valida,
            key=lambda x: float(x[3].strip().replace(',', '').replace(' ', ''))
        )
        etapa3 = f"O ator/atriz com maior média de receita por filme é {maior_media[0]}, com média de {float(maior_media[3].strip()):.2f} milhões de dólares."
    except ValueError as e:
        etapa3 = f"Erro ao processar a etapa 3: {e}"
    salvar_em_txt('etapa3.txt', etapa3)


    # 4 -> Contagem de filmes na coluna #1 MOVIE
    try:
        filmes = {}
        for linha in dados:
            filme = linha[4].strip()
            filmes[filme] = filmes.get(filme, 0) + 1
        filmes_ordenados = sorted(filmes.items(), key=lambda x: (-x[1], x[0]))
        etapa4 = "\n".join(
            f"{i+1} - O filme {filme} aparece {qtd} vez(es) no dataset."
            for i, (filme, qtd) in enumerate(filmes_ordenados)
        )
    except Exception as e:
        etapa4 = f"Erro ao processar a etapa 4: {e}"
    salvar_em_txt('etapa4.txt', etapa4)


    # 5 -> Atores ordenados por receita total bruta
    try:
        atores_validos = [
            linha for linha in dados if linha[1].strip().replace(',', '').replace('.', '').isdigit()
        ]
        atores_ordenados = sorted(
            atores_validos,
            key=lambda x: -float(x[1].strip().replace(',', '').replace(' ', ''))
        )
        etapa5 = "\n".join(
            f"{ator[0]} - {float(ator[1].strip()):.2f} milhões de dólares"
            for ator in atores_ordenados
        )
    except ValueError as e:
        etapa5 = f"Erro ao processar a etapa 5: {e}"
    salvar_em_txt('etapa5.txt', etapa5)

    print("Processo ETL concluído. Resultados salvos nos arquivos .txt!")


# executando o ETL:

caminho = r"C:/Users/yasmi/Desktop/CompassUol/Sprint03/actors.csv"

if __name__ == "__main__":
    executar_etl(caminho)