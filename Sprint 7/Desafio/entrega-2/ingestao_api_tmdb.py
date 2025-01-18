import json
import boto3
from tmdbv3api import TMDb, Discover, Movie
from datetime import datetime
import os

tmdb = TMDb()
tmdb.api_key = os.environ.get("TMDB_API_KEY")  # variável de ambiente
tmdb.language = "en"
discover = Discover()
movie = Movie()

s3_client = boto3.client("s3")

def save_to_s3(data, bucket_name, batch_count):
    process_date = datetime.now().strftime("%Y/%m/%d")
    file_name = f"dreamworks_movies_part{batch_count}.json"
    s3_path = f"Raw/TMDB/JSON/{process_date}/{file_name}"

    try:
        s3_client.put_object(
            Bucket=bucket_name,
            Key=s3_path,
            Body=json.dumps(data, ensure_ascii=False, indent=4),
            ContentType="application/json"
        )
        print(f"Arquivo {file_name} salvo no bucket S3 em {s3_path}")
    except Exception as e:
        print(f"Erro ao salvar no S3: {e}")
        raise

def fetch_dreamworks_movies(bucket_name, batch_size=100):
    company_id = 521  # ID da DreamWorks
    page = 1
    total_fetched = 0
    batch_count = 1
    movie_details = []

    try:
        first_response = discover.discover_movies({
            "with_companies": company_id,
            "page": 1
        })

        if not hasattr(first_response, "total_pages"):
            print("Erro ao obter o número total de páginas.")
            return

        total_pages = first_response.total_pages
        print(f"Total de páginas disponíveis: {total_pages}")
    except Exception as e:
        print(f"Erro ao inicializar a busca de filmes: {e}")
        raise

    while page <= total_pages:
        try:
            response = discover.discover_movies({
                "with_companies": company_id,
                "page": page
            })

            if not response or not hasattr(response, "results"):
                print(f"Sem mais resultados ou erro na página {page}. Encerrando.")
                break

            for m in response.results:
                if not hasattr(m, "id"):
                    print(f"Item inválido na página {page}: {m}")
                    continue

                details = movie.details(m.id)
                movie_data = {
                    "imdb_id": details.imdb_id,
                    "title": details.title,
                    "revenue": details.revenue,
                    "budget": details.budget,
                    "production_countries": [country["name"] for country in details.production_countries],
                    "spoken_languages": [lang["name"] for lang in details.spoken_languages],
                    "status": details.status,
                    "is_sequel": bool(details.belongs_to_collection),
                    "collection_name": details.belongs_to_collection["name"] if details.belongs_to_collection else None
                }

                movie_details.append(movie_data)
                total_fetched += 1

                if total_fetched % batch_size == 0:
                    save_to_s3(movie_details, bucket_name, batch_count)
                    movie_details = []
                    batch_count += 1

            page += 1
        except Exception as e:
            print(f"Erro ao processar a página {page}: {e}")
            break

    if movie_details:
        save_to_s3(movie_details, bucket_name, batch_count)

def lambda_handler(event, context):
    try:
        bucket_name = os.environ.get("S3_BUCKET_NAME")
        if not bucket_name:
            raise ValueError("Erro  nas variáveis de ambiente.")

        fetch_dreamworks_movies(bucket_name, batch_size=100)
        return {
            "statusCode": 200,
            "body": json.dumps("Filmes da DreamWorks salvos no bucket com sucesso.")
        }
    except Exception as e:
        print(f"Erro na execução do Lambda: {e}")
        return {
            "statusCode": 500,
            "body": json.dumps(f"Erro: {str(e)}")
        }
