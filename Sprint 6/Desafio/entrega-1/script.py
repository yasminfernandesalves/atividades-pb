import boto3
import os
from datetime import datetime

print("Iniciando o script...")

# variáveis de ambiente
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_SESSION_TOKEN = os.getenv("AWS_SESSION_TOKEN")

# iniciando cliente do S3
s3_client = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    aws_session_token=AWS_SESSION_TOKEN
)

# criando o bucket
bucket_name = 'desafio.final-yasmin.alves'
try:
    s3_client.head_bucket(Bucket=bucket_name)
    print(f"Bucket {bucket_name} já existe.")
except:
    s3_client.create_bucket(Bucket=bucket_name)
    print(f"Bucket {bucket_name} criado com sucesso.")

# local dos arquivos
arquivos = {
    "movies.csv": "/entrega-1/dados/movies.csv",
    "series.csv": "/entrega-1/dados/series.csv"
}

# data de processamento
data = datetime.now().strftime("%Y/%m/%d")

# upload dos arquivos CSV para o S3
for nome_arquivo, caminho_local in arquivos.items():
    tipo_dado = nome_arquivo.split(".")[0].capitalize()  
    caminho_s3 = f"Raw/Local/CSV/{tipo_dado}/{data}/{nome_arquivo}"

    try:
        s3_client.upload_file(caminho_local, bucket_name, caminho_s3)
        print(f"Arquivo '{nome_arquivo}' carregado com sucesso para '{caminho_s3}'.")
    except Exception as e:
        print(f"Erro ao carregar '{nome_arquivo}': {e}")