import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, row_number, lit
from pyspark.sql.types import IntegerType, DecimalType
from pyspark.sql.window import Window


args = getResolvedOptions(sys.argv, ['JOB_NAME', 'LOCAL_PATH', 'TMDB_PATH', 'REFINED_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

input_local = args['LOCAL_PATH']
input_tmdb = args['TMDB_PATH']
output_refined = args['REFINED_PATH']

local_df = spark.read.parquet(input_local).dropDuplicates(['id'])
tmdb_df = spark.read.parquet(input_tmdb)

# dimensão COLEÇÃO
window_colecao = Window.orderBy("nome_colecao")
dim_colecao = (
    tmdb_df.select(col("collection_name").alias("nome_colecao"))
    .distinct()
    .withColumn("colecao_id", row_number().over(window_colecao))
)

# unindo os datasets para consolidar as informações
filmes_filtrados = local_df.join(tmdb_df, local_df.id == tmdb_df.imdb_id, "inner")

# Dimensão TÍTULOS
window_titulos = Window.orderBy("imdb_id")
dim_titulos = (
    filmes_filtrados.select(col("id").alias("imdb_id"), col("tituloPincipal").alias("titulo"))
    .distinct()
    .withColumn("filme_id", row_number().over(window_titulos))
)

# tabela FATO
fato_filmes = (
    filmes_filtrados.join(dim_titulos, "imdb_id", "inner")
    .join(dim_colecao, filmes_filtrados.collection_name == dim_colecao.nome_colecao, "left")
    .select(
        col("filme_id"),
        col("revenue").cast(DecimalType(18, 2)).alias("receita"),
        col("budget").cast(DecimalType(18, 2)).alias("orcamento"),
        col("anoLancamento").cast("int").alias("ano_lancamento"),
        col("notaMedia").alias("nota_media"),
        col("numeroVotos").alias("numero_votos"),
        when(col("is_sequel"), 1).otherwise(0).alias("filme_continuacao"),
        col("colecao_id") 
    )
)
    
fato_filmes.write.partitionBy("ano_lancamento").parquet(f"{output_refined}/fato_filmes", mode='overwrite')
dim_titulos.write.parquet(f"{output_refined}/dim_titulos", mode='overwrite')
dim_colecao.write.parquet(f"{output_refined}/dim_colecao", mode='overwrite')

job.commit()