import sqlite3
from pathlib import Path


DATABASE_FILE = Path(
    "database/jeffwifi.db"
)



def create_database():

    DATABASE_FILE.parent.mkdir(
        exist_ok=True
    )


    connection = sqlite3.connect(
        DATABASE_FILE
    )


    cursor = connection.cursor()



    # ==========================
    # VOUCHERS TABLE
    # ==========================

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS vouchers (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            voucher_code TEXT UNIQUE NOT NULL,

            plan TEXT NOT NULL,

            status TEXT NOT NULL,

            created_date TEXT NOT NULL,

            sold_date TEXT,

            used_date TEXT,

            batch_id TEXT,

            price INTEGER,

            sold_amount INTEGER

        )
        """
    )



    # ==========================
    # BATCHES TABLE
    # ==========================

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS batches (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            batch_id TEXT UNIQUE NOT NULL,

            plan TEXT NOT NULL,

            quantity INTEGER NOT NULL,

            created TEXT NOT NULL

        )
        """
    )



    # ==========================
    # SALES TABLE
    # ==========================

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS sales (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            voucher_code TEXT NOT NULL,

            plan TEXT NOT NULL,

            amount INTEGER NOT NULL,

            sale_date TEXT NOT NULL

        )
        """
    )



    # ==========================
    # AUDIT LOG TABLE
    # ==========================

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS audit_log (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            action TEXT NOT NULL,

            voucher_code TEXT,

            details TEXT,

            created TEXT NOT NULL

        )
        """
    )



    connection.commit()

    connection.close()



    print(
        "JeffWiFi database created successfully."
    )

    print(
        DATABASE_FILE
    )




if __name__ == "__main__":

    create_database()