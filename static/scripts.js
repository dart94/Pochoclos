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
        $("body").toggleClass("menu-active");
    });

    // Cerrar el menú cuando se selecciona un ítem
    $(".nav-item").click(() => {
        hamburger.removeClass("active");
        navMenu.removeClass("active");
        $("body").removeClass("menu-active");
    });

    // Evento para el botón BB-8 para cambiar a la temática Star Wars y cambiar el logo
    const bb8ToggleCheckbox = document.querySelector('.bb8-toggle__checkbox');
    
    if (bb8ToggleCheckbox) {
        bb8ToggleCheckbox.addEventListener('change', function() {
            console.log("BB-8 toggle clicked!");
            document.body.classList.toggle('star-wars-theme');

            // Cambiar el logo
            var logoImage = document.getElementById('logoImage');
            if (document.body.classList.contains('star-wars-theme')) {
                logoImage.src = '/static/img/logo2.png';  // Cambia a la imagen de Star Wars
            } else {
                logoImage.src = '/static/img/logo.png';  // Vuelve a la imagen original
            }
        });
    } else {
        console.error('BB-8 toggle checkbox not found!');
    }
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

document.getElementById('regresarBtn').addEventListener('click', function() {
    window.location.href = 'index.html'; // Cambia 'index.html' por la ruta correcta si es necesario
});
