import argparse

from app.database import get_connection
from app.exporters import JSONExporter, XMLExporter
from app.repositories import StudentRoomRepository
from app.loaders import load_students, load_rooms

from app.application import StudentRoomApplication

def parse_arguments():
    parser =  argparse.ArgumentParser(
        description="Students and rooms database application"
    )

    parser.add_argument(
        "--students",
        required=True,
        help="Path to the students file"
    )

    parser.add_argument(
        "--rooms",
        required=True,
        help="Path to the rooms file"
    )

    parser.add_argument(
        "--format",
        choices=["json", "xml"],
        required=True,
        help="Output format"
    )

    return parser.parse_args()

def main():
    args = parse_arguments()

    rooms = load_rooms(args.rooms)
    students = load_students(args.students)

    with get_connection() as connection:
        repository = StudentRoomRepository(connection)

        if args.format == "json":
            exporter = JSONExporter()
            output_file = "result.json"
        else:
            exporter = XMLExporter()
            output_file = "result.xml"

        application = StudentRoomApplication(
            connection,
            repository,
            exporter
        )

        application.load_data(rooms, students)
        results = application.get_results()
        

        print("1. List of rooms and the number of students in each of them")
        print(results["student_count_by_room"][:5])

        print("\n2. 5 rooms with the smallest average age of students")
        print(results["smallest_average_age"])

        print("\n3. 5 rooms with the largest difference in the age of students")
        print(results["largest_age_difference"])

        print("\n4. List of rooms where different-sex students live:")
        print(results["mixed_sex_rooms"][:5])

        application.export_results(
            results,
            output_file
        )

if __name__ == "__main__":
    main()
