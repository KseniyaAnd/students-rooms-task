
import psycopg

from app.models import Room, Student


class BDDataInsertor:
    """Insert data into the database."""

    def insert_students(
        self,
        connection: psycopg.Connection,
        students: list[Student],
    ) -> None:
        """Insert student records into the database.
        
        :param connection: Active database connection.
        :param students: List of student records.
        :return: None.
        """

        with connection.cursor() as cursor:
            for student in students:
                cursor.execute(
                    """
                    INSERT INTO Students (id, name, birthday, room_id, sex)
                    VALUES (%s, %s, %s, %s, %s)
                    """,
                    (
                        student.student_id,
                        student.name,
                        student.birthday,
                        student.room_id,
                        student.sex,
                    ),
                )

        connection.commit()

    def insert_rooms(
        self,
        connection: psycopg.Connection,
        rooms: list[Room],
    ) -> None:
        """Insert room records into the database.
        
        :param connection: Active database connection.
        :param rooms: List of room records.
        :return: None.
        """

        with connection.cursor() as cursor:
            for room in rooms:
                cursor.execute(
                    """
                    INSERT INTO Rooms (id, name)
                    VALUES (%s, %s)
                    """,
                    (room.id, room.name),
                )

        connection.commit()