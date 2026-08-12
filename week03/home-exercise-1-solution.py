# -*- coding: utf-8 -*-
"""
Week 03 - Home exercise 1: Predict the output

Solution proposal.

For each snippet: what it displays, and why. Then the two broken loops.
"""

# ---------------------------------------------------------------------------
# a) Displays: [100, 200, 300]
#
# Nothing changed. `price` is a NAME that is attached to each item of the list
# in turn. Assigning to that name detaches it and points it at a new number -
# it does not write into the list.
#
# This is the same fact about names and objects we met when a list and a copy
# of a list turned out to be the same list. To change the list you have to
# reach into it: prices[i] = ... , or build a new list.
# ---------------------------------------------------------------------------

prices = [100, 200, 300]

for price in prices:
    price = price + 50

print(prices)

print("-" * 20)


# ---------------------------------------------------------------------------
# b) Displays: 4
#
# The initialization is INSIDE the loop, so total is reset to 0 at the start of
# every pass. The additions from the earlier passes are thrown away, and what
# survives is the contribution of the last item alone.
#
# The accumulator has three parts and they go in three different places:
# initialize before the loop, update inside it, use after it.
# ---------------------------------------------------------------------------

for num in [1, 2, 3, 4]:
    total = 0
    total += num

print(total)

print("-" * 20)


# ---------------------------------------------------------------------------
# c) Displays: range(0, 3), then [0, 1, 2], then 4
#
# range does not build a list. It produces the numbers one at a time as they
# are asked for, which is why printing it shows the recipe rather than the
# result, and why list() is needed to see it.
#
# len(range(1, 5)) is 4, not 5: the stop value is not included. Same rule as
# slicing, where [1:5] also gives four items.
# ---------------------------------------------------------------------------

print(range(3))
print(list(range(3)))
print(len(range(1, 5)))

print("-" * 20)


# ---------------------------------------------------------------------------
# d) The loop never ends, whatever `which` is.
#
#     while which != "F" or which != "C":
#
# Take the two halves one at a time.
#
#     which is "F"  ->  "F" != "F" is False, "F" != "C" is True   ->  True
#     which is "C"  ->  "C" != "F" is True                        ->  True
#     which is "x"  ->  both halves are True                      ->  True
#
# No value can fail both tests at once, because no value can be equal to "F"
# and to "C" at the same time. The condition is true for every string in
# existence, so the loop can never stop.
#
# This is the same family of bug as `grade == "A" or "B"`: an expression that
# looks like it says one thing and is in fact true always.
#
# The rule that fixes it: pushing a `not` inside brackets flips both the
# comparisons and the connective.
#
#     not (which == "F" or which == "C")   is   which != "F" and which != "C"
#
# So the connective has to be `and`, not `or`. Or, far more readably, use `in`.
# ---------------------------------------------------------------------------

print("which   with 'and'   with 'not in'")

for which in ("F", "C", "x"):
    with_and = which != "F" and which != "C"
    with_in = which not in ("F", "C")

    print(f"{which:<8}{str(with_and):<12}{with_in}")

print("-" * 20)


# ---------------------------------------------------------------------------
# e) Displays: 1, 2, 5, 6
#
# break leaves the loop it is written in, and nothing more. In the second row
# it fires immediately, so 3 and 4 are never displayed - but the OUTER loop
# carries on to the third row as if nothing had happened.
#
# To leave both loops you need a flag that the outer loop tests after the inner
# one has finished.
# ---------------------------------------------------------------------------

for row in [[1, 2], [3, 4], [5, 6]]:
    for value in row:
        if value == 3:
            break

        print(value)

print("-" * 20)


# ---------------------------------------------------------------------------
# f) Displays: 1, 4, 9 - and then [None, None, None]
#
# The squares really are printed, so at a glance it looks like it worked. But a
# comprehension exists to BUILD A LIST, and the value it collects is whatever
# the expression evaluates to. print() displays its argument and then returns
# nothing at all, which in Python is the value None.
#
# So the list is three Nones, built at some cost and wanted by nobody. If you
# are not keeping the result, write the loop.
# ---------------------------------------------------------------------------

squares = [print(num ** 2) for num in [1, 2, 3]]

print(squares)

print("-" * 20)


# ---------------------------------------------------------------------------
# g) Displays: ['a', '', 'b'], then ['a', 'b'], then ['']
#
# With an argument, .split() cuts at every single occurrence of the separator.
# Two commas in a row have nothing between them, so an empty string is what
# sits between them, and that is what you get.
#
# With no argument, .split() cuts on any RUN of whitespace and throws the
# empties away - which is why it is the right one for splitting text into
# words.
#
# The third is the one that catches people. Splitting an empty string gives a
# list containing one empty string, NOT an empty list. Its length is 1, and a
# list with something in it is truthy, so `if parts:` will cheerfully tell you
# that a blank line had content.
# ---------------------------------------------------------------------------

print("a,,b".split(","))
print("  a  b  ".split())
print("".split(","))

print("-" * 20)


# ---------------------------------------------------------------------------
# The two broken loops
# ---------------------------------------------------------------------------

# 1. for num in range(1, 10):
#
#    Displays 45 rather than 55. The stop value of range is not included, so
#    range(1, 10) is 1 to 9 and the 10 never arrives. To count up TO a number
#    you have to write one past it.

total = 0

for num in range(1, 11):
    total += num

print(total)


# 2. The else belongs to the `if` INSIDE the loop.
#
#    So the program does not report on the list at all - it reports on each
#    item separately, and prints "No negative numbers." four times over. A
#    single conclusion about a whole list cannot be reached until the loop has
#    finished looking at all of it.
#
#    The repair is the search pattern: a flag set inside the loop, and the
#    decision taken outside it.

values = [4, 9, 2, 7]

has_negative = False

for value in values:
    if value < 0:
        has_negative = True
        break

if has_negative:
    print("Found a negative number.")
else:
    print("No negative numbers.")


# ---------------------------------------------------------------------------
# The pattern behind (b), (d) and broken loop 2
#
# All three are about WHERE a statement sits rather than what it says. The
# accumulator in (b) is correct code in the wrong place. The decision in
# broken loop 2 is correct code in the wrong place. And (d) is the reminder
# that a condition can be perfectly valid Python and still be true always.
#
# Indentation is not formatting in Python. It is the part of the program that
# says which statements belong to the loop and which belong to the program
# around it, and it is worth reading as carefully as the statements themselves.
# ---------------------------------------------------------------------------
