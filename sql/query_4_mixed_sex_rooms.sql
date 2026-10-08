SELECT 
	Rooms.name
FROM Students
LEFT JOIN Rooms
	ON Students.room_id = Rooms.id
GROUP BY Rooms.id
HAVING COUNT(DISTINCT Students.sex) > 1
