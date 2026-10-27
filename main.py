import argparse
from pathlib import Path

from app.database import get_connection
from app.exporters import JSONExporter, XMLExporter, rows_to_dicts
from app.json_loaders import JsonDataLoader
from app.models import Room, Student
from app.query_executor import QueryExecutor


def parse_arguments() -> argparse.Namespace:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        description="Students and rooms database application"
    )

    parser.add_argument("--students", required=True, help="Path to the students file")

    parser.add_argument("--rooms", required=True, help="Path to the rooms file")

    parser.add_argument(
        "--format", choices=["json", "xml"], required=True, help="Output format"
    )

    return parser.parse_args()


def main() -> None:
    args: argparse.Namespace = parse_arguments()
    loader: JsonDataLoader = JsonDataLoader()

    students: list[Student] = loader.load_students(Path("data/students.json"))
    rooms: list[Room] = loader.load_rooms(Path("data/rooms.json"))

    with get_connection() as connection:
        QueryExecutor: QueryExecutor = QueryExecutor(connection)

        if args.format == "json":
            exporter: JSONExporter = JSONExporter()
            output_file: str = "result.json"
        else:
            exporter: XMLExporter = XMLExporter()
            output_file: str = "result.xml"


        from app.bd_data_insertors import BDDataInsertor
        
        insertor: BDDataInsertor = BDDataInsertor()
        insertor.insert_rooms(connection, rooms)
        insertor.insert_students(connection, students)
        
        result_1: list[dict[str, object]] = rows_to_dicts(
            QueryExecutor.get_student_count_by_room(),
            ["name", "student_count"],
        )

        result_2: list[dict[str, object]] = rows_to_dicts(
            QueryExecutor.get_smallest_average_age(),
            ["name", "avg_age"],
        )

        result_3: list[dict[str, object]] = rows_to_dicts(
            QueryExecutor.get_largest_age_difference(),
            ["name", "age_diff"],
        )

        result_4: list[dict[str, object]] = rows_to_dicts(
            QueryExecutor.get_mixed_sex_rooms(),
            ["name", "sex_count"],
        )

        results: dict[str, list[dict[str, object]]] = {
            "student_count_by_room": result_1,
            "smallest_average_age": result_2,
            "largest_age_difference": result_3,
            "mixed_sex_rooms": result_4,
        }

        print("1. List of rooms and the number of students in each of them")
        print(results["student_count_by_room"][:5])

        print("\n2. 5 rooms with the smallest average age of students")
        print(results["smallest_average_age"])

        print("\n3. 5 rooms with the largest difference in the age of students")
        print(results["largest_age_difference"])

        print("\n4. List of rooms where different-sex students live:")
        print(results["mixed_sex_rooms"][:5])

        exporter.export(results, output_file)


if __name__ == "__main__":
    main()
