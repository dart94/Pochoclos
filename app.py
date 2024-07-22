from flask import Flask, request, render_template
import requests

app = Flask(__name__)

API_KEY = 'db2d6677dbb67a0dcf89dc057129f47f'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/rated_movies')
def rated_movies():
    # Asegúrate de que la URL está en una línea continua
    url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={
        API_KEY}&language=es-ES"
    response = requests.get(url)
    image_base_url = "https://image.tmdb.org/t/p/w500"
    if response.status_code == 200:
        movies = response.json().get('results', [])
        movies_html = ''.join([
            f"<div class='movie-item'>"
            f"<img src='{image_base_url}{movie['poster_path']}' alt='Poster'>"
            f"<a href='/movie_details/{movie['id']}'>{movie['title']}</a> - "
            f"Calificación: {movie['vote_average']}</div>"
            for movie in movies if movie['poster_path']])
        return movies_html
    else:
        return '<div>No se encontraron películas calificadas.</div>'


@app.route('/rated_tv')
def rated_tv():
    # Asegúrate de que la URL está en una línea continua
    url = f"https://api.themoviedb.org/3/tv/top_rated?api_key={
        API_KEY}&language=es-ES"
    response = requests.get(url)
    image_base_url = "https://image.tmdb.org/t/p/w500"
    if response.status_code == 200:
        tv_shows = response.json().get('results', [])
        tv_shows_html = ''.join([
            f"<div class='movie-item'>"
            f"<img src='{image_base_url}{
                tv_show['poster_path']}' alt='Poster'>"
            f"<a href='/tv_details/{tv_show['id']}'>{tv_show['name']}</a> - "
            f"Calificación: {tv_show['vote_average']}</div>"
            for tv_show in tv_shows if tv_show['poster_path']])
        return tv_shows_html
    else:
        return '<div>No se encontraron series de TV calificadas.</div>'


@app.route('/search')
def search():
    query = request.args.get('query')
    movie_url = f"https://api.themoviedb.org/3/search/movie?api_key={
        API_KEY}&language=es-ES&query={query}"
    tv_url = f"https://api.themoviedb.org/3/search/tv?api_key={
        API_KEY}&language=es-ES&query={query}"

    movie_response = requests.get(movie_url)
    movies = movie_response.json().get(
        'results', []) if movie_response.status_code == 200 else []
    tv_response = requests.get(tv_url)
    tv_shows = tv_response.json().get(
        'results', []) if tv_response.status_code == 200 else []

    image_base_url = "https://image.tmdb.org/t/p/w500"

    index_html = ''.join([
        f"<div class='movie-item'><img src='{image_base_url}{
            movie['poster_path']}' alt='Poster'>"
        f"{movie['title']} (Película)</div>"
        for movie in movies if movie['poster_path']])

    index_html += ''.join([
        f"<div class='movie-item'><img src='{image_base_url}{
            tv['poster_path']}' alt='Poster'>"
        f"{tv['name']} (TV)</div>"
        for tv in tv_shows if tv['poster_path']])

    return index_html if index_html else '<div>No se encontraron resultados.</div>'


if __name__ == '__main__':
    app.run(debug=True)
