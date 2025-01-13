import boto3
import os
from datetime import datetime

# credenciais AWS
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_SESSION_TOKEN = os.getenv("AWS_SESSION_TOKEN")

# iniciando cliente s3
s3_client = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    aws_session_token=AWS_SESSION_TOKEN
)

# referenciando meu data lake
bucket_nome = 'desafio.final-yasmin.alves'
bucket = s3_client.Bucket(bucket_nome)

# data de processamento
data = datetime.now().strftime("%Y/%m/%d")

# upload (??)
for nome_arquivo, caminho_local in arquivos.items():
    caminho_s3 = f"Raw/TMDB/JSON/{data}/{nome_arquivo}"

    try:
        s3_client.upload_file(caminho_local, bucket_nome, caminho_s3)
        print(f"Arquivo '{nome_arquivo}' carregado com sucesso para '{caminho_s3}'.")
    except Exception as e:
        print(f"Erro ao carregar '{nome_arquivo}': {e}")