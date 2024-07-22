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

    // Cargar películas populares
    $.get('/popular-movies', function(data) {
        $('#popular-movies-container').html(data);
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

function createMovieHTML(movie) {
    return `
        <div class="movie-item">
            <img src="https://image.tmdb.org/t/p/w500${movie.poster_path}" alt="${movie.title}" style="width:100%;">
            <h2>${movie.title}</h2>
            <h3>Rating: ${movie.vote_average}</h3>
        </div>
    `;
}

function loadMovieDetails(movieId) {
    $.get(`/movie/${movieId}`, function(data) {
        const detailsContainer = $('#movie-details');
        const movieDetails = `
            <div>
                <h2>${data.title}</h2>
                <img src="https://image.tmdb.org/t/p/w500${data.poster_path}" alt="${data.title}">
                <p>${data.overview}</p>
                <p><strong>Fecha de lanzamiento:</strong> ${data.release_date}</p>
                <p><strong>Calificación:</strong> ${data.vote_average}</p>
                <p><strong>Duración:</strong> ${data.runtime} minutos</p>
                <p><strong>Géneros:</strong> ${data.genres.map(genre => genre.name).join(', ')}</p>
            </div>
        `;
        detailsContainer.html(movieDetails);
    });
}
$(document).ready(function() {
    $('.carousel-control-right').click(function() {
        var carousel = $('.carousel');
        carousel.animate({
            scrollLeft: '+=' + carousel.width()  // Ajusta según la cantidad que deseas desplazar
        }, 300);
    });

    $('.carousel-control-left').click(function() {
        var carousel = $('.carousel');
        carousel.animate({
            scrollLeft: '-=' + carousel.width()  // Ajusta según la cantidad que deseas desplazar
        }, 300);
    });
});
