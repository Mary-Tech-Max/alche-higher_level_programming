-- 16. Shows by genre

SELECT tv_genres.name, tv_shows.title
FROM tv_genres
JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows
ON tv_show_genres.show_id = tv_shows.id
ORDER BY tv_genres.name ASC, tv_shows.title ASC;
