import sys
from pathlib import Path


sys.path.append(
    str(Path(__file__).resolve().parents[2])
)


from database.database_manager import get_connection



connection = get_connection()

cursor = connection.cursor()


cursor.execute(
    """
    SELECT name
    FROM sqlite_master
    WHERE type='index'
    """
)


print("=" * 40)
print("DATABASE INDEXES")
print("=" * 40)


for row in cursor.fetchall():

    print(row["name"])


connection.close()