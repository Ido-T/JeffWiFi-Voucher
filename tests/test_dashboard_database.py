from dashboard_database import get_all_vouchers


vouchers = get_all_vouchers()


print(
    "Total vouchers:",
    len(vouchers)
)