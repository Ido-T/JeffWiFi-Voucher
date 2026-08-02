from pathlib import Path
from datetime import datetime


RECEIPT_FOLDER = Path("receipts")


def print_voucher_receipt(
    order_items,
    total,
    payment_method="CASH"
):

    RECEIPT_FOLDER.mkdir(
        exist_ok=True
    )


    filename = (
        RECEIPT_FOLDER /
        (
            "receipt_"
            +
            datetime.now().strftime(
                "%Y%m%d_%H%M%S"
            )
            +
            ".txt"
        )
    )


    lines = []


    lines.append(
        "================================"
    )

    lines.append(
        "          JEFF WIFI"
    )

    lines.append(
        "================================"
    )

    lines.append("")

    lines.append(
        "        WIFI VOUCHERS"
    )

    lines.append("")


    for item in order_items:

        lines.append(
            f"{item['plan']} x{item['quantity']}"
        )

        lines.append("")

        lines.append(
            "Voucher Codes:"
        )

        lines.append(
            "--------------------------------"
        )


        for code in item["codes"]:

            lines.append(
                "  " + code
            )


        lines.append(
            "--------------------------------"
        )

        lines.append("")

        lines.append(
            f"Subtotal: {item['subtotal']} Gdes"
        )

        lines.append("")



    lines.append(
        "--------------------------------"
    )


    lines.append(
        f"TOTAL: {total} Gdes"
    )


    lines.append(
        f"PAYMENT: {payment_method}"
    )


    lines.append(
        "DATE: "
        +
        datetime.now().strftime(
            "%Y-%m-%d %H:%M"
        )
    )


    lines.append("")

    lines.append(
        "HOW TO CONNECT:"
    )

    lines.append(
        "1. Connect to JeffWiFi"
    )

    lines.append(
        "2. Open your browser"
    )

    lines.append(
        "3. Enter your voucher code"
    )


    lines.append(
        "Keep this receipt."
    )


    lines.append("")

    lines.append(
        "--------------------------------"
    )

    lines.append(
        "SUPPORT:"
    )

    lines.append(
        "WhatsApp: +509 4733-0044"
    )

    lines.append(
        "--------------------------------"
    )

    lines.append("")

    lines.append(
        "Thank you!"
    )


    lines.append(
        "================================"
    )



    receipt = "\n".join(lines)



    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(receipt)



    return filename