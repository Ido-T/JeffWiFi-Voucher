import sys
from pathlib import Path


sys.path.append(
    str(Path(__file__).resolve().parents[2])
)


from database.voucher_repository import voucher_exists
from database.database_manager import get_connection



def main():

    print("=" * 45)
    print(" VOUCHER DATABASE UNIQUENESS TEST ")
    print("=" * 45)



    connection = get_connection()

    cursor = connection.cursor()



    cursor.execute(
        """
        SELECT voucher_code

        FROM vouchers

        LIMIT 1

        """
    )


    existing = cursor.fetchone()


    connection.close()



    if not existing:

        print(
            "Database has no vouchers to test."
        )

        return



    existing_code = existing["voucher_code"]



    print(
        "\nTesting existing voucher:"
    )

    print(
        existing_code
    )


    result = voucher_exists(
        existing_code
    )


    if result:

        print(
            "✓ Existing voucher detected correctly."
        )

    else:

        print(
            "❌ FAIL: Existing voucher was not detected."
        )



    print(
        "\nTesting fake voucher:"
    )


    fake_code = "2H-FAKE999"



    result = voucher_exists(
        fake_code
    )


    print(
        fake_code
    )


    if not result:

        print(
            "✓ Non-existing voucher handled correctly."
        )

    else:

        print(
            "❌ FAIL: Fake voucher detected."
        )



    print(
        "\nTest completed."
    )



if __name__ == "__main__":

    main()