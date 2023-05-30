import json
import requests


API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkOTBmYzliYjY4M2RmYTAxNWMyYTY0MWEzZmJhYTM0NiIsInN1YiI6IjY0NzE0MDY1ZGQ3MzFiMDBmYWU5ZDY1OSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.dhhwD7QHWOFKrExQQOerRR97dVRDCqbsnMkhGLqkpx4"
api_key = "d90fc9bb683dfa015c2a641a3fbaa346"

def get_popular_movies(list_type):
    endpoint = f'https://api.themoviedb.org/3/movie/{list_type}'
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

#У файлі tbdb_client.py визнач нову функцію під назвою get_poster_url. Нехай функція приймає шлях до плаката та розмір як параметр. Встанови значення за замовчуванням на w342. Нехай функція повертає повну URL-адресу зображення
def get_poster_url(poster_api_path, size="w342"):
    base_url = 'https://image.tmdb.org/t/p/'
    return f'{base_url}{size}/{poster_api_path}'


def get_movies(how_many, list_type):
    data = get_popular_movies(list_type)
    return data["results"][:how_many]

#визначимо там нову функцію get_single_movie(movie_id). 
#Вона працюватиме дуже подібно до того, який повертає нам список фільмів: нам також потрібно зробити запит GET і додати заголовок авторизації, що містить наш ключ API. Єдиною відмінністю буде URL-адреса, яку ми запитуватимемо.
def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

#функція повертає акторський склад для вибраного фільму
def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()["cast"]

def get_movies_list(list_type):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()

def get_single_movie_images(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()