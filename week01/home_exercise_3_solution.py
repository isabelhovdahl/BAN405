# -*- coding: utf-8 -*-
"""
Week 01 - Home exercise 3: Format a receipt

Solution proposal.

Three items have been sold. The lists line up by position: items[0] was sold in
quantity quantities[0] at price unit_prices[0].

Print a receipt with a banner, one line per item, and subtotal / VAT / total.
All amounts to two decimals; the total with a thousands separator.
"""

items = ["Espresso machine", "Coffee beans", "Oat milk"]
quantities = [1, 2, 3]
unit_prices = [4999.00, 149.90, 24.50]

VAT_RATE = 0.25

# Line totals, one per item. No loops yet, so we index each position by hand.
line_1 = quantities[0] * unit_prices[0]
line_2 = quantities[1] * unit_prices[1]
line_3 = quantities[2] * unit_prices[2]

subtotal = line_1 + line_2 + line_3
vat = subtotal * VAT_RATE
total = subtotal + vat

# Banner. "*" * 40 saves us counting asterisks - and makes the width easy to
# change later, since it appears in one place.
print("*" * 40)
print("           KAFFEBAREN AS")
print("*" * 40)

# One line per item.
#
# {name:<17}    left-aligns the name in a 17-character column
# {qty:>2}      right-aligns the quantity in a 2-character column
# {price:>9.2f} right-aligns the amount in 9 characters, with two decimals
#
# Right-aligning the numbers is what makes the decimal points line up. The
# widths are chosen to add up to 40, so the lines fit inside the banner.
print(f"{items[0]:<17}{quantities[0]:>2} x{unit_prices[0]:>9.2f}{line_1:>10.2f}")
print(f"{items[1]:<17}{quantities[1]:>2} x{unit_prices[1]:>9.2f}{line_2:>10.2f}")
print(f"{items[2]:<17}{quantities[2]:>2} x{unit_prices[2]:>9.2f}{line_3:>10.2f}")

print("-" * 40)

print(f"{'Subtotal':<20}{subtotal:>20.2f}")
print(f"{'VAT (25%)':<20}{vat:>20.2f}")
print(f"{'Total':<20}{total:>20,.2f}")

print("*" * 40)


# ---------------------------------------------------------------------------
# Two things worth noticing
#
# 1. We rounded nothing along the way. The :.2f in the f-string affects how the
#    numbers are *displayed*, not how they are stored, so the total is computed
#    from full-precision values. Rounding each line total first and then adding
#    them up can give a different answer by a few øre - which is exactly the
#    float problem from the lecture, and why you round at the end, once.
#
# 2. VAT_RATE is written in capitals and defined at the top. That is the usual
#    convention for a value that is fixed for the whole program, and it means
#    there is one place to change it if the rate ever moves.
# ---------------------------------------------------------------------------
