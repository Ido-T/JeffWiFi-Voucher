from config import PLANS
from database.database_manager import get_connection
from voucher_manager import sell_voucher
from printer import print_voucher_receipt

reserved_codes = []



def count_available_vouchers(plan_name):

    connection = get_connection()

    cursor = connection.cursor()


    cursor.execute(
        """
        SELECT COUNT(*)

        FROM vouchers

        WHERE plan = ?

        AND status = 'AVAILABLE'

        """,
        (
            plan_name,
        )
    )


    count = cursor.fetchone()[0]


    connection.close()


    return count




def get_available_vouchers(
    plan_name,
    quantity,
    reserved_codes
):

    connection = get_connection()

    cursor = connection.cursor()


    placeholders = ""

    params = [
        plan_name
    ]


    if reserved_codes:

        placeholders = ",".join(
            ["?"] * len(reserved_codes)
        )


        cursor.execute(
            f"""
            SELECT voucher_code

            FROM vouchers

            WHERE plan = ?

            AND status = 'AVAILABLE'

            AND voucher_code NOT IN ({placeholders})

            ORDER BY id

            LIMIT ?

            """,
            params +
            reserved_codes +
            [quantity]
        )


    else:

        cursor.execute(
            """
            SELECT voucher_code

            FROM vouchers

            WHERE plan = ?

            AND status = 'AVAILABLE'

            ORDER BY id

            LIMIT ?

            """,
            (
                plan_name,
                quantity
            )
        )


    rows = cursor.fetchall()


    connection.close()


    return [
        row["voucher_code"]
        for row in rows
    ]





def display_order(order):

    print("\n")
    print("=" * 35)
    print("CURRENT ORDER")
    print("=" * 35)


    total = 0


    for item in order:

        print()

        print(
            f"{item['plan']} x{item['quantity']}"
        )


        print("\nCodes:")


        for code in item["codes"]:

            print(code)



        print()


        print(
            f"Subtotal: {item['subtotal']} Gdes"
        )


        total += item["subtotal"]



    print()


    print(
        "-" * 35
    )


    print(
        "TOTAL:",
        total,
        "Gdes"
    )


    print(
        "=" * 35
    )


    return total





print("=" * 35)
print("       JEFF WIFI SALES")
print("=" * 35)



order = []



while True:


    print("\nAVAILABLE PLANS\n")


    for key, plan in PLANS.items():

        available = count_available_vouchers(
            plan["name"]
        )


        print(
            f"{key}. {plan['name']}"
        )


        print(
            f"   Available: {available}"
        )


        print(
            f"   Price: {plan['price']} Gdes\n"
        )



    print("5. Checkout")
    print("6. Cancel Order")


    choice = input(
        "Choose plan: "
    ).strip()



    if choice == "5":

        break



    if choice == "6":

        print(
            "\nOrder cancelled."
        )

        order = []

        continue



    if choice not in PLANS:

        print(
            "\nInvalid selection."
        )

        continue



    selected_plan = PLANS[choice]



    quantity = input(
        "Quantity: "
    ).strip()



    try:

        quantity = int(quantity)


    except ValueError:

        print(
            "Invalid quantity."
        )

        continue




    available = count_available_vouchers(
        selected_plan["name"]
    )



    if quantity > available:

        print(
            "\nNot enough vouchers available."
        )

        print(
            "Available:",
            available
        )

        print(
            "Requested:",
            quantity
        )

        continue




    codes = get_available_vouchers(
    selected_plan["name"],
    quantity,
    reserved_codes
)


    item = {

        "plan": selected_plan["name"],

        "quantity": quantity,

        "codes": codes,

        "subtotal":
            quantity *
            selected_plan["price"]

    }


    existing = None


    for old_item in order:

        if old_item["plan"] == selected_plan["name"]:

            existing = old_item

            break



    if existing:

        existing["quantity"] += quantity

        existing["codes"].extend(
            codes
        )

        existing["subtotal"] += (
            quantity *
            selected_plan["price"]
        )


    else:

        order.append(item)



    reserved_codes.extend(
        codes
    )




    print(
        "\nAdded:"
    )


    print(
        f"{selected_plan['name']} x{quantity}"
    )



    display_order(
        order
    )



    add_more = input(
        "\nAdd another plan? (y/n): "
    ).lower()



    if add_more != "y":

        break




if not order:


    print(
        "\nNo order created."
    )


    exit()



total = display_order(
    order
)



confirm = input(
    "\nConfirm sale? (y/n): "
).lower()



if confirm != "y":


    print(
        "\nSale cancelled."
    )


    exit()




sold_items = []



for item in order:


    for code in item["codes"]:


        sell_voucher(
            code
        )



    sold_items.append(
        item
    )




receipt = print_voucher_receipt(
    sold_items,
    total,
    payment_method="CASH"
)



print("\n")
print("=" * 35)
print("      SALE COMPLETED")
print("=" * 35)


print(
    "Total:",
    total,
    "Gdes"
)


print(
    "Receipt:",
    receipt
)


print(
    "\nGive receipt to customer."
)