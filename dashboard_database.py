import sqlite3

from database.database_manager import get_connection



def get_all_vouchers():

    connection = get_connection()

    cursor = connection.cursor()


    cursor.execute(
        """
        SELECT *

        FROM vouchers

        """
    )


    rows = cursor.fetchall()


    connection.close()


    return rows

def get_status_summary():

    connection = get_connection()

    cursor = connection.cursor()


    cursor.execute(
        """
        SELECT
            status,
            COUNT(*)

        FROM vouchers

        GROUP BY status

        """
    )


    rows = cursor.fetchall()


    connection.close()


    summary = {

        "AVAILABLE": 0,
        "SOLD": 0,
        "USED": 0

    }


    for status, count in rows:

        summary[status] = count


    return summary

def get_plan_summary():

    connection = get_connection()

    cursor = connection.cursor()


    cursor.execute(
        """
        SELECT
            plan,
            status,
            COUNT(*)

        FROM vouchers

        GROUP BY plan, status

        """
    )


    rows = cursor.fetchall()


    connection.close()



    summary = {}



    for plan, status, count in rows:


        if plan not in summary:

            summary[plan] = {

                "AVAILABLE": 0,
                "SOLD": 0,
                "USED": 0

            }


        summary[plan][status] = count



    return summary

def get_sales_summary():

    connection = get_connection()

    cursor = connection.cursor()


    cursor.execute(
        """
        SELECT
            COUNT(*),
            COALESCE(
                SUM(amount),
                0
            )

        FROM sales

        """
    )


    row = cursor.fetchone()


    connection.close()


    return row


def get_revenue_by_plan():

    connection = get_connection()

    cursor = connection.cursor()


    cursor.execute(
        """
        SELECT
            plan,
            COUNT(*),
            COALESCE(
                SUM(amount),
                0
            )

        FROM sales

        GROUP BY plan

        """
    )


    rows = cursor.fetchall()


    connection.close()



    revenue = {}


    for plan, sold, amount in rows:

        revenue[plan] = {

            "sold": sold,

            "revenue": amount

        }


    return revenue

def get_stock_value():

    connection = get_connection()

    cursor = connection.cursor()


    cursor.execute(
        """
        SELECT

            plan,

            COUNT(*),

            SUM(price)


        FROM vouchers


        WHERE status = 'AVAILABLE'


        GROUP BY plan

        """
    )


    rows = cursor.fetchall()


    connection.close()



    stock = {}


    total_value = 0



    for plan, quantity, value in rows:


        if value is None:

            value = 0


        stock[plan] = {

            "quantity": quantity,

            "value": value

        }


        total_value += value



    return stock, total_value


def get_last_batch():

    connection = get_connection()

    cursor = connection.cursor()


    cursor.execute(
        """
        SELECT

            batch_id,
            plan,
            quantity,
            created

        FROM batches

        ORDER BY id DESC

        LIMIT 1

        """
    )


    row = cursor.fetchone()


    connection.close()


    if row:

        return {

            "Batch ID": row[0],

            "Plan": row[1],

            "Quantity": row[2],

            "Created": row[3]

        }


    return None


def get_integrity_check():

    problems = []


    connection = get_connection()

    cursor = connection.cursor()



    # ==================================
    # Duplicate voucher check
    # ==================================

    cursor.execute(
        """
        SELECT
            voucher_code,
            COUNT(*)

        FROM vouchers

        GROUP BY voucher_code

        HAVING COUNT(*) > 1

        """
    )


    duplicates = cursor.fetchall()


    for voucher, count in duplicates:

        problems.append(
            f"Duplicate voucher: {voucher}"
        )



    # ==================================
    # Status validation
    # ==================================

    cursor.execute(
        """
        SELECT

            voucher_code,
            status,
            sold_date,
            used_date,
            price,
            sold_amount

        FROM vouchers

        """
    )


    vouchers = cursor.fetchall()



    for row in vouchers:

        voucher = row[0]
        status = row[1]
        sold = row[2]
        used = row[3]
        price = row[4]
        sold_amount = row[5]



        # AVAILABLE validation

        if status == "AVAILABLE":

            if sold or used:

                problems.append(
                    f"{voucher}: AVAILABLE voucher has dates"
                )



        # SOLD validation

        elif status == "SOLD":

            if not sold:

                problems.append(
                    f"{voucher}: SOLD voucher missing Sold Date"
                )


            if used:

                problems.append(
                    f"{voucher}: SOLD voucher already has Used Date"
                )



        # USED validation

        elif status == "USED":

            if not sold:

                problems.append(
                    f"{voucher}: USED voucher missing Sold Date"
                )


            if not used:

                problems.append(
                    f"{voucher}: USED voucher missing Used Date"
                )



        # Financial validation

        if price is None:

            problems.append(
                f"{voucher}: Missing price"
            )



        if status in ["SOLD", "USED"]:

            if sold_amount is None:

                problems.append(
                    f"{voucher}: {status} voucher missing Sold Amount"
                )



    connection.close()


    return problems