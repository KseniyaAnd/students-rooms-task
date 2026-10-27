import datetime


class Student:
    """
    Represents a student with an ID, name, birthday, room ID and sex.
    """

    def __init__(
            self, 
            student_id: int, 
            name: str, 
            birthday: datetime.date, 
            room_id: int, 
            sex: str
    ) -> None:
        self.student_id = student_id
        self.name = name
        self.birthday = birthday
        self.room_id = room_id
        self.sex = sex

class Room:
    """Store room data."""

    def __init__(
            self, 
            id: int,
            name: str
    ) -> None:
        self.id = id
        self.name = name