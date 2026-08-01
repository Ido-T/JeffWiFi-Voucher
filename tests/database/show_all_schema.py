import sys
from pathlib import Path


sys.path.append(
    str(Path(__file__).resolve().parents[2])
)


from database.database_manager import get_connection



def main():

    connection = get_connection()

    cursor = connection.cursor()


    cursor.execute(
        """
        SELECT
            name,
            sql

        FROM sqlite_master

        WHERE type='table'

        ORDER BY name;
        """
    )


    tables = cursor.fetchall()


    print("=" * 50)
    print("DATABASE SCHEMA")
    print("=" * 50)


    for table in tables:

        print("\n")
        print("TABLE:", table["name"])
        print("--------------------------------")

        print(
            table["sql"]
        )


    connection.close()



if __name__ == "__main__":

    main()