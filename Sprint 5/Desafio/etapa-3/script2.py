# enviando o arquivo csv com os dados tratados e limpos para o bucket 'sprint5-desafio'

import boto3

# credenciais
aws_access_key_id='ASIA5MSUB57R4SY6SC2G'
aws_secret_access_key='Pymxb6+gNV4er4nLVqyDaV10RA5QGQPOBPm3FoId'
aws_session_token='IQoJb3JpZ2luX2VjEBAaCXVzLWVhc3QtMSJIMEYCIQDrWTJdL03//6oLiTbsXxV8fmNdI5p2gj4jDuzPLrwz/AIhAMA40LFtj5hLzW8TviFfnDvOhIEkv92CeiwYbjjhbKHuKqYDCNn//////////wEQABoMOTIwMzczMDMwODgzIgwFfna8lUuAT1XV2Rgq+gIGoB1y7panzyO40qgHyOzLLu0sLp6sfdc6EWapOOL2Z4MNCx/vd3xkmbpg8IKIjeuPapbx8q7tFfekIBnz4zqRyJuYY/oVfiVWQJ9DB8SLZ8BJU6wrF9fzJ+mawl0tCC+bAziztQ7yqil1wJAKuiUgqAO7USWEVDOWXvT6fOeIGCIzlxtGmsB1lXLz1TlSi5TNKdxe74WwnfmVXelNeKCN+PRjSINCdYgVhoSkNg/tuIli1UNHRxGzVulKLCwZL9blax3W5sbFodtWJTA8b1TEtwqb5ylDZEmDTCR/Jz1gSady/EHBB5p9G3sXwv8bs0XAYSPsPc8xM8SxS6FIReQ8o0dFCz2ze1uGZzodPSMFLZWX8x1MwVd38YiNsCktcbJ2QLgp6UvqBIAaFNRK+V+D/FxexMhueQrkRuOwc45pyWi35VxmKMgP8/PymhNHp3qhldnfdFHB5oR9ZfFJ6fNojx7M+mQy3wZM5pufd4VqE/DJzXpO5ahcp1kw7Y2muwY6pQHfGoU9ZK62dcGH0gbD7MnrZj/2lgKL0xzDKioCJPsOM/xOXo5xyyNwU77IlgiulsFjFm36Jr176JM9tq7M7lLR8EQC/Nf8EtWS9Li9FzW3azWKuqXGurS7d1Xhb6iDBPbfQuR0+TP/1gWaFpqH9TPUNomuPyTCXcrColxxI/b05Btau+iYwOlXNP8GsuipjYnMfza1/Uqm5rknP/v8S9Ve9PsoZyo='

# iniciando o recurso S3
s3 = boto3.resource(
    's3',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    aws_session_token=aws_session_token
)

# referenciando o bucket
bucket_nome = 'sprint5-desafio'
bucket = s3.Bucket(bucket_nome)

# upload do arquivo
arquivo_path = 'C:/Users/yasmi/Documents/trainee-repo-template/Sprint 5/Desafio/etapa-2/dados-tratados.csv'
arquivo_key = 'dados-tratados.csv'

try:
    bucket.upload_file(arquivo_path, arquivo_key)
    print("Arquivo enviado com sucesso para o bucket!")
except Exception as e:
    print("Erro ao fazer upload do arquivo.")