import sys
from pathlib import Path


sys.path.append(
    str(Path(__file__).resolve().parents[2])
)


from database.database_manager import get_connection




def find_orphan_batches(cursor):

    cursor.execute(
        """
        SELECT
            b.batch_id,
            b.plan,
            b.quantity,
            b.created

        FROM batches b

        LEFT JOIN vouchers v

        ON b.batch_id = v.batch_id

        WHERE v.batch_id IS NULL

        """
    )


    return cursor.fetchall()




def delete_orphan_batches(cursor, batches):


    deleted = 0


    for batch in batches:

        batch_id = batch[0]


        cursor.execute(
            """
            DELETE FROM batches

            WHERE batch_id = ?

            """,

            (
                batch_id,
            )
        )


        deleted += cursor.rowcount


    return deleted




def main():


    print("=" * 40)
    print(" JEFF WIFI ORPHAN BATCH CLEANUP ")
    print("=" * 40)



    connection = get_connection()

    cursor = connection.cursor()



    orphan_batches = find_orphan_batches(
        cursor
    )



    if len(orphan_batches) == 0:


        print(
            "No orphan batches found."
        )


        connection.close()

        return




    print(
        "\nOrphan batches found:"
    )

    print(
        "--------------------------------"
    )



    for batch in orphan_batches:

        print(
            f"""
Batch ID: {batch[0]}
Plan: {batch[1]}
Quantity: {batch[2]}
Created: {batch[3]}
"""
        )



    print(
        f"Total orphan batches: {len(orphan_batches)}"
    )



    confirm = input(
        "\nDelete these batches? (yes/no): "
    )



    if confirm.lower() != "yes":


        print(
            "Cleanup cancelled."
        )


        connection.close()

        return




    deleted = delete_orphan_batches(
        cursor,
        orphan_batches
    )



    connection.commit()

    connection.close()



    print()

    print(
        f"Deleted batches: {deleted}"
    )


    print(
        "Cleanup completed."
    )




if __name__ == "__main__":

    main()