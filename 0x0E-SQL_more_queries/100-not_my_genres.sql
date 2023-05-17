-- Prints records with column values in a set from intersection of multiple tables
SELECT DISTINCT name
    FROM tv_genres
    WHERE name NOT IN
    (
        SELECT a.name
            FROM tv_genres a
            INNER JOIN tv_show_genres b
                ON a.id = b.genre_id
            INNER JOIN tv_shows c
                ON c.id = b.show_id
            WHERE c.title = 'Dexter'
    )
    ORDER BY name ASC;
