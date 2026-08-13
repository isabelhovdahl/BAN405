# -*- coding: utf-8 -*-
"""
Week 04 - Home exercise 4: The receipt, refactored

Solution proposal.

The receipt, written a third time: four small functions that each do one job,
and a main that puts them in order.
"""

VAT_RATE = 0.25


# 1. The smallest piece. One line, and worth its own name anyway: it is the
# only place in the program where a line total is defined, so if the shop
# starts charging per kilo it changes here and nowhere else.
def line_total(quantity, unit_price):
    """Return the total for one receipt line."""
    return quantity * unit_price


# 2. Returns a string rather than printing it.
#
# That is the whole difference between this and the loop version. A function
# that returns its line can be printed, written to a file, collected into a
# list or tested - and printing it is one word longer. A function that prints
# can only ever print.
def format_line(item, quantity, unit_price):
    """Return one formatted receipt line as a string."""
    total = line_total(quantity, unit_price)

    return f"{item:<20}{quantity:>3} x {unit_price:>9.2f} = {total:>10.2f}"


# 3. Three values out of one function.
#
# The three totals belong together - each is computed from the one before it -
# so computing them in one place and returning them together is more honest
# than three functions that would each have to recompute the subtotal.
def receipt_totals(quantities, unit_prices):
    """
    Return the subtotal, the VAT and the total including VAT.

    Parameters
    ----------
    quantities : list
        The quantity for each line.
    unit_prices : list
        The unit price for each line, in the same order.

    Returns
    -------
    tuple
        (subtotal, vat, total), all floats.
    """
    subtotal = 0

    for quantity, price in zip(quantities, unit_prices):
        subtotal += line_total(quantity, price)

    vat = subtotal * VAT_RATE

    return subtotal, vat, subtotal + vat


# 4. The only function that prints anything.
#
# Everything above it computes and returns; this one displays. Keeping the
# printing in one place is what makes the other three testable.
def print_receipt(items, quantities, unit_prices):
    """Print the full receipt for the given items."""
    print("*" * 48)
    print("KAFFEBUTIKKEN BERGEN")
    print("*" * 48)

    for item, quantity, price in zip(items, quantities, unit_prices):
        print(format_line(item, quantity, price))

    subtotal, vat, total = receipt_totals(quantities, unit_prices)

    print("-" * 48)
    print(f"{'Subtotal':<36}{subtotal:>12.2f}")
    print(f"{'VAT (25%)':<36}{vat:>12.2f}")
    print(f"{'TOTAL':<36}{total:>12,.2f}")
    print("*" * 48)


# 5. The data lives inside main, not at the top of the file.
#
# There are now no global variables in this program except VAT_RATE, which is a
# constant. No function can accidentally depend on something it was not given.
def main():
    """Print a receipt for the coffee shop's three items."""
    items = ["Espresso machine", "Coffee beans", "Oat milk"]
    quantities = [1, 2, 3]
    unit_prices = [4999.00, 149.90, 24.50]

    print_receipt(items, quantities, unit_prices)


if __name__ == "__main__":
    main()

    # Testing the pieces separately, which is the point of having written it
    # this way. Neither of these prints a receipt.
    print("\nChecks:")
    print(f"  line_total(3, 24.50)            = {line_total(3, 24.50)}")
    print(f"  receipt_totals([1], [100.0])    = {receipt_totals([1], [100.0])}")
    print(f"  receipt_totals([], [])          = {receipt_totals([], [])}")


# ---------------------------------------------------------------------------
# What the third version bought
#
# The hand-written receipt could be wrong in three places. The loop version
# could only be wrong in one, but it was one long block of code that had to be
# read from top to bottom to be understood, and there was no way to check any
# part of it except by running the whole thing and looking at the output.
#
# This version can be checked a piece at a time. line_total(3, 24.50) is either
# 73.5 or it is not, and you find out in one line without printing anything.
# That is not a small convenience: it is the difference between "the total
# looks wrong somewhere" and "line_total is wrong".
#
# Notice which function calls which. format_line calls line_total, and
# receipt_totals calls line_total, so the multiplication is written once and
# the two can never disagree about what a line costs. In the loop version the
# line total was computed twice - once for display and once for the subtotal -
# and nothing stopped those two expressions drifting apart.
#
# Notice also that VAT_RATE is written in capitals. That is a convention, not a
# rule: Python will let you reassign it. Capitals are how programmers tell each
# other "this is a fixed value, do not change it while the program runs", and
# it is the one kind of global variable that is generally accepted, because a
# constant cannot surprise you the way a changing one can.
#
# What this program does NOT do:
#
# - The data is still three parallel lists that belong together only by
#   position. Nothing stops somebody inserting an item and forgetting its
#   price, and zip stops at the shortest list, so the receipt would quietly
#   lose its last line rather than complain. A table with named columns is the
#   right shape for this, and it comes in the second half of the course.
# - receipt_totals trusts its inputs completely. Hand it strings instead of
#   numbers and it will happily add them up in a way that makes no sense.
# - It applies one VAT rate to the whole receipt. Norwegian VAT is lower on
#   food, so a real receipt needs a rate per line.
# - An empty receipt produces a banner, no lines, and totals of 0.00. That is
#   arguably correct and definitely untested against what a shop would want.
# ---------------------------------------------------------------------------
