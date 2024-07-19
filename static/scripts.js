$(document).ready(function() {
    $('#searchButton').click(function(e) {
        e.preventDefault();
        var query = $('#searchQuery').val();
        $.get('/search', { query: query }, function(data) {
            $('#results').html(data);
        });
    });

    $('#searchQuery').on('keypress', function(e) {
        if (e.which == 13) { // Enter key pressed
            $('#searchButton').click();
        }
    });

    $('#ratedMoviesButton').click(function(e) {
        e.preventDefault();
        loadRatedMovies();
    });

    $('#ratedTVButton').click(function(e) {
        e.preventDefault();
        loadRatedTV();
    });

    $('#loadReviewButton').click(function(e) {
        e.preventDefault();
        var reviewId = $('#reviewId').val();
        $.get(`/review/${reviewId}`, function(data) {
            $('#results').html(data);
        });
    });

    // Cargar películas populares
    $.get('/popular-movies', function(movies) {
        const container = $('#popular-movies');
        movies.forEach(movie => {
            container.append(createMovieHTML(movie));
        });
    });
});

function loadRatedMovies() {
    $.get('/rated_movies', function(data) {
        $('#results').html(data);
    });
}

function loadRatedTV() {
    $.get('/rated_tv', function(data) {
        $('#results').html(data);
    });
}

function loadReviews(type, id) {
    $.get(`/reviews/${type}/${id}`, function(data) {
        $('#results').html(data);
    });
}

// Función para crear HTML para cada película
function createMovieHTML(movie) {
    return `
        <div class="movie-item">
            <img src="https://image.tmdb.org/t/p/w500${movie.poster_path}" alt="${movie.title}">
            <h2>${movie.title}</h2>
            <h3>Rating: ${movie.vote_average}</h3>
        </div>`;
}

