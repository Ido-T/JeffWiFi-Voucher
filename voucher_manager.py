from datetime import datetime

from database.database_manager import get_connection, transaction

def add_audit_log(
    cursor,
    action,
    voucher_code,
    details
):

    cursor.execute(
        """
        INSERT INTO audit_log
        (
            action,
            voucher_code,
            details,
            created
        )

        VALUES (?, ?, ?, ?)

        """,

        (
            action,
            voucher_code,
            details,
            datetime.now().strftime(
                "%Y-%m-%d %H:%M"
            )
        )
    )



def search_voucher(voucher_code):

    connection = get_connection()

    cursor = connection.cursor()


    cursor.execute(
        """
        SELECT
            voucher_code,
            plan,
            status,
            created_date,
            sold_date,
            used_date,
            price,
            sold_amount

        FROM vouchers

        WHERE voucher_code = ?

        """,

        (
            voucher_code,
        )
    )


    row = cursor.fetchone()


    connection.close()



    if row:

        print("\nVoucher Found")
        print("----------------")

        print("Voucher:", row[0])
        print("Plan:", row[1])
        print("Status:", row[2])
        print("Created:", row[3])
        print("Price:", row[6], "Gdes")
        print("Sold Amount:", row[7], "Gdes")
        print("Sold Date:", row[4])
        print("Used Date:", row[5])


        return row



    print("\nVoucher not found.")

    return None



def sell_voucher(voucher_code):


    with transaction() as connection:

        cursor = connection.cursor()


        cursor.execute(
            """
            SELECT
                status,
                plan,
                price

            FROM vouchers

            WHERE voucher_code = ?

            """,
            (
                voucher_code,
            )
        )


        row = cursor.fetchone()



        if not row:

            print(
                "\nVoucher not found."
            )

            return



        status = row["status"]

        plan = row["plan"]

        price = row["price"]



        if status != "AVAILABLE":


            print(
                "\nCannot sell voucher."
            )

            print(
                "Current status:",
                status
            )

            print(
                "Only AVAILABLE vouchers can be sold."
            )

            return



        sold_date = datetime.now().strftime(
            "%Y-%m-%d %H:%M"
        )



        cursor.execute(
            """
            UPDATE vouchers

            SET

            status = 'SOLD',

            sold_date = ?,

            sold_amount = ?

            WHERE voucher_code = ?

            """,

            (
                sold_date,
                price,
                voucher_code
            )
        )



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
                voucher_code,
                plan,
                price,
                sold_date
            )
        )



        add_audit_log(
            cursor,
            "SELL_VOUCHER",
            voucher_code,
            f"Sold for {price} Gdes"
        )


    print(
        "\nVoucher successfully marked as SOLD."
    )

    print(
        "Sold Amount:",
        price,
        "Gdes"
    )







def use_voucher(voucher_code):


    with transaction() as connection:

        cursor = connection.cursor()



        cursor.execute(
            """
            SELECT
                status

            FROM vouchers

            WHERE voucher_code = ?

            """,

            (
                voucher_code,
            )
        )



        row = cursor.fetchone()



        if not row:

            print(
                "\nVoucher not found."
            )

            return



        status = row["status"]



        if status != "SOLD":


            print(
                "\nCannot mark voucher as USED."
            )

            print(
                "Current status:",
                status
            )

            print(
                "Only SOLD vouchers can become USED."
            )

            return



        used_date = datetime.now().strftime(
            "%Y-%m-%d %H:%M"
        )



        cursor.execute(
            """
            UPDATE vouchers

            SET

            status = 'USED',

            used_date = ?

            WHERE voucher_code = ?

            """,

            (
                used_date,
                voucher_code
            )
        )



        add_audit_log(
            cursor,
            "USE_VOUCHER",
            voucher_code,
            "Voucher activated"
        )



    print(
        "\nVoucher successfully marked as USED."
    )