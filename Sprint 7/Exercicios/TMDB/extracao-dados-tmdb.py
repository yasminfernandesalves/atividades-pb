import requests
import pandas as pd
from dotenv import load_dotenv
import os
from IPython.display import display

# carregando as variáveis do arquivo .env e lendo a chave da api dentro dele
load_dotenv()
api_key = os.getenv("TMDB_API_KEY")

# termo de busca
query = "Shrek"

# URL para a pesquisa
url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={query}&language=pt-BR"

# fazendo requisição para a API
response = requests.get(url)
data = response.json()

# lista para armazenar os dados dos filmes
filmes = []

# processando os resultados retornados pela API
if "results" in data:
    for movie in data['results']:
        df = {
            'Título': movie['title'],
            'Data de Lançamento': movie['release_date'],
            'Sinopse': movie['overview'],
            'Quantidade de Votos': movie['vote_count'],
            'Média de Votos': movie['vote_average']
        }
        filmes.append(df)

# criando um DataFrame com os dados coletados
df = pd.DataFrame(filmes)

display(df)
