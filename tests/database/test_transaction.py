import sys
from pathlib import Path


sys.path.append(
    str(Path(__file__).resolve().parents[2])
)


from database.database_manager import transaction



def main():

    print("=" * 40)
    print("TRANSACTION TEST")
    print("=" * 40)



    try:

        with transaction() as connection:

            cursor = connection.cursor()


            cursor.execute(
                "SELECT COUNT(*) FROM vouchers"
            )


            count = cursor.fetchone()[0]


            print(
                f"Voucher count: {count}"
            )


        print(
            "Transaction completed successfully."
        )


    except Exception as error:

        print(
            "Transaction failed:"
        )

        print(error)



if __name__ == "__main__":

    main()