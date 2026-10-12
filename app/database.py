import os

import psycopg
from dotenv import load_dotenv

load_dotenv()


def get_connection() -> psycopg.Connection:
    """Create a connection to the PostgreSQL database.

    Database connection settings are loaded from environment variables.

    :return: An active PostgreSQL database connection.
    :rtype: psycopg.Connection
    """

    return psycopg.connect(
        host= os.environ["DB_HOST"],
        port= int(os.environ["DB_PORT"]),
        dbname= os.environ["DB_NAME"],
        user= os.environ["DB_USER"],
        password= os.environ["DB_PASSWORD"],
    )
