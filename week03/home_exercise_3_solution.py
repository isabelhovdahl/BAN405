# -*- coding: utf-8 -*-
"""
Week 03 - Home exercise 3: Random code generator

Solution proposal.

Draw a code of random digits of a length chosen by the user, and display it as
a string rather than as a list.
"""

from random import randint, seed


# Setting the seed makes the program produce the same code every time it runs,
# which is what lets you check your output against this file. Comment the line
# out to get a genuinely different code on each run.
seed(405)


# 1. Welcome message, stating what the input has to look like.
print("*" * 47)
print("**** Welcome to the random code generator! ****")
print("*" * 47)
print("This program draws a code of random digits between 0 and 9.")
print("The length must be a whole number that is not negative.\n")


# 2. Ask.
length_text = input("How many digits should the code have? ").strip()


# 3. Check the input. .isdigit() is exactly right here: the welcome message
# promised a whole, non-negative number, and .isdigit() is False for "-4",
# "2.5" and "" alike.
if length_text.isdigit():

    length = int(length_text)

    # 4. Draw the digits.
    #
    # The digits are converted to strings as they go in, so that .join() can
    # use them later. Doing it here rather than at the end keeps the list and
    # the code in the same form and saves a second loop.
    code_digits = []

    for i in range(length):
        digit = randint(0, 9)
        code_digits.append(str(digit))

    # 5. Display it.
    #
    # "".join() with an empty separator glues the pieces together with nothing
    # in between, which is the difference between 481902 and [4, 8, 1, 9, 0, 2].
    code = "".join(code_digits)

    print(f"\nYour code is: {code}")

    # 6. The same list again, in one line.
    #
    # This is a comprehension doing exactly what it is for: one sequence in,
    # one list out, and the whole thing readable in a single breath.
    code_digits = [str(randint(0, 9)) for i in range(length)]

    print(f"And another:  {''.join(code_digits)}")

else:
    print("\nINVALID INPUT")
    print("The length must be a whole number that is not negative.")


# ---------------------------------------------------------------------------
# A length of 0
#
# It should produce an empty code, and it does. range(0) yields no numbers at
# all, so the loop body never runs, the list stays empty, and "".join([]) is
# the empty string. The program displays "Your code is: " and nothing after it.
#
# That is the right behavior rather than a bug, and it is worth noticing that
# nothing in the program had to be written to make it happen. A loop that runs
# zero times is not a special case to be guarded against - it is what a
# correctly written loop does when there is nothing to do.
#
# Test it with:
#     6        -> a six-digit code
#     1        -> a one-digit code
#     0        -> an empty code
#     abc      -> "INVALID INPUT"
#     -3       -> "INVALID INPUT", because "-3".isdigit() is False
#
# What this program does NOT do:
#
# - It does not stop you asking for a code of 100000 digits. Nothing breaks; it
#   just prints for a while.
# - It cannot guarantee the code is unique, or that it does not start with a
#   zero. A real one-time code generator cares about both.
# - The numbers are not truly random. They come from a formula, which is
#   precisely why seed() can make them repeat - useful here, and useless as
#   security.
# ---------------------------------------------------------------------------
