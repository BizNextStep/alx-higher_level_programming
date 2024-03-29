-- lists all genres of the show Dexter from the hbtn_0d_tvshows database.

-- Use database hbtn_0d_tvshows
USE hbtn_0d_tvshows;

-- List all genres of the show Dexter
SELECT genres.name
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN genres ON tv_show_genres.genre_id = genres.id
WHERE tv_shows.title = 'Dexter'
ORDER BY genres.name ASC;
