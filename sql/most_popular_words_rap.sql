SELECT l.word, SUM(l.count) AS count
FROM songs s JOIN lyrics l
ON s.track_id = l.track_id
WHERE s.genre = 'Rap'
GROUP BY l.word
ORDER BY word;