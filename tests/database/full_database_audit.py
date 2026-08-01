import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parents[2])
)

from database.database_manager import get_connection


def audit_vouchers(cursor):

    print("\nVOUCHERS")
    print("--------------------------------")

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM vouchers
        """
    )

    total = cursor.fetchone()[0]

    print(
        f"Total vouchers: {total}"
    )


    # Missing batch_id

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM vouchers
        WHERE batch_id IS NULL
        OR batch_id = ''
        """
    )

    missing_batch = cursor.fetchone()[0]


    print(
        f"Missing batch ID: {missing_batch}"
    )


    # Duplicate voucher codes

    cursor.execute(
        """
        SELECT voucher_code, COUNT(*)
        FROM vouchers
        GROUP BY voucher_code
        HAVING COUNT(*) > 1
        """
    )

    duplicates = cursor.fetchall()


    print(
        f"Duplicate vouchers: {len(duplicates)}"
    )




def audit_batches(cursor):

    print("\nBATCHES")
    print("--------------------------------")


    cursor.execute(
        """
        SELECT
            batch_id,
            quantity
        FROM batches
        """
    )


    batches = cursor.fetchall()


    print(
        f"Total batches: {len(batches)}"
    )


    mismatch = 0


    for batch_id, quantity in batches:


        cursor.execute(
            """
            SELECT COUNT(*)
            FROM vouchers
            WHERE batch_id = ?
            """,
            (
                batch_id,
            )
        )


        count = cursor.fetchone()[0]


        if count != quantity:

            mismatch += 1

            print(
                f"Mismatch: {batch_id}"
            )

            print(
                f"Expected: {quantity}, Found: {count}"
            )


    print(
        f"Batch mismatches: {mismatch}"
    )




def audit_sales(cursor):

    print("\nSALES")
    print("--------------------------------")


    cursor.execute(
        """
        SELECT COUNT(*)
        FROM sales
        """
    )


    total = cursor.fetchone()[0]


    print(
        f"Total sales: {total}"
    )


    cursor.execute(
        """
        SELECT COUNT(*)
        FROM sales s
        LEFT JOIN vouchers v
        ON s.voucher_code = v.voucher_code
        WHERE v.voucher_code IS NULL
        """
    )


    orphan_sales = cursor.fetchone()[0]


    print(
        f"Orphan sales: {orphan_sales}"
    )




def audit_status(cursor):

    print("\nSTATUS")
    print("--------------------------------")


    cursor.execute(
        """
        SELECT status, COUNT(*)
        FROM vouchers
        GROUP BY status
        """
    )


    rows = cursor.fetchall()


    for status, count in rows:

        print(
            f"{status}: {count}"
        )




def main():


    print("=" * 40)
    print(" JEFF WIFI DATABASE AUDIT ")
    print("=" * 40)


    connection = get_connection()

    cursor = connection.cursor()


    audit_vouchers(cursor)

    audit_batches(cursor)

    audit_sales(cursor)

    audit_status(cursor)


    connection.close()


    print("\n================================")
    print("AUDIT COMPLETED")
    print("================================")



if __name__ == "__main__":

    main()