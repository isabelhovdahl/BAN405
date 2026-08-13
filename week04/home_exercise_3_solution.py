# -*- coding: utf-8 -*-
"""
Week 04 - Home exercise 3: Random character, and a code generator

Solution proposal.

Builds a random code out of two functions: one that draws a single character
from any sequence, and one that uses it repeatedly.
"""

import random
from random import randint


# 1 and 2. Draw one character.
#
# The empty sequence has to be decided, not discovered. Three answers were
# defensible; this one returns None, for the reason argued in the commentary at
# the bottom.
def random_character(characters):
    """
    Return one character chosen at random from a sequence of characters.

    Parameters
    ----------
    characters : str
        A string of characters to choose from.

    Returns
    -------
    str or None
        A single character, or None if the sequence is empty.
    """
    if len(characters) == 0:
        return None

    position = randint(0, len(characters) - 1)

    return characters[position]


# 3. Build a code out of repeated draws.
#
# make_code does not know how to draw a random digit and does not need to. It
# knows which alphabet it wants and how many characters it wants, and it asks
# random_character for the rest. That division is what makes random_character
# worth keeping.
def make_code(length):
    """
    Return a code of `length` random digits, as a single string.

    Parameters
    ----------
    length : int
        The number of digits in the code. Zero gives an empty string.

    Returns
    -------
    str
        The code.
    """
    digits = "0123456789"

    code = ""

    # The loop variable is never used - we want `length` draws, not the
    # numbers themselves. An underscore is the conventional name for a value
    # you are deliberately ignoring.
    for _ in range(length):
        code += random_character(digits)

    return code


if __name__ == "__main__":

    # Fixed seed so this file prints the same thing every time it is run.
    random.seed(405)

    # 5. Three lengths.
    print(f"Length 6: {make_code(6)}")
    print(f"Length 1: {make_code(1)}")

    # A length of 0 should give an empty string - a code with no digits in it.
    # There is nothing special to write for this: range(0) runs zero times, so
    # the loop never executes and `code` is still "". A loop over an empty
    # sequence doing nothing is almost always the right answer.
    print(f"Length 0: '{make_code(0)}'")

    # Confirm the function is not secretly specific to digits.
    letters = "abcdefghijklmnopqrstuvwxyz"
    print(f"\nRandom letter: {random_character(letters)}")
    print(f"Random digit:  {random_character('0123456789')}")
    print(f"Empty string:  {random_character('')}")


# ---------------------------------------------------------------------------
# The empty-sequence decision
#
# Try the "do nothing special" version first, as the exercise asked:
#
#     def random_character(characters):
#         position = randint(0, len(characters) - 1)
#         return characters[position]
#
# Most people expect an IndexError. You get a ValueError instead, from randint:
#
#     ValueError: empty range in randint(0, -1)
#
# The indexing never happens. randint(0, -1) is asked for a number between 0
# and -1, there is no such number, and it gives up before characters[position]
# is ever reached. Worth seeing once, because it is a small example of a large
# habit: check which exception you actually get rather than the one that seems
# obvious. Writing `except IndexError:` here would have caught nothing.
#
# The three options, and what each costs:
#
#   return ""     Reads well on its own and is a disaster in make_code, because
#                 code += "" silently produces a code that is shorter than it
#                 was asked for, with nothing anywhere reporting a problem.
#
#   return None   code += None raises a TypeError at once. The message points
#                 at make_code rather than at the empty alphabet that caused
#                 it, but it is loud, immediate, and impossible to ignore.
#
#   let it raise  Also loud and immediate, and needs no code at all. The only
#                 real objection is the misleading ValueError text above, which
#                 talks about ranges rather than about an empty sequence.
#
# None was chosen here because a function that answers "there is no answer"
# should say so with a value that cannot be mistaken for one, and "" is exactly
# such a mistake waiting to happen. Letting it raise would have been an equally
# good answer, and returning "" would not.
#
# The general shape of this: a function that cannot do its job must fail in a
# way the CALLER cannot overlook. Returning something plausible is the one
# option that fails that test.
#
# What this program does NOT do:
#
# - make_code does not check its argument. make_code(-3) returns an empty
#   string, because range(-3) runs zero times - it does not complain that a
#   code of minus three digits was requested. make_code("6") raises a TypeError
#   from range, which is at least loud.
# - It never checks that random_character returned something usable, so an
#   empty alphabet turns into a TypeError from `code += None` rather than into
#   a sentence explaining the problem.
# - Codes drawn this way can repeat digits and can come out as 000000, which is
#   correct behavior for a random code and wrong for, say, a lottery draw.
# - `random` is not suitable for anything that has to be genuinely
#   unguessable. It is designed to be fast and reproducible, which is the
#   opposite of what security needs, and Python has a separate module for that.
# ---------------------------------------------------------------------------
