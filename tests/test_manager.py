import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)


from voucher_manager import (
    search_voucher,
    sell_voucher,
    use_voucher
)


print("JEFF WIFI VOUCHER MANAGER")
print("------------------------")


while True:

    code = input(
        "\nEnter voucher code (or type exit): "
    )


    if code.lower() == "exit":
        break


    voucher = search_voucher(code)


    if voucher is None:

        print(
            "\nVoucher not found."
        )

        print(
            "Please enter a valid voucher code."
        )

        continue



    choice = input(
        """
Choose action:

1 - Sell voucher
2 - Mark as USED
3 - Cancel

Choose:
"""
    )


    if choice == "1":

        sell_voucher(code)


    elif choice == "2":

        use_voucher(code)


    elif choice == "3":

        print(
            "Cancelled"
        )


    else:

        print(
            "Invalid option"
        )