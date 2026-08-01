import sqlite3


DATABASE_FILE = "database/jeffwifi.db"


connection = sqlite3.connect(
    DATABASE_FILE
)

cursor = connection.cursor()


cursor.execute(
    """
    SELECT name
    FROM sqlite_master
    WHERE type='table'
    """
)


print("=" * 40)
print("DATABASE TABLES")
print("=" * 40)


for table in cursor.fetchall():

    print(
        table[0]
    )


connection.close()