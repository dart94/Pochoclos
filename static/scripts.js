$(document).ready(function() {
    // Variables para el menú hamburguesa
    const hamburger = $(".hamburger");
    const navMenu = $(".nav-menu");

    // Cargar películas populares automáticamente
    $.get('/popular-movies', function(data) {
        $('#popular-movies-container').html(data);
    });

    // Evento para búsqueda con "Enter"
    $('#searchQuery').on('keypress', function(e) {
        if (e.which == 13) {
            e.preventDefault();
            performSearch();
        }
    });

    // Botones para cargar contenido específico
    $('#ratedMoviesButton').click(function(e) {
        e.preventDefault();
        loadRatedMovies();
    });

    $('#ratedTVButton').click(function(e) {
        e.preventDefault();
        loadRatedTV();
    });

    $('#upcomingMoviesButton').click(function(e) {
        e.preventDefault();
        fetchUpcomingMovies();
    });

    $('#upcomingTVButton').click(function(e) {
        e.preventDefault();
        fetchUpcomingTV();
    });

    // Controles del carrusel
    $('.carousel-control-right').click(function() {
        var carousel = $('.carousel');
        carousel.animate({ scrollLeft: '+=' + carousel.width() }, 300);
    });

    $('.carousel-control-left').click(function() {
        var carousel = $('.carousel');
        carousel.animate({ scrollLeft: '-=' + carousel.width() }, 300);
    });

    // Toggle del menú tipo hamburguesa
    hamburger.click(() => {
        hamburger.toggleClass("active");
        navMenu.toggleClass("active");
    });

    // Cerrar el menú cuando se selecciona un ítem
    $(".nav-item").click(() => {
        hamburger.removeClass("active");
        navMenu.removeClass("active");
    });
});

function performSearch() {
    var query = $('#searchQuery').val();
    $.get('/search', { query: query }, function(data) {
        $('#results').html(data);
    });
}

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

function fetchUpcomingMovies() {
    $.get('/upcoming_movies', function(data) {
        $('#results').html(data);
    });
}

function fetchUpcomingTV() {
    $.get('/upcoming_tv', function(data) {
        $('#results').html(data);
    });
}


