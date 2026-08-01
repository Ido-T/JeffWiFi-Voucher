

import secrets

from database.voucher_repository import voucher_exists
# Characters intentionally exclude:
# O, 0, I, l, 1
# to avoid user confusion when typing vouchers.

CHARACTERS = (
    "ABCDEFGHJKLMNPQRSTUVWXYZ"
    "abcdefghjkmnpqrstuvwxyz"
    "23456789"
)



def generate_code(prefix):
    """
    Generates one secure voucher code.

    Example:
        2H-K7mQ4a
    """


    code = ""


    for _ in range(6):

        code += secrets.choice(
            CHARACTERS
        )


    return prefix + code




def generate_vouchers(prefix, quantity):

    vouchers = set()


    while len(vouchers) < quantity:

        voucher = generate_code(prefix)


        if voucher in vouchers:

            continue


        if voucher_exists(voucher):

            continue


        vouchers.add(voucher)


    return sorted(vouchers)