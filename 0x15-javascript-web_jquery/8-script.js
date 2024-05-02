$(document).ready(function() {
    $.getJSON("https://swapi-api.alx-tools.com/api/films/?format=json", function(data) {
        $("#list_movies").append("<li>" + data.title + "</li>");
    });
});
