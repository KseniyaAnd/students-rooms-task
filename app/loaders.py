import json

def load_students(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def insert_students(connection, students):
    with connection.cursor() as cursor:
        for student in students:
            cursor.execute(
                """
                INSERT INTO Students (id, name, birthday, room_id, sex) 
                VALUES (%s, %s, %s, %s, %s)
                """,
                (student["id"], student["name"], student["birthday"], student["room"], student["sex"]),
            )
    connection.commit()

def load_rooms(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def insert_rooms(connection, rooms):
    with connection.cursor() as cursor:
        for room in rooms:
            cursor.execute(
                """
                INSERT INTO Rooms (id, name) 
                VALUES (%s, %s)
                """,
                (room["id"], room["name"]),
            )
    connection.commit()