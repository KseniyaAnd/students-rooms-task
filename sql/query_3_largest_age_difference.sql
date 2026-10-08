SELECT 
	Rooms.name, 
	MAX(
		EXTRACT(
			YEAR FROM AGE(CURRENT_DATE, Students.birthday)
		)
	) - MIN(
		EXTRACT(
			YEAR FROM AGE(CURRENT_DATE, Students.birthday)
		)
	) AS avg_diff
FROM Students
LEFT JOIN Rooms
	ON Students.room_id = Rooms.id
GROUP BY Rooms.id
ORDER BY avg_diff DESC
LIMIT 5;
