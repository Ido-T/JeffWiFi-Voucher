from dashboard_database import (
    get_status_summary,
    get_plan_summary,
    get_sales_summary
)


print("STATUS")
print(get_status_summary())


print("\nPLAN")
print(get_plan_summary())


print("\nSALES")
print(get_sales_summary())