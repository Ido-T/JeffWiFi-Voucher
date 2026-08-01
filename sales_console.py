from config import PLANS
from database.database_manager import get_connection
from voucher_manager import sell_voucher


def get_available_voucher(plan_name):

    connection = get_connection()

    cursor = connection.cursor()


    cursor.execute(
        """
        SELECT voucher_code

        FROM vouchers

        WHERE plan = ?

        AND status = 'AVAILABLE'

        ORDER BY id

        LIMIT 1

        """,
        (
            plan_name,
        )
    )


    row = cursor.fetchone()

    connection.close()


    if row:
        return row["voucher_code"]


    return None



print("=" * 35)
print("       JEFF WIFI SALES")
print("=" * 35)


while True:

    print("\nAVAILABLE PLANS\n")


    for key, plan in PLANS.items():

        print(
            f"{key} - {plan['name']} "
            f"({plan['price']} Gdes)"
        )


    print("5 - Exit")


    choice = input(
        "\nChoose plan: "
    )


    if choice == "5":

        break


    if choice not in PLANS:

        print(
            "Invalid selection."
        )

        continue



    plan = PLANS[choice]


    voucher = get_available_voucher(
        plan["name"]
    )


    if not voucher:

        print(
            "\nNo voucher available for this plan."
        )

        continue



    print("\nVoucher Found")
    print("----------------")
    print(
        "Code:",
        voucher
    )

    print(
        "Plan:",
        plan["name"]
    )

    print(
        "Price:",
        plan["price"],
        "Gdes"
    )


    confirm = input(
        "\nConfirm sale? (y/n): "
    )


    if confirm.lower() == "y":

        sell_voucher(
            voucher
        )


        print("\nCUSTOMER VOUCHER")
        print("----------------")
        print(
            "Voucher Code:",
            voucher
        )

        print(
            "\nInstructions:"
        )

        print(
            "1. Connect to JeffWiFi"
        )

        print(
            "2. Open browser"
        )

        print(
            "3. Enter your voucher code"
        )

        print(
            "\nThank you!"
        )


    else:

        print(
            "Sale cancelled."
        )