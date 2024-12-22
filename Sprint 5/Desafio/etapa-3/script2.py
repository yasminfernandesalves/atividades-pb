# enviando o arquivo csv com os dados tratados e limpos para o bucket 'sprint5-desafio'

import boto3

# credenciais
aws_access_key_id='ASIA5MSUB57RTAJHP36R'
aws_secret_access_key='TmNlOdxtxJhrA+StciiXIi0FFYnKaJPGIBtnxaMe'
aws_session_token='IQoJb3JpZ2luX2VjEMr//////////wEaCXVzLWVhc3QtMSJHMEUCIGqBlJg4b9vZzjEjHkdaTwPSe3qbPMBj/825nm3Ms6bnAiEA++0hMXALwDrwVma0+pf2SwnatA/BoUSCGw+crUeLSOcqpgMIkv//////////ARAAGgw5MjAzNzMwMzA4ODMiDHKUTDhWrhesmeixPir6AlBusjzd+S7fzfvE8eZlrCKFlNZdLgcXHK1lZgXFZSp4crm1+gO7WGNTyQHfjEBAWGXn9i3i7E3R1zRis1cbl32WidDpbeOXpezuha8lUGnGRT8Xd/ckCBpCvWhpl7T0OINUv8ThUcbfi0pyCjim9RxFIjCl4hmaCxVDDDJMSpzF3JNglmfvgz5GtSPTPEWEMwSBaSsUO0SgxYLyMz235lA/uQDZLywUErmw+IRzyMGpCwF8vOd2GSIreO/BPelQrbW100s2LVSRPgrVtJWs6WLIZB5v+KnS4KCsc1OF9ISf3WkIxHMlq5AN62+w0YcSjAnV73kbJ+rwJdnUyNXRVVT67gzt7GZz2gBrKf6eDYOh6eNVBLQQCWGpk0MoI7Rwf3Rj0nuMf9sE1A06ojHKGjCWxd5AIawhjkvvR71pjmZbIPwsgTfkpKERNlVPkk2U5ynnO9h5G6WAcKH0sNBQ+woiSgwvSozlS7DF/wLTPGa56BKoF2Yu5MYx7zDBy5a7BjqmAeRmLifj0RZa9Jqn1kJ9D8Ok31K6M2sJbisfU9D12P7q+L5OdICrp4dKPYP9omHOXS9VT+W0r7xwis+uvKOcF8vW6At2uI5GlHf3sGDeuvdSNrEoFDVTUBPK57Gno7kNrc7jlN/jhDaKQjjqDJirfPKwRxLVy2KNNNXBTc0lHvFPr+zhDOgIMOAAGDTeKIMIRbvWjueuwtk55hQqGXJcp+uL5LooZFw='

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