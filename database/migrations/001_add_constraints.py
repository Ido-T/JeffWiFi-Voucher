import sys
from pathlib import Path


sys.path.append(
    str(Path(__file__).resolve().parents[2])
)


from database.database_manager import get_connection



def migrate():

    connection = get_connection()

    cursor = connection.cursor()


    print("=" * 50)
    print(" JEFF WIFI DATABASE MIGRATION 001 ")
    print(" ADD CONSTRAINTS ")
    print("=" * 50)


    try:

        # Enable foreign keys

        cursor.execute(
            "PRAGMA foreign_keys = ON;"
        )


        print("\nCreating protected tables...")


        # -----------------------------
        # BATCHES
        # -----------------------------

        cursor.execute(
            """
            CREATE TABLE batches_new (

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                batch_id TEXT UNIQUE NOT NULL,

                plan TEXT NOT NULL,

                quantity INTEGER NOT NULL
                CHECK(quantity >= 0),

                created TEXT NOT NULL

            );
            """
        )



        # -----------------------------
        # VOUCHERS
        # -----------------------------

        cursor.execute(
            """
            CREATE TABLE vouchers_new (

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                voucher_code TEXT UNIQUE NOT NULL,

                plan TEXT NOT NULL,

                status TEXT NOT NULL
                CHECK(
                    status IN
                    (
                        'AVAILABLE',
                        'SOLD',
                        'USED'
                    )
                ),

                created_date TEXT NOT NULL,

                sold_date TEXT,

                used_date TEXT,


                batch_id TEXT NOT NULL,


                price INTEGER
                CHECK(
                    price IS NULL
                    OR price >= 0
                ),


                sold_amount INTEGER
                CHECK(
                    sold_amount IS NULL
                    OR sold_amount >= 0
                ),


                FOREIGN KEY(batch_id)
                REFERENCES batches_new(batch_id)

            );
            """
        )



        # -----------------------------
        # SALES
        # -----------------------------

        cursor.execute(
            """
            CREATE TABLE sales_new (

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                voucher_code TEXT NOT NULL,

                plan TEXT NOT NULL,

                amount INTEGER NOT NULL
                CHECK(amount >= 0),

                sale_date TEXT NOT NULL,


                FOREIGN KEY(voucher_code)
                REFERENCES vouchers_new(voucher_code)

            );
            """
        )



        print("Copying data...")


        # Copy batches

        cursor.execute(
            """
            INSERT INTO batches_new
            SELECT *
            FROM batches;
            """
        )


        # Copy vouchers

        cursor.execute(
            """
            INSERT INTO vouchers_new
            SELECT *
            FROM vouchers;
            """
        )


        # Copy sales

        cursor.execute(
            """
            INSERT INTO sales_new
            SELECT *
            FROM sales;
            """
        )


        print("Replacing old tables...")


        cursor.execute(
            """
            DROP TABLE sales;
            """
        )


        cursor.execute(
            """
            DROP TABLE vouchers;
            """
        )


        cursor.execute(
            """
            DROP TABLE batches;
            """
        )


        cursor.execute(
            """
            ALTER TABLE batches_new
            RENAME TO batches;
            """
        )


        cursor.execute(
            """
            ALTER TABLE vouchers_new
            RENAME TO vouchers;
            """
        )


        cursor.execute(
            """
            ALTER TABLE sales_new
            RENAME TO sales;
            """
        )


        connection.commit()


        print()
        print("Migration completed successfully.")



    except Exception as error:


        connection.rollback()


        print()
        print("Migration failed.")
        print(error)


        raise



    finally:

        connection.close()




if __name__ == "__main__":

    migrate()