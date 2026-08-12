# -*- coding: utf-8 -*-
"""
Week 03 - Home exercise 2: for versus while

Solution proposal.

Sum the first N whole numbers three ways: with a for loop, with a while loop,
and with no loop at all.
"""

# 1. Welcome message. It states the rule the input has to satisfy, because a
# program that rejects input without having said what it wanted is just rude.
print("*" * 46)
print("**** Sum of the first N whole numbers ****")
print("*" * 46)
print("This program adds up 1 + 2 + 3 + ... + N.")
print("N must be a positive whole number.\n")


# 2. Ask. input always hands back a string, so N is text until we decide
# otherwise.
n_text = input("Enter N: ").strip()


# 3. Is it a whole number at all?
#
# .isdigit() is the right check here only because the welcome message promised
# a positive whole number - it is False for "-4" and for "2.5", which is
# exactly what we want and would be exactly wrong if negatives were allowed.
if n_text.isdigit():

    N = int(n_text)

    # The second question can only be asked once we know we have a number.
    # "0".isdigit() is True, so zero gets through the first check and has to be
    # rejected here. Nesting keeps the two failures reportable separately.
    if N > 0:

        # ------------------------------------------------------------------
        # Version 1: a for loop
        #
        # range(1, N + 1) is the whole trick. The stop value is excluded, so
        # writing N would stop one short and quietly give the wrong answer.
        # ------------------------------------------------------------------
        total_for = 0

        for num in range(1, N + 1):
            total_for += num

        print(f"\nUsing a for loop:   {total_for}")

        # ------------------------------------------------------------------
        # Version 2: a while loop
        #
        # Everything range did for us now has to be done by hand: start the
        # counter, test it, and remember to move it on. Forget the last line
        # and the program never finishes.
        # ------------------------------------------------------------------
        total_while = 0
        num = 1

        while num <= N:
            total_while += num
            num += 1

        print(f"Using a while loop: {total_while}")

        # ------------------------------------------------------------------
        # Version 3: no loop at all
        #
        # range produces the numbers and sum adds them up. Nothing is written
        # by hand, so there is nothing to get wrong except the bounds.
        # ------------------------------------------------------------------
        print(f"Using sum and range: {sum(range(1, N + 1))}")

    else:
        print("\nINVALID INPUT")
        print("N must be greater than zero.")

else:
    print("\nINVALID INPUT")
    print("N must be a positive whole number.")


# ---------------------------------------------------------------------------
# Which one would you actually ship?
#
# The third, every time. It says what it means in one line and there is no
# counter to initialize, no stop value to get wrong and no update line to
# forget.
#
# The for loop is the one to write when the body does something sum cannot -
# printing a table as it goes, skipping some of the numbers, accumulating two
# things at once.
#
# The while loop is the wrong tool for this task and is here only to show what
# a for loop is doing on your behalf. Every line of bookkeeping in it is a line
# range writes for you. Note that this is a DEFINITE loop - the number of
# passes is settled before it starts - which is the clearest possible signal
# that a for loop was the right choice.
#
# Test it with:
#     10       -> 55
#     1        -> 1
#     0        -> "N must be greater than zero"
#     five     -> "N must be a positive whole number"
#     (blank)  -> the same, because "".isdigit() is False
#
# What this program does NOT do:
#
# - It does not accept a negative N, and it should not: the sum of the first -3
#   whole numbers is not a thing.
# - It does not accept "10.0", or " 10 " with the spaces left in by something
#   other than our .strip(), or a number typed with a thousands separator.
#   .isdigit() rejects all of them.
# - It gives up after one wrong answer instead of asking again. Exercises 5 and
#   6 fix that; the loop that does it is the same one you use here.
# ---------------------------------------------------------------------------
