import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)


# caminhos fornecidos via parâmetros
source_file = args['S3_INPUT_PATH']  
target_path = args['S3_TARGET_PATH'] 

# lógica do Job
df_dynamic = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [source_file]},
    format="csv",
    format_options={"withHeader": True, "separator": ","}
)

# conversão para DataFrame Spark
df = df_dynamic.toDF()

# transformações
df = df.withColumn("nome", upper(col("nome")))

# Estatísticas e análises (como no exemplo anterior)
# ...

# gravando no S3
target_output = target_path + "/frequencia_registro_nomes_eua"
df_dynamic_upper = DynamicFrame.fromDF(df, glueContext, "df_dynamic_upper")
glueContext.write_dynamic_frame.from_options(
    frame=df_dynamic_upper,
    connection_type="s3",
    connection_options={
        "path": target_output,
        "partitionKeys": ["sexo", "ano"]
    },
    format="json"
)


job.commit()