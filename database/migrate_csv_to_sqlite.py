import sqlite3
import csv
from pathlib import Path


DATABASE_FILE = Path(
    "database/jeffwifi.db"
)


INVENTORY_FILE = Path(
    "inventory/master_inventory.csv"
)


BATCH_FILE = Path(
    "inventory/batch_history.csv"
)



def migrate_vouchers(connection):

    if not INVENTORY_FILE.exists():

        print(
            "Inventory file not found."
        )

        return


    cursor = connection.cursor()


    with open(
        INVENTORY_FILE,
        "r",
        newline="",
        encoding="utf-8"
    ) as file:


        reader = csv.DictReader(file)


        count = 0


        for row in reader:


            cursor.execute(
                """
                INSERT OR IGNORE INTO vouchers
                (
                    voucher_code,
                    plan,
                    status,
                    created_date,
                    sold_date,
                    used_date,
                    batch_id,
                    price,
                    sold_amount
                )

                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)

                """,

                (

                    row["Voucher"],

                    row["Plan"],

                    row["Status"],

                    row["Created"],

                    row["Sold Date"],

                    row["Used Date"],

                    row["Batch ID"],

                    row["Price"],

                    row["Sold Amount"]

                )

            )


            count += 1



    print(
        f"Vouchers migrated: {count}"
    )




def migrate_batches(connection):


    if not BATCH_FILE.exists():

        print(
            "Batch history file not found."
        )

        return



    cursor = connection.cursor()



    with open(
        BATCH_FILE,
        "r",
        newline="",
        encoding="utf-8"
    ) as file:


        reader = csv.DictReader(file)


        count = 0


        for row in reader:


            cursor.execute(
                """
                INSERT OR IGNORE INTO batches
                (
                    batch_id,
                    plan,
                    quantity,
                    created
                )

                VALUES (?, ?, ?, ?)

                """,

                (

                    row["Batch ID"],

                    row["Plan"],

                    row["Quantity"],

                    row["Created"]

                )

            )


            count += 1



    print(
        f"Batches migrated: {count}"
    )




def migrate_sales(connection):


    cursor = connection.cursor()


    cursor.execute(
        """
        SELECT
            voucher_code,
            plan,
            sold_amount,
            sold_date

        FROM vouchers

        WHERE status IN ('SOLD','USED')

        """
    )


    rows = cursor.fetchall()


    count = 0


    for row in rows:


        cursor.execute(
            """
            INSERT INTO sales
            (
                voucher_code,
                plan,
                amount,
                sale_date
            )

            VALUES (?, ?, ?, ?)

            """,

            (

                row[0],

                row[1],

                row[2],

                row[3]

            )

        )


        count += 1



    print(
        f"Sales migrated: {count}"
    )




def main():


    connection = sqlite3.connect(
        DATABASE_FILE
    )


    print(
        "Starting migration..."
    )


    migrate_vouchers(
        connection
    )


    migrate_batches(
        connection
    )


    migrate_sales(
        connection
    )


    connection.commit()


    connection.close()


    print(
        "Migration completed successfully."
    )



if __name__ == "__main__":

    main()