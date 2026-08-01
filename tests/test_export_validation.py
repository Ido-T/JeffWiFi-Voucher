import sys
from pathlib import Path


sys.path.append(
    str(Path(__file__).resolve().parents[1])
)


from exporter import save_import_file



def test_valid_export():

    vouchers = [
        "2H-TEST01",
        "2H-TEST02"
    ]


    file = save_import_file(
        vouchers,
        "2-HOURS"
    )


    print(
        "✓ Valid export created:"
    )

    print(
        file
    )





def test_invalid_voucher():


    vouchers = [
        "2H-BAD;REMOVE"
    ]


    try:

        save_import_file(
            vouchers,
            "2-HOURS"
        )


        print(
            "❌ FAIL: Invalid voucher accepted."
        )


    except ValueError:

        print(
            "✓ Invalid voucher rejected."
        )





def test_invalid_profile():


    vouchers = [
        "2H-TEST01"
    ]


    try:

        save_import_file(
            vouchers,
            'BAD"PROFILE'
        )


        print(
            "❌ FAIL: Invalid profile accepted."
        )


    except ValueError:

        print(
            "✓ Invalid profile rejected."
        )





if __name__ == "__main__":


    print("=" * 45)

    print(
        " JEFF WIFI EXPORT SECURITY TEST "
    )

    print("=" * 45)


    test_valid_export()

    test_invalid_voucher()

    test_invalid_profile()


    print()

    print(
        "Export security test completed."
    )