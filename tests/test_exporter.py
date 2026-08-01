import sys
from pathlib import Path


sys.path.append(
    str(Path(__file__).resolve().parents[1])
)


from exporter import save_import_file



def main():

    print("=" * 45)
    print(" JEFF WIFI MIKROTIK EXPORT TEST ")
    print("=" * 45)


    vouchers = [
        "2H-TEST01",
        "2H-TEST02",
        "2H-TEST03"
    ]


    file = save_import_file(
        vouchers,
        "2-HOURS"
    )


    print()

    print(
        "Generated file:"
    )

    print(
        file
    )


    print(
        "\nExport test completed."
    )



if __name__ == "__main__":

    main()