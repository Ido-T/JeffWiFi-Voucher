import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)


from dashboard_database import get_integrity_check


print("=" * 40)
print("DATABASE INTEGRITY CHECK")
print("=" * 40)


issues = get_integrity_check()



if len(issues) == 0:

    print(
        "✓ All checks passed."
    )


else:

    print(
        f"⚠ {len(issues)} problem(s) found:"
    )


    for issue in issues:

        print(
            "-",
            issue
        )