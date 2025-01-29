import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.types import StructType, StructField, StringType, FloatType, BooleanType, ArrayType

#parâmetros
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'RAW_PATH', 'TRUSTED_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

input_path = args['RAW_PATH']
output_path = args['TRUSTED_PATH']

schema = StructType([
    StructField("imdb_id", StringType(), True),
    StructField("title", StringType(), True),
    StructField("revenue", FloatType(), True),
    StructField("budget", FloatType(), True),
    StructField("production_countries", ArrayType(StringType()), True),
    StructField("spoken_languages", ArrayType(StringType()), True),
    StructField("status", StringType(), True),
    StructField("is_sequel", BooleanType(), True), 
    StructField("collection_name", StringType(), True)
])

tmdb_df = spark.read.schema(schema).option("multiline", "true").json(input_path)
tmdb_df = tmdb_df.filter(tmdb_df.imdb_id.isNotNull())

if tmdb_df.count() > 0:
    tmdb_df.write.mode("overwrite").parquet(output_path)
    print(f"Aquivo salvo em: {output_path}")
else:
    print("Nenhum dado encontrado! O Parquet não foi gerado.")

job.commit()