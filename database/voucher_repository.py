from database.database_manager import get_connection



def voucher_exists(voucher_code):

    connection = get_connection()

    cursor = connection.cursor()


    cursor.execute(
        """
        SELECT 1

        FROM vouchers

        WHERE voucher_code = ?

        LIMIT 1

        """,
        (
            voucher_code,
        )
    )


    result = cursor.fetchone()


    connection.close()


    return result is not None