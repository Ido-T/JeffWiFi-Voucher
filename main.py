from pathlib import Path
from datetime import datetime

from config import PLANS
from generator import generate_vouchers
from inventory import add_vouchers_to_inventory
from exporter import save_import_file



print("=" * 35)
print("      JEFF WIFI MANAGER")
print("=" * 35)
print()



for key, value in PLANS.items():

    print(
        f"{key} - {value['name']}"
    )



while True:

    choice = input(
        "\nChoose plan: "
    )


    if choice in PLANS:

        break


    print(
        "\nInvalid selection."
    )

    print(
        "Please choose one of the available options."
    )


while True:

    try:

        quantity = int(
            input(
                "Number of vouchers: "
            )
        )


        if quantity > 0:

            break


        print(
            "Quantity must be greater than zero."
        )


    except ValueError:

        print(
            "Please enter a valid number."
        )



plan = PLANS[choice]



batch_id = (
    "BATCH-"
    +
    datetime.now().strftime(
        "%Y%m%d-%H%M%S"
    )
)



vouchers = generate_vouchers(
    plan["prefix"],
    quantity
)






# ==========================
# Save to SQLite database
# ==========================


inventory_result = add_vouchers_to_inventory(
    vouchers,
    plan["name"],
    batch_id,
    plan["price"]
)

# ==========================
# Create voucher text file
# ==========================


voucher_folder = Path(
    "vouchers"
)

voucher_folder.mkdir(
    exist_ok=True
)



voucher_file = (
    voucher_folder
    /
    (
        plan["name"].replace(
            " ",
            "_"
        )
        +
        "_"
        +
        datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )
        +
        ".txt"
    )
)



with open(
    voucher_file,
    "w",
    encoding="utf-8"
) as file:


    file.write(
        "JEFF WIFI\n"
    )


    file.write(
        f"PLAN: {plan['name']}\n\n"
    )


    for voucher in vouchers:

        file.write(
            voucher + "\n"
        )


# ==========================
# MikroTik export
# ==========================


import_file = save_import_file(
    vouchers,
    plan["profile"],
    plan["limit_uptime"]
)



print("\nDone!\n")


print(
    "Voucher file:"
)

print(
    voucher_file
)


print(
    "\nDatabase:"
)

print(
    "database/jeffwifi.db"
)


print(
    "\nBatch ID:"
)

print(
    batch_id
)


print(
    "\nMikroTik Import:"
)

print(
    import_file
)