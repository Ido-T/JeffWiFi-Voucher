import sys
from pathlib import Path


sys.path.append(
    str(Path(__file__).resolve().parents[1])
)


from generator import generate_vouchers
from database.voucher_repository import voucher_exists



def main():

    print("=" * 45)
    print(" JEFF WIFI GENERATION PIPELINE TEST ")
    print("=" * 45)


    vouchers = generate_vouchers(
        "2H-",
        20
    )


    print(
        f"\nGenerated: {len(vouchers)}"
    )


    duplicate_found = False


    for voucher in vouchers:

        if voucher_exists(voucher):

            duplicate_found = True


            print(
                "Duplicate found:",
                voucher
            )


    if duplicate_found:

        print(
            "❌ FAIL: Database duplicate detected."
        )

    else:

        print(
            "✓ No database duplicates."
        )


    print(
        "\nPipeline test completed."
    )



if __name__ == "__main__":

    main()