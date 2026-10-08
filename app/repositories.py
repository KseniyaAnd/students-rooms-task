from  pathlib import Path


class StudentRoomRepository:
    def __init__(self, connection):
        self.connection = connection

    def _execute_query(self, file_name):
        sql = Path("sql") / file_name
        sql = sql.read_text(encoding="utf-8")

        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()

    def get_student_count_by_room(self):
        return self._execute_query(
            "query_1_student_count.sql"
        )

    def get_smallest_average_age(self):
        return self._execute_query(
            "query_2_smallest_average_age.sql"
        )

    def get_largest_age_difference(self):
        return self._execute_query(
            "query_3_largest_age_difference.sql"
        )

    def get_mixed_sex_rooms(self):
        return self._execute_query(
            "query_4_mixed_sex_rooms.sql"
        )