from dashboard_database import (
    get_status_summary,
    get_plan_summary,
    get_sales_summary,
    get_revenue_by_plan,
    get_stock_value,
    get_last_batch,
    get_integrity_check
)



def show_dashboard():


    print("\n====================================")
    print("        JEFF WIFI INVENTORY")
    print("====================================\n")



    # STATUS SUMMARY

    status = get_status_summary()



    total_vouchers = (
        status["AVAILABLE"]
        +
        status["SOLD"]
        +
        status["USED"]
    )



    print(
        f"TOTAL VOUCHERS: {total_vouchers}"
    )



    print("\nSTATUS SUMMARY")
    print("------------------------------------")


    print(
        f"AVAILABLE : {status['AVAILABLE']}"
    )

    print(
        f"SOLD      : {status['SOLD']}"
    )

    print(
        f"USED      : {status['USED']}"
    )



    # PLAN SUMMARY

    print("\nPLAN SUMMARY")
    print("------------------------------------")



    plans = get_plan_summary()



    for plan, data in plans.items():


        print(
            f"\n{plan}"
        )


        print(
            f"    AVAILABLE : {data['AVAILABLE']}"
        )


        print(
            f"    SOLD      : {data['SOLD']}"
        )


        print(
            f"    USED      : {data['USED']}"
        )



    # SALES SUMMARY


    sold, revenue = get_sales_summary()



    print("\nSALES SUMMARY")
    print("------------------------------------")


    print(
        f"TOTAL SOLD: {sold}"
    )


    print(
        f"TOTAL REVENUE: {revenue} Gdes"
    )



    # REVENUE BY PLAN


    print("\nREVENUE BY PLAN")
    print("------------------------------------")


    revenue_plan = get_revenue_by_plan()



    for plan, data in revenue_plan.items():


        print(
            f"\n{plan}"
        )


        print(
            f"    Sold: {data['sold']}"
        )


        print(
            f"    Revenue: {data['revenue']} Gdes"
        )



    # STOCK VALUE


    stock, total_stock = get_stock_value()



    print("\nAVAILABLE STOCK VALUE")
    print("------------------------------------")



    for plan, data in stock.items():


        print(
            f"\n{plan}"
        )


        print(
            f"    Quantity: {data['quantity']}"
        )


        print(
            f"    Value: {data['value']} Gdes"
        )



    print(
        f"\nTOTAL STOCK VALUE: {total_stock} Gdes"
    )



    # LAST BATCH


    print("\nLAST GENERATED BATCH")
    print("------------------------------------")


    batch = get_last_batch()



    if batch:


        print(
            f"Batch ID: {batch['Batch ID']}"
        )


        print(
            f"Plan: {batch['Plan']}"
        )


        print(
            f"Quantity: {batch['Quantity']}"
        )


        print(
            f"Created: {batch['Created']}"
        )


    else:

        print(
            "No batch history found."
        )



    # INTEGRITY CHECK


    print("\nDATA INTEGRITY CHECK")
    print("------------------------------------")


    problems = get_integrity_check()



    if len(problems) == 0:


        print(
            "✓ All checks passed."
        )


    else:


        print(
            f"⚠ {len(problems)} problem(s) found:"
        )


        for problem in problems:


            print(
                "-",
                problem
            )




if __name__ == "__main__":

    show_dashboard()