import sqlite3
from pathlib import Path
from contextlib import contextmanager


DATABASE_FILE = Path(
    "database/jeffwifi.db"
)



def get_connection():

    connection = sqlite3.connect(
        DATABASE_FILE,
        timeout=10
    )


    connection.execute(
        "PRAGMA foreign_keys = ON;"
    )


    connection.execute(
        "PRAGMA journal_mode = WAL;"
    )


    connection.row_factory = sqlite3.Row


    return connection




@contextmanager
def transaction():

    connection = get_connection()


    try:

        yield connection


        connection.commit()


    except Exception:

        connection.rollback()

        raise


    finally:

        connection.close()