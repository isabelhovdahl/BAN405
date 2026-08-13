# -*- coding: utf-8 -*-
"""
Week 02 - Home exercise 1: Predict the output

Solution proposal.

For each snippet: what it displays, and why. Then the three broken conditions.
"""

# ---------------------------------------------------------------------------
# a) The first block displays:  B
#    The second block displays: B
#                               C
#
# An elif ladder is ONE decision with several possible outcomes: Python stops
# at the first condition that is true, so only "B" is printed.
#
# Three separate ifs are THREE decisions. Each one is evaluated on its own, so
# both score >= 80 and score >= 70 fire.
#
# This is the difference that decides which one you want: alternatives -> elif,
# independent tests -> separate ifs.
# ---------------------------------------------------------------------------

score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")

print("-" * 20)

score = 85

if score >= 90:
    print("A")
if score >= 80:
    print("B")
if score >= 70:
    print("C")

print("-" * 20)


# ---------------------------------------------------------------------------
# b) Displays: False, then True
#
# 0.1 + 0.2 is 0.30000000000000004, not 0.3. == asks an exact question and
# gets an honest answer. Rounding first throws away the noise, and then the
# two values really are equal.
# ---------------------------------------------------------------------------

print(0.1 + 0.2 == 0.3)
print(round(0.1 + 0.2, 2) == 0.3)

print("-" * 20)


# ---------------------------------------------------------------------------
# c) Displays: True, then False
#
# `and` binds tighter than `or`, so the first line means
#     (is_member and age >= 18) or age >= 67
#     (False       and True     ) or True         ->  True
# and the brackets on the second line change the grouping to
#     is_member and (age >= 18 or age >= 67)
#     False     and (True                  )      ->  False
#
# Same words, same order, different rule. This is why the house rule is to
# bracket anything that mixes `and` with `or`.
# ---------------------------------------------------------------------------

is_member = False
age = 70

print(is_member and age >= 18 or age >= 67)
print(is_member and (age >= 18 or age >= 67))

print("-" * 20)


# ---------------------------------------------------------------------------
# d) Displays: B, then True
#
# The first line is not a comparison at all. Comparison binds tighter than
# `or`, so Python reads it as
#     (answer == "A") or ("B")   ->   False or "B"
# and `or` returns one of its two operands rather than True/False - here the
# string "B", which is truthy.
#
# So that condition is true for every possible value of answer, including "F".
# It just happens to look right when answer really is "B".
#
# Each side of an `and` or an `or` has to be a complete question.
# ---------------------------------------------------------------------------

answer = "B"

print(answer == "A" or "B")
print(answer == "A" or answer == "B")

print("-" * 20)


# ---------------------------------------------------------------------------
# e) Displays: False, False, False
#
# A decimal point is not a digit. A minus sign is not a digit. And an empty
# string has nothing to check, so there is no "at least one character".
#
# .isdigit() answers exactly one narrow question, and "did the user type a
# number?" is not it.
# ---------------------------------------------------------------------------

print("3.14".isdigit())
print("-7".isdigit())
print("".isdigit())

print("-" * 20)


# ---------------------------------------------------------------------------
# f) Displays: False - and does NOT crash
#
# `and` short-circuits. len(code) > 0 is False, so the answer is already
# settled and code[0] is never evaluated. Written the other way round it
# raises an IndexError.
# ---------------------------------------------------------------------------

code = ""

print(len(code) > 0 and code[0] == "N")

print("-" * 20)


# ---------------------------------------------------------------------------
# g) Displays: True, False, True
#
# " " is a string containing one character, so it is not empty and therefore
# truthy. "0" is likewise a one-character string, and truthy - unlike the
# number 0, which is falsy.
#
# The two strings are the reason `if answer:` and `if answer != "":` are not
# always the same test as `if int(answer) != 0:`.
# ---------------------------------------------------------------------------

print(bool(" "))
print(bool(0))
print(bool("0"))

print("-" * 20)


# ---------------------------------------------------------------------------
# The three broken conditions
# ---------------------------------------------------------------------------

# 1. if grade = "A":
#
#    A single = assigns, it does not compare, and Python will not let you
#    assign inside a condition. The error message even suggests the fix.

grade = "A"

if grade == "A":
    print("Top marks")


# 2. if 0 < score or score > 100:
#
#    Two mistakes. `or` should be `and` - the score has to satisfy both halves,
#    not either one - and as written the condition is true for 200, which is
#    the opposite of what was wanted. The lower bound should also include 0.
#
#    Written with `or` and `>`, this is the "out of range" test, not the "in
#    range" one. The chained form says what it means:

score = 87

if 0 <= score <= 100:
    print("Valid score")


# 3. if name[0].isupper() and len(name) > 0:
#
#    The guard is on the wrong side. name[0] is evaluated first, so an empty
#    name raises an IndexError before the length is ever checked. Swapping the
#    two halves lets short-circuiting do its job.

name = ""

if len(name) > 0 and name[0].isupper():
    print("Starts with a capital")
else:
    print("Empty, or does not start with a capital")


# ---------------------------------------------------------------------------
# The pattern behind (d), (f) and broken condition 3
#
# All three are about the fact that Python evaluates a condition in a
# particular order, and that the order is not always the one you read off the
# page. Precedence decides how the pieces group; short-circuiting decides
# which pieces get evaluated at all.
#
# Brackets fix the first. Putting the safety check first fixes the second.
# ---------------------------------------------------------------------------
