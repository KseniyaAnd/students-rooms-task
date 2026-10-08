SELECT Rooms.name, COUNT(Students.id)
FROM Students
LEFT JOIN Rooms
	ON Students.room_id = Rooms.id
GROUP BY Rooms.id