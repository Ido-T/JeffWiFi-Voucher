import sys
from pathlib import Path


sys.path.append(
    str(Path(__file__).resolve().parents[1])
)


from exporter import save_import_file



def main():

    print("=" * 45)
    print(" JEFF WIFI EXPORT HISTORY TEST ")
    print("=" * 45)


    vouchers = [
        "2H-HISTORY01",
        "2H-HISTORY02",
        "2H-HISTORY03"
    ]


    file = save_import_file(
        vouchers,
        "2-HOURS"
    )


    print()

    print(
        "Export created:"
    )

    print(
        file
    )


    print()

    print(
        "History test completed."
    )



if __name__ == "__main__":

    main()