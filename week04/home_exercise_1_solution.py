# -*- coding: utf-8 -*-
"""
Week 04 - Home exercise 1: Predict the output

Solution proposal.

For each snippet: what it displays, and why. Then the two broken functions.
"""

# ---------------------------------------------------------------------------
# a) Displays: None
#
# add_vat computes the right number and then throws it away. There is no
# return statement, so the function hands back None - Python's way of saying
# "there is no value here".
#
# This is the same None that turned up when `fruits = fruits.sort()` destroyed
# a list. It is a value, not an absence of one, so it travels quietly through
# the program until it meets something that cannot cope with it.
# ---------------------------------------------------------------------------


def add_vat(price):
    total = price * 1.25


print(add_vat(100))

print("-" * 20)


# ---------------------------------------------------------------------------
# b) Displays: 10
#
# The return is INSIDE the loop, so it fires on the very first pass. return
# does not leave the loop the way break does - it leaves the whole function,
# and the remaining items are never visited.
#
# Moving the return one level of indentation to the left, so that it sits after
# the loop, gives the intended 60. Indentation is not formatting in Python; it
# is the part of the program that says which statements belong to the loop.
# ---------------------------------------------------------------------------


def total_of(values):
    total = 0

    for value in values:
        total += value
        return total


print(total_of([10, 20, 30]))

print("-" * 20)


# ---------------------------------------------------------------------------
# c) Displays: 99, then 10
#
# `count = 99` inside the function creates a NEW variable that is local to
# bump. It has the same name as the global one and nothing to do with it.
#
# The global count is untouched, which is exactly what scope is for: you can
# write a function without first checking every variable name in the rest of
# the program.
# ---------------------------------------------------------------------------

count = 10


def bump():
    count = 99
    return count


print(bump())
print(count)

print("-" * 20)


# ---------------------------------------------------------------------------
# d) Displays: [4, 9, 0] [4, 9, 0]
#              5 4
#
# The list was changed and the number was not, and the difference is not about
# functions at all - it is the fact about names and objects from the first
# week, seen from a new angle.
#
# `values` is a second NAME for the caller's list. .append reaches into the
# object that both names refer to, so the caller sees the change.
#
# `number` is a second name for the caller's 4. `number = number + 1` does not
# change the 4 - a number cannot be changed - it points the local name at a
# new object, and the caller's name is left where it was.
#
# The rule: a function can change a list or a dictionary you pass it. It can
# never change a number, a string or a boolean.
# ---------------------------------------------------------------------------


def add_zero(values):
    values.append(0)
    return values


def add_one(number):
    number = number + 1
    return number


readings = [4, 9]
n = 4

print(add_zero(readings), readings)
print(add_one(n), n)

print("-" * 20)


# ---------------------------------------------------------------------------
# e) Displays: 5.0, 2.0, 0.5, then a TypeError
#
#   divide(10)          -> b uses its default of 2                    -> 5.0
#   divide(10, 5)       -> the default is overridden                  -> 2.0
#   divide(b=10, a=5)   -> named, so the order does not matter        -> 0.5
#   divide(b=10)        -> a has no default and was not supplied      -> TypeError
#
# A parameter with a default is optional. A parameter without one is required,
# and naming the other argument does not help.
# ---------------------------------------------------------------------------


def divide(a, b=2):
    return a / b


print(divide(10))
print(divide(10, 5))
print(divide(b=10, a=5))

try:
    print(divide(b=10))
except TypeError as error:
    print(f"TypeError: {error}")

print("-" * 20)


# ---------------------------------------------------------------------------
# f) ValueError, IndexError, KeyError, ZeroDivisionError, TypeError
#
# Note the first one. "12,50" is written with a comma, which is how the number
# is written in Norwegian and how a lot of exported data arrives. float knows
# nothing about that, so it is a ValueError: a string is a reasonable thing to
# hand to float, this particular string just is not a number.
#
# Compare it with the last one. "3" + 3 is a TypeError, because a string and an
# integer are not the sort of things that can be added at all. Wrong value
# versus wrong kind of thing.
# ---------------------------------------------------------------------------

try:
    float("12,50")
except ValueError as error:
    print(f'float("12,50")   -> ValueError: {error}')

try:
    [1, 2, 3][3]
except IndexError as error:
    print(f"[1, 2, 3][3]     -> IndexError: {error}")

try:
    {"a": 1}["b"]
except KeyError as error:
    print(f'{{"a": 1}}["b"]    -> KeyError: {error}')

try:
    10 / 0
except ZeroDivisionError as error:
    print(f"10 / 0           -> ZeroDivisionError: {error}")

try:
    "3" + 3
except TypeError as error:
    print(f'"3" + 3          -> TypeError: {error}')

print("-" * 20)


# ---------------------------------------------------------------------------
# g) Displays: None
#
# "42" is a perfectly good number, and the function said it was not.
#
# The body says `flooat(text)` with three o's. That raises a NameError, and a
# bare `except:` catches EVERYTHING, so the typo was quietly converted into
# "the input was bad". The function will now reject every string you ever hand
# it and will never once say why.
#
# With `except ValueError:` instead, the NameError is not caught, and the
# program stops with a traceback naming the misspelled function. That is the
# whole argument for naming the exception you expect: anything you did not
# expect is free to interrupt you, and being interrupted is how you find out.
# ---------------------------------------------------------------------------


def read_number(text):
    try:
        return flooat(text)
    except:
        return None


print(read_number("42"))


def read_number_fixed(text):
    try:
        return flooat(text)
    except ValueError:
        return None


try:
    read_number_fixed("42")
except NameError as error:
    print(f"With except ValueError, the real problem surfaces -> NameError: {error}")

print("-" * 20)


# ---------------------------------------------------------------------------
# The two broken functions
# ---------------------------------------------------------------------------

# 1. has_negative returns False.
#
#    The else belongs to the `if` INSIDE the loop, so the function reaches a
#    return on the very first item and never looks at the rest. It reports on
#    values[0] alone.
#
#    A conclusion about a WHOLE list cannot be reached until the loop has
#    finished looking at all of it. So the "yes" answer can be returned early -
#    one negative value settles it - but the "no" answer has to wait until
#    afterwards.


def has_negative(values):
    for value in values:
        if value < 0:
            return True

    return False


print(has_negative([4, 9, -2]))
print(has_negative([4, 9, 2]))


# 2. average returns 0 for a list of strings.
#
#    The empty list is handled correctly, but only by accident. The bare
#    `except:` also catches the TypeError that sum raises when the list holds
#    strings, and reports an average of zero - a number that looks like data,
#    goes into a report, and is believed.
#
#    Catch the exception you actually meant.


def average(values):
    try:
        return sum(values) / len(values)
    except ZeroDivisionError:
        return 0


print(average([4, 9, 2]))
print(average([]))

try:
    print(average(["4", "9"]))
except TypeError as error:
    print(f"TypeError: {error}")


# ---------------------------------------------------------------------------
# The pattern behind (a), (b), broken function 1 and broken function 2
#
# All four are about a return statement in the wrong place, or missing.
#
#   (a) no return at all         -> None
#   (b) return inside the loop   -> answers after one item
#   (1) return inside the loop   -> answers after one item
#   (2) the wrong thing caught   -> answers when it should have stopped
#
# When a function gives a wrong answer rather than an error, check what it
# RETURNS before you check what it computes. A great many "the numbers are
# wrong" bugs are a function that returned None, or returned too early, or
# returned a fallback that nobody realized was a fallback.
#
# And note what (a), (b) and (1) have in common with each other but not with
# (2): nothing raised, nothing was caught, and no message appeared anywhere.
# try / except only helps with problems Python can see. It is no defense at all
# against a program that runs perfectly and is wrong.
# ---------------------------------------------------------------------------
