from dashboard_database import (
    get_revenue_by_plan,
    get_stock_value
)


print("=" * 40)
print("REVENUE BY PLAN")
print("=" * 40)


revenue = get_revenue_by_plan()


for plan, data in revenue.items():

    print()

    print(plan)

    print(
        "Sold:",
        data["sold"]
    )

    print(
        "Revenue:",
        data["revenue"],
        "Gdes"
    )



print("\n")


print("=" * 40)
print("AVAILABLE STOCK VALUE")
print("=" * 40)


stock, total = get_stock_value()



for plan, data in stock.items():

    print()

    print(plan)

    print(
        "Quantity:",
        data["quantity"]
    )

    print(
        "Value:",
        data["value"],
        "Gdes"
    )



print()

print(
    "TOTAL STOCK VALUE:",
    total,
    "Gdes"
)