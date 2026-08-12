# -*- coding: utf-8 -*-
"""
Week 03 - Home exercise 4: The receipt, finished

Solution proposal.

The receipt from the first set of exercises, written with a loop so that it no
longer cares how many items there are.
"""

items = ["Espresso machine", "Coffee beans", "Oat milk"]
quantities = [1, 2, 3]
unit_prices = [4999.00, 149.90, 24.50]

VAT_RATE = 0.25


# 1. Banner.
print("*" * 40)
print("KAFFEBUTIKKEN BERGEN")
print("*" * 40)


# 2, 3 and 5. One pass over the data does all three jobs at once.
#
# zip walks the three lists in step, so there is no indexing anywhere and no
# chance of reading item 2 next to quantity 3. enumerate wraps it to supply the
# line number, and start=1 means we number from 1 without writing i + 1.
#
# Everything that has to survive the loop is initialized before it: the running
# subtotal, and the two variables recording the biggest line so far.
subtotal = 0

largest_total = 0
largest_item = ""

for line_no, (item, quantity, price) in enumerate(zip(items, quantities, unit_prices), start=1):

    line_total = quantity * price

    print(f"{line_no}. {item:<20}{quantity:>3} x {price:>9.2f} = {line_total:>10.2f}")

    # The accumulator.
    subtotal += line_total

    # The search, run as we go rather than in a second loop. A plain > means
    # the FIRST of two equal lines wins, which is the usual convention.
    if line_total > largest_total:
        largest_total = line_total
        largest_item = item


# 4. Totals. The subtotal was accumulated above, so there is nothing to
# recalculate here.
vat = subtotal * VAT_RATE
total = subtotal + vat

print("-" * 40)
print(f"{'Subtotal':<28}{subtotal:>12.2f}")
print(f"{'VAT (25%)':<28}{vat:>12.2f}")
print(f"{'TOTAL':<28}{total:>12,.2f}")
print("*" * 40)


# 5. The result of the search.
print(f"\nLargest line: {largest_item} at {largest_total:.2f}")


# ---------------------------------------------------------------------------
# Adding a fourth item
#
# Append "Filter papers", 4 and 39.00 to the three lists and run it again.
# Nothing else changes: the loop produces four lines instead of three, the
# subtotal picks up the extra line on its own, and the search reconsiders the
# winner without being asked.
#
# That is the test that tells you the loop is doing the work. Anything that
# needs editing when the data grows is a piece of the program that was written
# by hand and should not have been - which is exactly what the hand-written
# version of this receipt was.
#
# Three parallel lists is a fragile way to store this, though. Nothing stops
# somebody inserting an item and forgetting its price, and then every row after
# it is wrong with no error to warn you. A better shape is one list of records
# rather than three lists of fields - and better still is a table with named
# columns, which is where the second half of this course goes.
#
# What this program does NOT do:
#
# - It does not check that the three lists are the same length. zip stops at
#   the shortest, so a missing price silently drops the last item from the
#   receipt rather than complaining about it.
# - It does not handle an empty receipt gracefully. With empty lists the loop
#   runs zero times, the totals come out as 0.00, which is fine, but
#   largest_item stays as the empty string and the last line reads oddly.
# - VAT in Norway is not 25% on everything - food is lower. One rate for the
#   whole receipt is a simplification.
# ---------------------------------------------------------------------------
