# -*- coding: utf-8 -*-
"""
Week 01 - Home exercise 5: Temperature conversion program

Solution proposal.

Convert a temperature from Fahrenheit to Celsius.

1. Print a welcome message.
2. Ask the user for a temperature in Fahrenheit.
3. Convert using C = (5/9) * (F - 32).
4. Display the result rounded to the nearest whole degree.
"""

# 1. Welcome message.
#
# Telling the user what the program does before asking them for anything is a
# small courtesy that costs three lines. The \n at the end of the last line
# leaves a blank line before the prompt.
print("*" * 40)
print("**** Temperature conversion program ****")
print("*" * 40)
print("This program converts Fahrenheit to Celsius.\n")

# 2. Prompt for input.
#
# input() always returns a string, so we wrap it in float() to get a number we
# can do arithmetic with. Using float rather than int means 98.6 is accepted.
fahrenheit = float(input("Enter a temperature in Fahrenheit: "))

# 3. Convert.
celsius = (fahrenheit - 32) * 5 / 9

# 4. Report.
#
# {celsius:.0f} rounds to the nearest whole degree for display, while `celsius`
# itself keeps its full precision - so if we needed the exact value later, it is
# still there.
print(f"\n{fahrenheit} degrees Fahrenheit is {celsius:.0f} degrees Celsius.")


# ---------------------------------------------------------------------------
# Check it against values you can verify
#
#    32 F  ->    0 C
#   212 F  ->  100 C
#   -40 F  ->  -40 C     (the one temperature where the two scales agree)
#    98.6 F ->   37 C
#
# Always test a program on inputs whose answer you already know. It is the
# cheapest way to catch a formula typed in the wrong order - note that
#     fahrenheit - 32 * 5 / 9
# is a perfectly valid expression and a completely wrong conversion, because
# multiplication happens before subtraction. The brackets are load-bearing.
#
# One thing this program does NOT do is cope with a user who types "cold"
# instead of a number - float() would raise a ValueError and the program would
# stop. Handling that properly, so the program says something helpful instead of
# crashing, is something we come back to later in the course.
# ---------------------------------------------------------------------------
