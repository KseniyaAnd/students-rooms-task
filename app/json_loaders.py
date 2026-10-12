import json
from datetime import date
from pathlib import Path

from app.models import Room, Student


class JsonDataLoader:
    """Load students and rooms from JSON files."""

    def _read_json(
        self,
        file_path: str | Path,
    ) -> list[dict]:
        """Read data from a JSON file.
        
        :param file_path: Path to the JSON file.
        :return: A list of dictionaries containing the data.
        :rtype: list[dict]
        """

        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    def load_students(
        self,
        file_path: str | Path,
    ) -> list[Student]:
        """Load students from a JSON file.
        
        :param file_path: Path to the JSON file containing student data.
        :return: A list of Student objects.
        :rtype: list[Student]
        """

        data = self._read_json(file_path)
        students: list[Student] = []

        for item in data:
            student = Student(
                student_id=item["id"],
                birthday=date.fromisoformat(item["birthday"][:10]),
                name=item["name"],
                room_id=item["room"],
                sex=item["sex"],
            )
            students.append(student)

        return students

    def load_rooms(
        self,
        file_path: str | Path,
    ) -> list[Room]:
        """Load rooms from a JSON file.
        
        :param file_path: Path to the JSON file containing room data.
        :return: A list of Room objects.
        :rtype: list[Room]"""

        data = self._read_json(file_path)
        rooms: list[Room] = []

        for item in data:
            room = Room(
                id=item["id"],
                name=item["name"],
            )
            rooms.append(room)

        return rooms