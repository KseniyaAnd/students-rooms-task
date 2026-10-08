SELECT 
	Rooms.name, 
	ROUND (
		AVG(
			EXTRACT(
				YEAR FROM AGE(CURRENT_DATE, Students.birthday)
			)
		), 
		2
	) AS avg_age
FROM Students
LEFT JOIN Rooms
	ON Students.room_id = Rooms.id
GROUP BY Rooms.id
ORDER BY avg_age ASC
LIMIT 5;
