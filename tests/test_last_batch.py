from dashboard_database import get_last_batch


print("=" * 40)
print("LAST GENERATED BATCH")
print("=" * 40)


batch = get_last_batch()


if batch:

    print(
        "Batch ID:",
        batch["Batch ID"]
    )

    print(
        "Plan:",
        batch["Plan"]
    )

    print(
        "Quantity:",
        batch["Quantity"]
    )

    print(
        "Created:",
        batch["Created"]
    )


else:

    print(
        "No batch found."
    )