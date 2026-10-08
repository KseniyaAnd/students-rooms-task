# Students and Rooms

An application for loading students and rooms data into PostgreSQL, executing SQL queries, and exporting the results to JSON or XML.

## Technologies

- Python 3
- PostgreSQL
- Psycopg 3
- SQL
- python-dotenv
- OOP
- SOLID

## Project Structure

```text
students-rooms/
├── app/
│   ├── application.py
│   ├── database.py
│   ├── exporters.py
│   ├── loaders.py
│   └── repositories.py
├── data/
│   ├── students.json
│   └── rooms.json
├── sql/
│   ├── query_1_student_count.sql
│   ├── query_2_smallest_average_age.sql
│   ├── query_3_largest_age_difference.sql
│   ├── query_4_mixed_sex_rooms.sql
│   └── indexes.sql
├── main.py
├── requirements.txt
├── .env
└── README.md
```

## Database

The application uses two related tables:

- `rooms` — contains information about rooms;
- `students` — contains information about students.

The relationship between the tables is **many-to-one**: multiple students can live in the same room.

The relationship is implemented using the foreign key `students.room_id`, which references `rooms.id`.

## SQL Queries

The application executes the following queries:

1. Get the number of students in each room.
2. Find the 5 rooms with the smallest average student age.
3. Find the 5 rooms with the largest age difference between students.
4. Find rooms where students of different sexes live together.

All calculations are performed at the database level using SQL.

## Indexes

An index is created on the foreign key used to connect students with rooms:

```sql
CREATE INDEX idx_students_room_id
ON Students(room_id);
```

This index improves the performance of searches and joins involving `students.room_id`.

Indexes for primary keys are not created manually because PostgreSQL creates them automatically.

## Installation

Create a virtual environment:

```powershell
python -m venv venv
```

Activate it:

```powershell
.\venv\Scripts\Activate.ps1
```

Install the dependencies:

```powershell
pip install -r requirements.txt
```

Create a `.env` file in the project root:

```text
DB_HOST=localhost
DB_PORT=5432
DB_NAME=students_rooms
DB_USER=postgres
DB_PASSWORD=your_password
```

## Running the Application

The application accepts paths to the students and rooms files and the required output format.

### JSON

```powershell
python main.py --students data/students.json --rooms data/rooms.json --format json
```

### XML

```powershell
python main.py --students data/students.json --rooms data/rooms.json --format xml
```

After execution, the corresponding output file is created:

```text
result.json
```

or:

```text
result.xml
```

## OOP and SOLID

The project uses an object-oriented approach.

`StudentRoomApplication` is responsible for the main application logic.

`StudentRoomRepository` is responsible for executing SQL queries.

The export functionality uses an abstract `Exporter` class with two implementations:

- `JsonExporter`;
- `XmlExporter`.

This approach makes it possible to add new export formats without changing the main application logic.

## Requirements

The project meets the following requirements:

- PostgreSQL relational database;
- many-to-one relationship between students and rooms;
- loading data from files;
- raw SQL queries without an ORM;
- calculations performed at the database level;
- database indexing;
- JSON and XML export;
- CLI parameters for input files and output format;
- OOP;
- SOLID principles.
