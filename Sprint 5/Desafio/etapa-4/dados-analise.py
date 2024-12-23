import boto3
import pandas as pd

# Credenciais
aws_access_key_id='ASIA5MSUB57R4SY6SC2G'
aws_secret_access_key='Pymxb6+gNV4er4nLVqyDaV10RA5QGQPOBPm3FoId'
aws_session_token='IQoJb3JpZ2luX2VjEBAaCXVzLWVhc3QtMSJIMEYCIQDrWTJdL03//6oLiTbsXxV8fmNdI5p2gj4jDuzPLrwz/AIhAMA40LFtj5hLzW8TviFfnDvOhIEkv92CeiwYbjjhbKHuKqYDCNn//////////wEQABoMOTIwMzczMDMwODgzIgwFfna8lUuAT1XV2Rgq+gIGoB1y7panzyO40qgHyOzLLu0sLp6sfdc6EWapOOL2Z4MNCx/vd3xkmbpg8IKIjeuPapbx8q7tFfekIBnz4zqRyJuYY/oVfiVWQJ9DB8SLZ8BJU6wrF9fzJ+mawl0tCC+bAziztQ7yqil1wJAKuiUgqAO7USWEVDOWXvT6fOeIGCIzlxtGmsB1lXLz1TlSi5TNKdxe74WwnfmVXelNeKCN+PRjSINCdYgVhoSkNg/tuIli1UNHRxGzVulKLCwZL9blax3W5sbFodtWJTA8b1TEtwqb5ylDZEmDTCR/Jz1gSady/EHBB5p9G3sXwv8bs0XAYSPsPc8xM8SxS6FIReQ8o0dFCz2ze1uGZzodPSMFLZWX8x1MwVd38YiNsCktcbJ2QLgp6UvqBIAaFNRK+V+D/FxexMhueQrkRuOwc45pyWi35VxmKMgP8/PymhNHp3qhldnfdFHB5oR9ZfFJ6fNojx7M+mQy3wZM5pufd4VqE/DJzXpO5ahcp1kw7Y2muwY6pQHfGoU9ZK62dcGH0gbD7MnrZj/2lgKL0xzDKioCJPsOM/xOXo5xyyNwU77IlgiulsFjFm36Jr176JM9tq7M7lLR8EQC/Nf8EtWS9Li9FzW3azWKuqXGurS7d1Xhb6iDBPbfQuR0+TP/1gWaFpqH9TPUNomuPyTCXcrColxxI/b05Btau+iYwOlXNP8GsuipjYnMfza1/Uqm5rknP/v8S9Ve9PsoZyo='

# Iniciando o cliente S3
s3_client = boto3.client(
    's3',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    aws_session_token=aws_session_token
)

bucket_name = 'sprint5-desafio'
arquivo_key = 'dados-tratados.csv' 

# Carregando o arquivo do S3
response = s3_client.get_object(Bucket=bucket_name, Key=arquivo_key)
dados = pd.read_csv(response['Body'])  

# análise dos dados: 

# Pergunta: "Qual foi o maior grupo de despesa no mês de agosto, considerando apenas despesas acima de R$2000 e cujo favorecido seja "UNIVERSIDADE FEDERAL DO PARANA", 
# constando suas subcategorias, seus gastos totais e a média geral desses gastos?"

# filtragem de agosto, despesas acima de 2000 e favorecido "UNIVERSIDADE FEDERAL DO PARANA"
dados['Data'] = pd.to_datetime(dados['Data'], format='%Y-%m-%d')
dados['Mes'] = dados['Data'].dt.month
filtro = (
    (dados['Mes'] == 8) & 
    (dados['Valor'] > 2000) & 
    (dados['Favorecido'].str.strip() == "UNIVERSIDADE FEDERAL DO PARANA")
)
dados_filtrados = dados[filtro].copy()

# adicionando uma coluna condicional
dados_filtrados.loc[:, 'Valor_Alta'] = dados_filtrados['Valor'].apply(
    lambda x: 'Alta' if x > 5000 else 'Baixa'
)

# agrupamento e agregação
resultado = (
    dados_filtrados
    .groupby(['Grupo_Despesa', 'Elemento_Despesa'], as_index=False)
    .agg(
        Total_Gasto=('Valor', 'sum'),
        Media_Gasto=('Valor', 'mean')
    )
)

# grupo com maior gasto total
grupo_maior_gasto = (
    resultado
    .groupby('Grupo_Despesa', as_index=False)
    .agg(
        Gasto_Total=('Total_Gasto', 'sum'),
        Media_Final=('Media_Gasto', 'mean')
    )
    .sort_values(by='Gasto_Total', ascending=False)
    .iloc[0]
)

# consolidando o resultado em um dataframe
grupo_nome = grupo_maior_gasto['Grupo_Despesa']
gasto_total = grupo_maior_gasto['Gasto_Total']
media_geral = grupo_maior_gasto['Media_Final']
subcategorias = ", ".join(
    f"{row['Elemento_Despesa']} (R${row['Total_Gasto']:.2f})"
    for _, row in resultado[resultado['Grupo_Despesa'] == grupo_nome].iterrows()
)

resultado_df = pd.DataFrame({
    'Maior Grupo de Despesa': [grupo_nome],
    'Gasto Total': [gasto_total],
    'Média Geral': [media_geral],
    'Subcategorias': [subcategorias]
})

# salvando o dataframe no formato CSV
csv_output = resultado_df.to_csv(index=False)


output_key = 'dados-analise.csv'
s3_client.put_object(Bucket=bucket_name, Key=output_key, Body=csv_output)

print(f"Arquivo modificado enviado para o S3 com o nome: {output_key}")