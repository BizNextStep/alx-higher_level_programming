-- lists all shows contained in hbtn_0d_tvshows without a genre linked.

-- Use database hbtn_0d_tvshows
USE hbtn_0d_tvshows;

-- List all shows without a genre linked
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
