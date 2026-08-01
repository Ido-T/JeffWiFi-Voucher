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
            name
        FROM sqlite_master
        WHERE type = 'index'
        ORDER BY name;
        """
    )


    indexes = cursor.fetchall()


    print("=" * 40)
    print("DATABASE INDEXES")
    print("=" * 40)


    for index in indexes:

        print(
            index["name"]
        )


    connection.close()



if __name__ == "__main__":

    main()