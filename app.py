from flask import Flask, request, render_template
import requests
from dotenv import load_dotenv
import os

load_dotenv()  # Carga las variables de entorno desde '.env'

app = Flask(__name__)

API_KEY = os.getenv('API_KEY')  # Obtiene la API key de las variables de entorno

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rated_movies')
def rated_movies():
    url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={API_KEY}&language=es-ES"
    response = requests.get(url)
    image_base_url = "https://image.tmdb.org/t/p/w500"
    if response.status_code == 200:
        movies = response.json().get('results', [])
        movies_html = ''.join([
            f"<div class='movie-item'>"
            f"<a href='/movie_details/{movie['id']}'>"
            f"<img src='{image_base_url}{movie['poster_path']}' alt='Poster'>"
            f"</a></div>"
            
            for movie in movies if movie['poster_path']])
        return movies_html
    else:
        return '<div>No se encontraron películas calificadas.</div>'

@app.route('/rated_tv')
def rated_tv():
    url = f"https://api.themoviedb.org/3/tv/top_rated?api_key={API_KEY}&language=es-ES"
    response = requests.get(url)
    image_base_url = "https://image.tmdb.org/t/p/w500"
    if response.status_code == 200:
        tv_shows = response.json().get('results', [])
        tv_shows_html = ''.join([
            f"<div class='movie-item'>"
            f"<a href='/tv_details/{tv_show['id']}'>"
            f"<img src='{image_base_url}{tv_show['poster_path']}' alt='Poster'>"
            f"</a></div>"
            
            
            for tv_show in tv_shows if tv_show['poster_path']])
        return tv_shows_html
    else:
        return '<div>No se encontraron series de TV calificadas.</div>'

@app.route('/search')
def search():
    query = request.args.get('query')
    movie_url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&language=es-ES&query={query}"
    tv_url = f"https://api.themoviedb.org/3/search/tv?api_key={API_KEY}&language=es-ES&query={query}"

    movie_response = requests.get(movie_url)
    movies = movie_response.json().get('results', []) if movie_response.status_code == 200 else []
    tv_response = requests.get(tv_url)
    tv_shows = tv_response.json().get('results', []) if tv_response.status_code == 200 else []

    image_base_url = "https://image.tmdb.org/t/p/w500"

    index_html = ''.join([
        f"<div class='movie-item'>"
        f"<a href='/movie_details/{movie['id']}'>"
        f"<img src='{image_base_url}{movie['poster_path']}' alt='Poster'>"
        f"</a></div>"
        for movie in movies if movie['poster_path']])

    index_html += ''.join([
        f"<div class='movie-item'>"
        f"<a href='/tv_details/{tv['id']}'>"
        f"<img src='{image_base_url}{tv['poster_path']}' alt='Poster'>"
        f"</a></div>"
        
        for tv in tv_shows if tv['poster_path']])

    return index_html if index_html else '<div>No se encontraron resultados.</div>'

@app.route('/review/<review_id>')
def review_details(review_id):
    url = f"https://api.themoviedb.org/3/review/{review_id}?api_key={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        review = response.json()
        review_html = f"<div><strong>Author:</strong> {review['author']}</div>" \
            f"<div><strong>Content:</strong> {review['content']}</div>"
        return review_html
    else:
        return '<div>Review not found.</div>'

@app.route('/reviews/<media_type>/<int:media_id>')
def reviews(media_type, media_id):
    url = f"https://api.themoviedb.org/3/{media_type}/{media_id}/reviews?api_key={API_KEY}&language=es-ES"
    response = requests.get(url)
    if response.status_code == 200:
        reviews = response.json().get('results', [])
        reviews_html = ''.join([f"<div><strong>{review['author']}</strong>: {review['content']}</div>" for review in reviews])
        return reviews_html if reviews else '<div>No se encontraron reseñas.</div>'
    else:
        return '<div>Error al cargar reseñas.</div>'

@app.route('/popular-movies')
def popular_movies():
    url = f"https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&language=es-ES"
    response = requests.get(url)
    image_base_url = "https://image.tmdb.org/t/p/w500"
    if response.status_code == 200:
        movies = response.json().get('results', [])
        movies_html = ''.join([
            f"<div class='movie-item'>"
            f"<a href='/movie_details/{movie['id']}'>"
            f"<img src='{image_base_url}{movie['poster_path']}' alt='Poster'>"
            f"</a></div>"
            
            
            for movie in movies if movie['poster_path']])
        return movies_html
    else:
        return '<div>No se encontraron películas calificadas.</div>'

@app.route('/movie_details/<int:movie_id>')
def movie_details(movie_id):
    movie_url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=es-ES"

    movie_response = requests.get(movie_url)
    

    if movie_response.status_code == 200:
        movie_details = movie_response.json()
        return render_template('movie_details.html', details=movie_details)
    else:
        return '<div>Error al obtener los detalles de la película.</div>'

@app.route('/tv_details/<int:tv_id>')
def tv_details(tv_id):
    tv_url = f"https://api.themoviedb.org/3/tv/{tv_id}?api_key={API_KEY}&language=es-ES"

    tv_response = requests.get(tv_url)

    if tv_response.status_code == 200:
        tv_details = tv_response.json()
        return render_template('tv_details.html', details=tv_details)
    else:
        return '<div>Error al obtener los detalles de la serie de TV.</div>'

@app.route('/upcoming_movies')
def upcoming_movies():
    url = f"https://api.themoviedb.org/3/movie/upcoming?api_key={API_KEY}&language=es-ES"
    response = requests.get(url)
    image_base_url = "https://image.tmdb.org/t/p/w500"
    if response.status_code == 200:
        movies = response.json().get('results', [])
        movies_html = ''.join([
            f"<div class='movie-item'>"
            f"<a href='/movie_details/{movie['id']}'>"
            f"<img src='{image_base_url}{movie['poster_path']}' alt='Poster de {movie['title']}'>"
            f"</a></div>"
            for movie in movies if movie['poster_path']])
        return movies_html
    else:
        return '<div>No se encontraron próximos estrenos.</div>'

@app.route('/upcoming_tv')
def upcoming_tv():
    url = f"https://api.themoviedb.org/3/tv/on_the_air?api_key={API_KEY}&language=es-ES"
    response = requests.get(url)
    image_base_url = "https://image.tmdb.org/t/p/w500"
    if response.status_code == 200:
        tv_shows = response.json().get('results', [])
        tv_shows_html = ''.join([
            f"<div class='movie-item'>"
            f"<a href='/tv_details/{tv_show['id']}'>"
            f"<img src='{image_base_url}{tv_show['poster_path']}' alt='Poster de {tv_show['name']}'>"
            f"</a></div>"
            for tv_show in tv_shows if tv_show['poster_path']])
        return tv_shows_html
    else:
        return '<div>No se encontraron series próximas a estrenar.</div>'

if __name__ == '__main__':
    app.run(debug=True)
