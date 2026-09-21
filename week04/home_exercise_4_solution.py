# -*- coding: utf-8 -*-
"""
Week 04 - Home exercise 4: The receipt, refactored

Solution proposal.

The receipt, written a third time: four small functions that each do one job,
and a main that puts them in order. line_total, format_line and a first main
come from the lecture notebook; this version adds the VAT and moves the
printing out of main.
"""


# 1. The smallest piece, exactly as in the lecture. One line, and worth its own
# name anyway: it is the only place in the program where a line total is
# defined, so if the shop starts charging per kilo it changes here and nowhere
# else.
def line_total(quantity, unit_price):
    """Return the total for one receipt line."""
    return quantity * unit_price


# 2. Returns a string rather than printing it. Also from the lecture, unchanged.
#
# That is the whole difference between this and the loop version. A function
# that returns its line can be printed, written to a file, collected into a
# list or tested - and printing it is one word longer. A function that prints
# can only ever print.
def format_line(item, quantity, unit_price):
    """Return one formatted receipt line as a string."""
    return f"{item:<20}{quantity:>3} x {unit_price:>8.2f} = {line_total(quantity, unit_price):>9.2f}"


# 3. Three values out of one function.
#
# The three totals belong together - each is computed from the one before it -
# so computing them in one place and returning them together is more honest
# than three functions that would each have to recompute the subtotal.
#
# The VAT rate comes in as a parameter with a default, not as a variable at the
# top of the file. The default keeps the common call short, and the header
# says everything the function depends on.
def receipt_totals(quantities, unit_prices, vat_rate=0.25):
    """
    Return the subtotal, the VAT and the total including VAT.

    Parameters
    ----------
    quantities : list
        The quantity for each line.
    unit_prices : list
        The unit price for each line, in the same order.
    vat_rate : float, optional
        The VAT rate as a decimal. Defaults to 0.25.

    Returns
    -------
    tuple
        (subtotal, vat, total), all floats.
    """
    subtotal = 0

    for quantity, price in zip(quantities, unit_prices):
        subtotal += line_total(quantity, price)

    vat = subtotal * vat_rate

    return subtotal, vat, subtotal + vat


# 4. The only function that prints anything.
#
# Everything above it computes and returns; this one displays. Keeping the
# printing in one place is what makes the other three testable.
#
# It needs the VAT rate too - both to pass on to receipt_totals and to write
# the label - so it takes the same parameter with the same default. The label
# is built from the rate rather than typed as "25%", so the two cannot
# disagree.
def print_receipt(items, quantities, unit_prices, vat_rate=0.25):
    """Print the full receipt for the given items."""
    print("*" * 46)
    print("KAFFEBUTIKKEN BERGEN")
    print("*" * 46)

    for item, quantity, price in zip(items, quantities, unit_prices):
        print(format_line(item, quantity, price))

    subtotal, vat, total = receipt_totals(quantities, unit_prices, vat_rate)
    vat_label = f"VAT ({vat_rate:.0%})"

    print("-" * 46)
    print(f"{'Subtotal':<34}{subtotal:>12.2f}")
    print(f"{vat_label:<34}{vat:>12.2f}")
    print(f"{'TOTAL':<34}{total:>12,.2f}")
    print("*" * 46)


# 5. The data lives inside main, not at the top of the file.
#
# The lecture's main printed the receipt itself. This one only holds the data
# and hands it over. There are no global variables in this program at all, so
# no function can accidentally depend on something it was not given.
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
    print(f"  line_total(3, 24.50)                          = {line_total(3, 24.50)}")
    print(f"  receipt_totals([1], [100.0])                  = {receipt_totals([1], [100.0])}")
    print(f"  receipt_totals([1], [100.0], vat_rate=0.15)   = {receipt_totals([1], [100.0], vat_rate=0.15)}")
    print(f"  receipt_totals([], [])                        = {receipt_totals([], [])}")


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
# Notice also where the VAT rate lives: in the headers of the two functions that
# need it, with a default. That is the repair the lecture made to add_vat, and
# it means both functions can be read, tested and reused without looking
# anywhere else in the file.
#
# In other people's code you will often see a fixed value like this written in
# capitals at the top of the file instead - VAT_RATE = 0.25 - and read by the
# functions directly. That is a widely used convention for constants, and you
# should recognise it when you meet it. This course passes values in instead,
# because a function that reads a name from outside its brackets has a header
# that no longer tells you what it depends on, whether or not the value ever
# changes.
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
