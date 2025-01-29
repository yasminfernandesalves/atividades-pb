import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

# parâmetros
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'RAW_PATH', 'TRUSTED_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

input_path = args['RAW_PATH']     
output_path = args['TRUSTED_PATH']   

# lendo o arquivo
df = spark.read.csv(input_path, header=True, inferSchema=True, sep='|', mode="PERMISSIVE")

num_linhas = df.count()
print(f"Número de linhas carregadas: {num_linhas}")

if num_linhas > 0:
    df.dropDuplicates().write.mode("overwrite").parquet(output_path)
    print(f"Arquivo salvo em: {output_path}")
else:
    print("Nenhum dado encontrado! O Parquet não foi gerado.")
    

job.commit()