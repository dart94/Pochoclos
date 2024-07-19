from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

API_KEY = 'db2d6677dbb67a0dcf89dc057129f47f'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/rated_movies')
def rated_movies():
    url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={
        API_KEY}&language=es-ES"
    response = requests.get(url)
    image_base_url = "https://image.tmdb.org/t/p/w500"
    if response.status_code == 200:
        movies = response.json().get('results', [])
        movies_html = ''.join([
            f"<div class='movie-item2'><img src='{image_base_url}{movie['poster_path']}' alt='Poster' style='height:150px;'> {
                movie['title']} - Calificación: {movie['vote_average']} ({movie.get('release_date', 'Sin fecha')})</div>"
            for movie in movies if movie['poster_path']])
        return movies_html
    else:
        return '<div>No se encontraron películas calificadas.</div>'


@app.route('/rated_tv')
def rated_tv():
    url = f"https://api.themoviedb.org/3/tv/top_rated?api_key={
        API_KEY}&language=es-ES"
    response = requests.get(url)
    image_base_url = "https://image.tmdb.org/t/p/w500"  # Base URL for images
    if response.status_code == 200:
        tv_shows = response.json().get('results', [])
        tv_shows_html = ''.join([
            f"<div class='movie-item2'><img src='{image_base_url}{tv_show['poster_path']}' alt='Poster' style='height:150px;'> {
                tv_show['name']} - Calificación: {tv_show['vote_average']} ({tv_show.get('first_air_date', 'Sin fecha')})</div>"
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

    image_base_url = "https://image.tmdb.org/t/p/w500"  # Base URL for images

    index_html = ''.join([
        f"<div class='movie-item'><img src='{image_base_url}{
            movie['poster_path']}' alt='Poster' style='height:100px;'>"
        f"{movie['title']} (Película) - <button onclick=\"loadReviews('movie', '{
            movie['id']}')\">Ver Reseñas</button></div>"
        for movie in movies if movie['poster_path']])

    index_html += ''.join([
        f"<div class='movie-item'><img src='{image_base_url}{
            tv['poster_path']}' alt='Poster' style='height:100px;'>"
        f"{tv['name']} (TV) - <button onclick=\"loadReviews('tv', '{tv['id']
                                                                    }')\">Ver Reseñas</button></div>"
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
    if media_type == "movie":
        url = f"https://api.themoviedb.org/3/movie/{
            media_id}/reviews?api_key={API_KEY}&language=es-ES"
    else:
        url = f"https://api.themoviedb.org/3/tv/{
            media_id}/reviews?api_key={API_KEY}&language=es-ES"

    response = requests.get(url)
    if response.status_code == 200:
        reviews = response.json().get('results', [])
        reviews_html = ''.join([f"<div><strong>{
                               review['author']}</strong>: {review['content']}</div>" for review in reviews])
        return reviews_html if reviews else '<div>No se encontraron reseñas.</div>'
    else:
        return '<div>Error al cargar reseñas.</div>'


@app.route('/popular-movies')
def popular_movies():
    url = f"https://api.themoviedb.org/3/movie/popular?api_key={
        API_KEY}&language=es-ES"
    response = requests.get(url)
    movies = response.json().get('results', [])
    return jsonify(movies)  # Devuelve los datos como JSON


if __name__ == '__main__':
    app.run(debug=True)
