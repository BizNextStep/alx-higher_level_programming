-- This script lists all genres from hbtn_0d_tvshows
-- displays the number of shows linked to each.

-- Use database hbtn_0d_tvshows
USE hbtn_0d_tvshows;

-- List all genres and the number of shows linked to each genre
SELECT genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM genres
JOIN tv_show_genres ON genres.id = tv_show_genres.genre_id
GROUP BY genres.name
ORDER BY number_of_shows DESC;
