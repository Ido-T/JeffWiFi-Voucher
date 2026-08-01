from datetime import datetime

from database.database_manager import get_connection



def add_vouchers_to_inventory(
    vouchers,
    plan_name,
    batch_id,
    price
):

    connection = get_connection()

    cursor = connection.cursor()


    created = datetime.now().strftime(
        "%Y-%m-%d %H:%M"
    )


    # Insert batch record

    cursor.execute(
        """
        INSERT INTO batches
        (
            batch_id,
            plan,
            quantity,
            created
        )

        VALUES (?, ?, ?, ?)

        """,

        (
            batch_id,
            plan_name,
            len(vouchers),
            created
        )
    )



    # Insert vouchers

    for voucher in vouchers:


        cursor.execute(
            """
            INSERT INTO vouchers
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

                voucher,

                plan_name,

                "AVAILABLE",

                created,

                "",

                "",

                batch_id,

                price,

                ""

            )

        )


    connection.commit()

    connection.close()


    return batch_id