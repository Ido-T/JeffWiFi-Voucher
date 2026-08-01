import sqlite3


DATABASE_FILE = "database/jeffwifi.db"


connection = sqlite3.connect(
    DATABASE_FILE
)

cursor = connection.cursor()


cursor.execute(
    """
    SELECT
        id,
        action,
        voucher_code,
        details,
        created

    FROM audit_log

    ORDER BY id DESC

    """
)


rows = cursor.fetchall()


print("=" * 40)
print("AUDIT LOG")
print("=" * 40)


if not rows:

    print("No audit records found.")


else:

    for row in rows:

        print()

        print(
            "ID:",
            row[0]
        )

        print(
            "Action:",
            row[1]
        )

        print(
            "Voucher:",
            row[2]
        )

        print(
            "Details:",
            row[3]
        )

        print(
            "Created:",
            row[4]
        )


connection.close()