from voucher_manager import search_voucher, sell_voucher


print("=" * 35)
print("       JEFF WIFI SALES")
print("=" * 35)


while True:

    print("\n")

    voucher_code = input(
        "Enter voucher code (or type exit): "
    ).strip()


    if voucher_code.lower() in [
        "exit",
        "quit",
        "q"
    ]:

        print("\nClosing Sales Console.")

        break



    voucher = search_voucher(
        voucher_code
    )


    if not voucher:

        continue



    status = voucher[2]


    if status != "AVAILABLE":

        print("\nCannot sell this voucher.")

        print(
            "Current status:",
            status
        )

        print(
            "Only AVAILABLE vouchers can be sold."
        )

        continue



    print("\nSale Information")
    print("----------------")
    print(
        "Voucher:",
        voucher[0]
    )

    print(
        "Plan:",
        voucher[1]
    )

    print(
        "Price:",
        voucher[6],
        "Gdes"
    )


    confirm = input(
        "\nConfirm sale? (y/n): "
    )


    if confirm.lower() == "y":


        sell_voucher(
            voucher_code
        )


        print("\n")
        print("=" * 35)
        print("      CUSTOMER VOUCHER")
        print("=" * 35)


        print(
            "Voucher Code:",
            voucher[0]
        )


        print(
            "Plan:",
            voucher[1]
        )


        print(
            "Price:",
            voucher[6],
            "Gdes"
        )


        print("\nInstructions:")
        print(
            "1. Connect to JeffWiFi"
        )

        print(
            "2. Open your browser"
        )

        print(
            "3. Enter your voucher code"
        )


        print("\nThank you!")


    else:

        print(
            "\nSale cancelled."
        )