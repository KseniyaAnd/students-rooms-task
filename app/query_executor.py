import typing
from pathlib import Path

import psycopg


class QueryExecutor:
    """Execute SQL queries related to students and rooms."""

    def __init__(
            self, 
            connection: psycopg.Connection
        ) -> None:
        """Initialize the Query Executor.

        :param connection: Active database connection.
        :return: None.
        """

        self.connection: psycopg.Connection = connection

    def _execute_query(
            self, 
            file_name: str
        ) -> list[tuple]:
        """Execute an SQL query stored in a file.

        :param file_name: Name of the SQL file inside the ``sql`` directory.
        :return: Rows returned by the query.
        :rtype: list[tuple[Any, ...]]
        """

        sql_path: Path = Path("sql") / file_name
        query: typing.LiteralString = typing.cast(typing.LiteralString, sql_path.read_text(encoding="utf-8"))

        with self.connection.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()

    def get_student_count_by_room(self) -> list[tuple]:
        """Get the number of students in each room.

        :return: Room names and their student counts.
        :rtype: list[tuple[Any, ...]]
        """

        return self._execute_query("query_1_student_count.sql")

    def get_smallest_average_age(self) -> list[tuple]:
        """Get the five rooms with the smallest average student age.

        :return: Room names and their average student ages.
        :rtype: list[tuple[Any, ...]]
        """

        return self._execute_query("query_2_smallest_average_age.sql")

    def get_largest_age_difference(self) -> list[tuple]:
        """Get the five rooms with the largest age difference.

        :return: Room names and their age differences.
        :rtype: list[tuple[Any, ...]]
        """

        return self._execute_query("query_3_largest_age_difference.sql")

    def get_mixed_sex_rooms(self) -> list[tuple]:
        """Get rooms containing students of different sexes.

        :return: Room names and the number of distinct sexes in each room.
        :rtype: list[tuple[Any, ...]]
        """

        return self._execute_query("query_4_mixed_sex_rooms.sql")
