import sys
from pathlib import Path


sys.path.append(
    str(Path(__file__).resolve().parents[1])
)


from generator import generate_vouchers



AMBIGUOUS_CHARACTERS = (
    "I",
    "O",
    "i",
    "l",
    "o",
    "0",
    "1"
)



def main():

    print("=" * 45)
    print(" JEFF WIFI SECURE GENERATOR TEST ")
    print("=" * 45)


    quantity = 100


    vouchers = generate_vouchers(
        "2H-",
        quantity
    )


    print(
        f"\nGenerated vouchers: {len(vouchers)}"
    )


    # Test quantity

    if len(vouchers) != quantity:

        print(
            "❌ FAIL: Wrong number of vouchers generated."
        )

        return


    print(
        "✓ Quantity test passed."
    )



    # Test duplicates

    if len(vouchers) != len(set(vouchers)):

        print(
            "❌ FAIL: Duplicate vouchers detected."
        )

        return


    print(
        "✓ Duplicate test passed."
    )



    # Test ambiguous characters

    for voucher in vouchers:

        for char in AMBIGUOUS_CHARACTERS:

            if char in voucher:

                print(
                    "❌ FAIL: Ambiguous character found:"
                )

                print(
                    voucher
                )

                return



    print(
        "✓ Ambiguous character test passed."
    )



    # Display samples

    print(
        "\nSample vouchers:"
    )

    print(
        "----------------"
    )


    for voucher in vouchers[:10]:

        print(
            voucher
        )


    print(
        "\n✓ Security test completed successfully."
    )



if __name__ == "__main__":

    main()