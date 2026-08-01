import sys
from pathlib import Path
from datetime import datetime


sys.path.append(
    str(Path(__file__).resolve().parents[2])
)


from database.database_manager import get_connection



MIGRATION_BATCH_ID = (
    "BATCH-MIGRATION-20260731"
)



def create_migration_batch(cursor):

    cursor.execute(
        """
        SELECT batch_id
        FROM batches
        WHERE batch_id = ?
        """,
        (
            MIGRATION_BATCH_ID,
        )
    )


    exists = cursor.fetchone()


    if exists:

        return False



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
            MIGRATION_BATCH_ID,
            "MIGRATION",
            0,
            datetime.now().strftime(
                "%Y-%m-%d %H:%M"
            )
        )
    )


    return True




def repair_vouchers(cursor):


    cursor.execute(
        """
        SELECT COUNT(*)
        FROM vouchers
        WHERE batch_id IS NULL
        OR batch_id = ''
        """
    )


    count = cursor.fetchone()[0]


    if count == 0:

        return 0



    cursor.execute(
        """
        UPDATE vouchers

        SET batch_id = ?

        WHERE batch_id IS NULL
        OR batch_id = ''

        """,

        (
            MIGRATION_BATCH_ID,
        )
    )


    return count





def update_batch_quantity(cursor):


    cursor.execute(
        """
        SELECT COUNT(*)
        FROM vouchers
        WHERE batch_id = ?

        """,

        (
            MIGRATION_BATCH_ID,
        )
    )


    quantity = cursor.fetchone()[0]



    cursor.execute(
        """
        UPDATE batches

        SET quantity = ?

        WHERE batch_id = ?

        """,

        (
            quantity,
            MIGRATION_BATCH_ID
        )
    )



    return quantity




def main():

    print("=" * 40)
    print(" JEFF WIFI BATCH REPAIR ")
    print("=" * 40)


    connection = get_connection()

    cursor = connection.cursor()



    created = create_migration_batch(
        cursor
    )


    repaired = repair_vouchers(
        cursor
    )


    quantity = update_batch_quantity(
        cursor
    )



    connection.commit()

    connection.close()



    print()

    if created:

        print(
            "Migration batch created."
        )

    else:

        print(
            "Migration batch already exists."
        )



    print(
        f"Vouchers repaired: {repaired}"
    )


    print(
        f"Migration batch quantity: {quantity}"
    )


    print("\nRepair completed.")




if __name__ == "__main__":

    main()