from app.exporters import rows_to_dicts


class StudentRoomApplication:

    def __init__(self, connection, repository, exporter):
        self.connection = connection
        self.repository = repository
        self.exporter = exporter


    def load_data(self, rooms, students):
        from app.loaders import insert_rooms, insert_students

        insert_rooms(self.connection, rooms)
        insert_students(self.connection, students)

    def get_results(self):
        result_1 = rows_to_dicts(
            self.repository.get_student_count_by_room(),
            ["name", "student_count"]
        )

        result_2 = rows_to_dicts(
            self.repository.get_smallest_average_age(),
            ["name", "avg_age"]
        )

        result_3 = rows_to_dicts(
            self.repository.get_largest_age_difference(),
            ["name", "age_diff"]
        )

        result_4 = rows_to_dicts(
            self.repository.get_mixed_sex_rooms(),
            ["name", "sex_count"]
        )

        return {
            "student_count_by_room": result_1,
            "smallest_average_age": result_2,
            "largest_age_difference": result_3,
            "mixed_sex_rooms": result_4
        }

    def export_results(self, results, file_path):
        self.exporter.export(results, file_path)