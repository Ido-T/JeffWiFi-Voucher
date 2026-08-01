import sqlite3


DATABASE_FILE = "database/jeffwifi.db"



def check_database():

    connection = sqlite3.connect(
        DATABASE_FILE
    )


    cursor = connection.cursor()


    print("=" * 40)
    print(" JEFF WIFI DATABASE CHECK")
    print("=" * 40)



    # Count vouchers

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM vouchers
        """
    )


    vouchers = cursor.fetchone()[0]


    print()

    print(
        f"Total vouchers: {vouchers}"
    )



    # Status summary

    cursor.execute(
        """
        SELECT status, COUNT(*)

        FROM vouchers

        GROUP BY status

        """
    )


    print("\nSTATUS SUMMARY")
    print("--------------------------------")


    for row in cursor.fetchall():

        print(
            f"{row[0]} : {row[1]}"
        )



    # Sales

    cursor.execute(
        """
        SELECT COUNT(*), SUM(amount)

        FROM sales

        """
    )


    sales = cursor.fetchone()


    print("\nSALES SUMMARY")
    print("--------------------------------")


    print(
        f"Sales count: {sales[0]}"
    )


    print(
        f"Revenue: {sales[1]} Gdes"
    )



    connection.close()



if __name__ == "__main__":

    check_database()