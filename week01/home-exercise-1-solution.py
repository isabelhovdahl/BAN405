# -*- coding: utf-8 -*-
"""
Week 01 - Home exercise 1: Predict the output

Solution proposal.

For each snippet: what it displays, and why.
"""

# ---------------------------------------------------------------------------
# a) Displays: 30
#
# Each line reassigns x, using the value x had a moment earlier.
#   x = 10  ->  x = 10 + 5 = 15  ->  x = 15 * 2 = 30
# ---------------------------------------------------------------------------

x = 10
x = x + 5
x = x * 2
print(x)


# ---------------------------------------------------------------------------
# b) Displays: python
#
# Strings are immutable. .upper() does not change the string, it returns a NEW
# string - and here we throw that new string away without storing it.
# To keep it, we would have to write: word = word.upper()
# ---------------------------------------------------------------------------

word = "python"
word.upper()
print(word)


# ---------------------------------------------------------------------------
# c) Displays: [70, 85, 90, 100]
#
# The catch. "top = scores" does not copy the list, it gives the same list a
# second name. Appending through one name is visible through the other,
# because there is only one list.
# To get an independent copy: top = scores[:]  (or scores.copy())
# ---------------------------------------------------------------------------

scores = [70, 85, 90]
top = scores
top.append(100)
print(scores)


# ---------------------------------------------------------------------------
# d) Displays: None
#
# .append() changes the list in place, so it has nothing useful to return and
# returns None. Assigning that return value replaces the list with None and
# the data is gone.
# The correct form is just: items.append("d")
# ---------------------------------------------------------------------------

items = ["a", "b", "c"]
items = items.append("d")
print(items)


# ---------------------------------------------------------------------------
# e) Displays: ['b', 'c']
#
# No IndexError. Indexing past the end fails, but slicing past the end does
# not - the slice simply stops when it runs out of items.
# Compare: letters[5] would raise IndexError.
# ---------------------------------------------------------------------------

letters = ["a", "b", "c"]
print(letters[1:5])


# ---------------------------------------------------------------------------
# f) Displays: 7, then 8
#
# int() truncates - it drops everything after the decimal point.
# round() rounds to the nearest whole number.
# These give different answers for every value with a decimal part above .5,
# which is a common source of quiet, wrong results.
# ---------------------------------------------------------------------------

print(int(7.9))
print(round(7.9))
