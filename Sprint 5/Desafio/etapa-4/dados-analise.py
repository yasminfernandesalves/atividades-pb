import boto3
import pandas as pd

# Credenciais
aws_access_key_id='ASIA5MSUB57RZ4AR6YL3'
aws_secret_access_key='o2Lw3zqTL7HaFx8f4ID0TDKC7PD6JsoYrOSEEE4Y'
aws_session_token='IQoJb3JpZ2luX2VjEPr//////////wEaCXVzLWVhc3QtMSJIMEYCIQC0IJDrIcsLdV1IV8EZ6TNinfEI3j6I9LSvZE9AouIrGAIhAOqUsy0BT4kyBrPR1SNSJ8CGGzg0nveH2MlYzpGAdIYkKqYDCMP//////////wEQABoMOTIwMzczMDMwODgzIgxy2a0DAPtZny/bUCcq+gKiUfCKC8SwnpMMJ8bTtMcnpt6Be6RavBxbXH06+pp0tUo/2ZIrNAT39Ez7aQnqJvH5tI0TCuJKTvzbpLNyVKCAUO6tmebJpYK2zCXcb6Qh0np98RTWpVHO7kClp1+NePmWY2fOLMn1tSrt4BbMS9+xltmCfy9v/pWEBcGmrqIcMTNttVHp/Gbm4Xe9FYAEXQbLpl+H2QQiYiM5V4I+Uo86b8UIFwv5ho8Xn1sG1GuXfbqRKH8shyy/piZveonCsHGWNuWQJn4m9H953v0fognb0/yvoU4yAqk6P9ndcxL9vCtTzlQDnLcmt0/+redsPrTUZzN69BWoZcvd/bzlkElHbrxm3tc0CR2NwiwWfdGI2noeRG4SrTKnCL7yhvLN1Y5TUEURl6ykJyZU4DFyTURXV0FqkM7kQoypnALMvum/+bpHxyXICpk5TwFSRpNwkWKrjK9A7yc6cEoTJ52C+d9YofSD5zv2YjdMq+RqecKN4G3lraeTdaA5MMkw3JihuwY6pQEzHWipzuEfk+YOwVVw+dD56+qUaXRfYpjexaK3wB4j1Knhr1SLRK7XFDqjhvG7+rZwABiG3eN3LFanWMSGmK+4qYrlrvRwlaNFreiUzabjP73YwHsV/mHQMOfLJj28ihtaVL4C69iMLtUNADxQ0hJa38Xa8sLy2z4ZvQkjsSDDYXnP1WjoJw1vUMhgnI636ro+Az82I9xKN0FzXzhg8yOoWWMCrRs='

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