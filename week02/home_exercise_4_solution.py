# -*- coding: utf-8 -*-
"""
Week 02 - Home exercise 4: Random number generator

Solution proposal.

Draw a random whole number between two bounds supplied by the user, with the
two ways of getting the input wrong reported separately.
"""

from random import randint


# 1. Welcome message.
#
# It states the rule the input has to satisfy. A program that rejects input
# without ever having said what it wanted is just rude.
print("*" * 49)
print("**** Welcome to the random number generator! ****")
print("*" * 49)
print("This program draws a random number between two bounds.")
print("Both bounds must be whole numbers that are not negative.\n")


# 2. Ask. input() always gives us a string, so `lower` and `upper` are text
# until we decide they are numbers.
lower = input("Enter the lower bound: ")
upper = input("Enter the upper bound: ")


# 3. Are they numbers at all?
#
# .isdigit() is exactly the right tool here, and only because the welcome
# message promised whole, non-negative numbers - it is False for "-3" and for
# "2.5". Had we allowed negative bounds, this check would reject perfectly
# valid input and we would need something else.
if lower.isdigit() and upper.isdigit():

    lower = int(lower)
    upper = int(upper)

    # 4. Only now can we ask about the ordering. Comparing two strings with <=
    # would compare them alphabetically, so "10" <= "9" is True - which is
    # true of the text and nonsense about the numbers.
    if lower <= upper:
        draw = randint(lower, upper)

        print(f"\nYou asked for a random number between {lower} and {upper}.")
        print(f"Your random draw is... {draw}!")

    else:
        print("\nINVALID BOUNDS")
        print("The lower bound cannot be larger than the upper bound.")

else:
    print("\nINVALID BOUNDS")
    print("Both bounds must be whole numbers that are not negative.")


# ---------------------------------------------------------------------------
# Why this has to be nested
#
# The obvious-looking flat version does not work:
#
#     if lower.isdigit() and upper.isdigit() and int(lower) <= int(upper):
#
# It is safe - short-circuiting means int(lower) is never reached when the
# .isdigit() checks fail - but it collapses two different problems into one
# else, so a user who typed "two" and a user who typed the bounds the wrong
# way round get the same message and no idea which mistake they made.
#
# The nesting is not a stylistic choice here. The second question cannot even
# be asked until the first has been answered: int("two") would stop the
# program. That is the test for when nesting is the right shape - not "is this
# complicated", but "does the inner question depend on the outer one".
#
# Test it with:
#     2 and 8      -> a number between 2 and 8
#     8 and 2      -> "lower bound cannot be larger"
#     two and 8    -> "must be whole numbers"
#     (nothing)    -> "must be whole numbers", because "".isdigit() is False
#
# Note that randint includes both ends, so 2 and 8 can both come up. The
# documentation says so; there was no way to guess it.
# ---------------------------------------------------------------------------
