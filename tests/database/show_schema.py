import sqlite3


connection = sqlite3.connect(
    "database/jeffwifi.db"
)

cursor = connection.cursor()


cursor.execute(
    """
    SELECT sql
    FROM sqlite_master
    WHERE type='table'
    AND name='audit_log'
    """
)


print(
    cursor.fetchone()[0]
)


connection.close()