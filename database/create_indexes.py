import sys
from pathlib import Path


sys.path.append(
    str(Path(__file__).resolve().parents[1])
)


from database.database_manager import get_connection



INDEXES = [

    """
    CREATE INDEX IF NOT EXISTS idx_vouchers_code
    ON vouchers(voucher_code);
    """,


    """
    CREATE INDEX IF NOT EXISTS idx_vouchers_status
    ON vouchers(status);
    """,


    """
    CREATE INDEX IF NOT EXISTS idx_vouchers_batch
    ON vouchers(batch_id);
    """,


    """
    CREATE INDEX IF NOT EXISTS idx_sales_date
    ON sales(sale_date);
    """,


    """
    CREATE INDEX IF NOT EXISTS idx_audit_created
    ON audit_log(created);
    """

]



def main():

    connection = get_connection()

    cursor = connection.cursor()


    for index in INDEXES:

        cursor.execute(index)


    connection.commit()

    connection.close()


    print(
        "Database indexes created successfully."
    )



if __name__ == "__main__":

    main()