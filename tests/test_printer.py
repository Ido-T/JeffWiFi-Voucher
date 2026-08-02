import sys
from pathlib import Path


sys.path.append(
    str(Path(__file__).resolve().parents[1])
)


from printer import print_voucher_receipt



# Simulate a real customer order:
#
# Customer buys:
#
# 3 x 2 HOURS
# 3 x 4 HOURS
# 1 x 24 HOURS


order_items = [

    {
        "plan": "2 HOURS",
        "quantity": 3,
        "codes": [
            "2H-Z4nB4i",
            "2H-A8kL2m",
            "2H-P7xQ9d"
        ],
        "subtotal": 75
    },


    {
        "plan": "4 HOURS",
        "quantity": 3,
        "codes": [
            "4H-B5vF5h",
            "4H-C2mN8s",
            "4H-K9wR4t"
        ],
        "subtotal": 150
    },


    {
        "plan": "24 HOURS",
        "quantity": 1,
        "codes": [
            "24H-X8pL2z"
        ],
        "subtotal": 100
    }

]



total = 325



receipt = print_voucher_receipt(
    order_items,
    total,
    payment_method="CASH"
)



print(
    "Receipt created:"
)

print(receipt)