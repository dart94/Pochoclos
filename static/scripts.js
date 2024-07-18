$(document).ready(function() {
    $('#searchButton').click(function(e) {
        e.preventDefault();
        var query = $('#searchQuery').val();
        $.get('/search', { query: query }, function(data) {
            $('#results').html(data);
        });
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
