SELECT * FROM lyrics WHERE track_id IN (
    SELECT track_id FROM lyrics GROUP BY track_id ORDER BY random() LIMIT 1000
)