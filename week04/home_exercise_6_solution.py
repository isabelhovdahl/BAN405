# -*- coding: utf-8 -*-
"""
Week 04 - Home exercise 6: A loop that survives bad data

Solution proposal.

Reads a column of messy text readings, sorting each entry into usable, missing
or unreadable, and reports on all three without stopping at the first problem.
"""

MISSING_CODE = -999


# 1. Turn one field of text into a number, or say that it cannot be done.
#
# The function answers exactly one question: can this text be read as a number?
# It knows nothing about -999, about this dataset, or about what the caller
# intends to do with the answer - which is what makes it reusable on the next
# dataset, where the missing-value code will be something else entirely.
#
# .strip() first, so that "  9.8  " is treated as the number it obviously is,
# and so that a field of nothing but spaces is caught by the emptiness test.
def parse_reading(text):
    """
    Return the reading as a number, or None if the text is not a number.

    Parameters
    ----------
    text : str
        One raw field, possibly blank or containing something that is not a
        number.

    Returns
    -------
    float or None
        The reading, or None if the field is blank or cannot be converted.
    """
    cleaned = text.strip()

    if cleaned == "":
        return None

    try:
        return float(cleaned)
    except ValueError:
        return None


def main():
    """Summarize a column of raw readings."""
    rows = ["12.5", "14.0", "-999", "", "13.2", "n/a", "11.0", "  9.8  ", "-999"]

    # 3. The accumulators, all initialized before the loop.
    total = 0
    usable = 0
    missing = 0
    unreadable = 0

    # 2. One pass, three destinations.
    #
    # The order of the tests matters. parse_reading has to run first, because
    # until the text is a number there is no way to compare it with anything.
    # Only then can we ask the question that is about this dataset rather than
    # about text: is this number the code that means "no reading"?
    for row in rows:
        value = parse_reading(row)

        if value is None:
            unreadable += 1
            print(f"  skipping unreadable field: '{row}'")
        elif value == MISSING_CODE:
            missing += 1
        else:
            usable += 1
            total += value

    # 4 and 5. Report.
    print(f"\n{len(rows)} fields read")
    print(f"  usable:     {usable}")
    print(f"  missing:    {missing}")
    print(f"  unreadable: {unreadable}")

    # The guard. Without it, an input where nothing was usable divides by zero
    # - and the whole point of this program is that bad data does not stop it.
    if usable == 0:
        print("\nNo usable readings, so there is no average to report.")
    else:
        print(f"\nAverage of the usable readings: {total / usable:.1f}")


if __name__ == "__main__":
    main()

    print("\n" + "=" * 50)
    print("The same program with nothing usable in the data:\n")

    rows = ["n/a", "", "-999"]

    usable = 0
    for row in rows:
        value = parse_reading(row)
        if value is not None and value != MISSING_CODE:
            usable += 1

    if usable == 0:
        print("No usable readings, so there is no average to report.")


# ---------------------------------------------------------------------------
# Where the line between the function and the loop falls
#
# The single design decision in this program is that parse_reading does not
# know about -999.
#
# It would have been easy to write it the other way, returning None for the
# sentinel as well - one line shorter and the loop would have had two branches
# instead of three. It would also have been wrong, and not because of a rule.
# "This field is not a number" is a fact about text and is true everywhere.
# "-999 means no reading was taken" is a convention that this particular
# organization adopted for this particular file, and the next file will use
# -1, or 9999, or an empty cell, or the word NULL.
#
# Put the convention in the function and the function stops traveling. Put it
# in the loop and both halves are reusable: parse_reading on any text at all,
# and the three-way sort on any sentinel you like.
#
# That is a general shape rather than a trick: a function should know about the
# problem it solves and nothing about the program that calls it.
#
# Things worth noticing:
#
# - Two of the three groups are found by asking a question, and the third is
#   whatever is left over. Writing the tests in the other order - checking for
#   -999 before checking for None - crashes, because None cannot be compared
#   with a number in a useful way.
# - `if value is None` uses `is`, not `==`. Both work here, and `is` is the
#   conventional way to test for None, because there is only ever one None.
# - The guard before the division is not defensive programming for its own
#   sake. It is the same ZeroDivisionError that the average function raised in
#   the lecture, and here an `if` is a better answer than a try / except,
#   because an empty dataset is an expected outcome rather than an error - we
#   know in advance it can happen and exactly what to say about it.
# - The count of unreadable fields is reported rather than silently dropped.
#   Two bad fields out of nine is a data entry problem; two hundred out of nine
#   hundred is a broken export, and you only find that out if somebody counts.
#
# What this program does NOT do:
#
# - It cannot tell the two kinds of nothing apart. parse_reading returns None
#   for a blank field and None for "n/a", so a column that was never filled in
#   looks exactly like a column somebody typed nonsense into. Distinguishing
#   them means returning something richer than None, or raising and letting the
#   caller inspect the exception.
# - -999 is a convention, not a type. A genuine reading of -999 would be
#   counted as missing, and nothing in the data itself can tell the two apart.
#   This is exactly why real datasets eventually stop using sentinel codes and
#   adopt a dedicated missing-value marker instead - which is how the second
#   half of this course represents it.
# - It accepts "inf" and "nan" as usable readings, because float does. Either
#   one poisons the average: the total becomes infinity or nan and stays that
#   way whatever else is added to it.
# - The data is written into the program. Reading it from a file is the obvious
#   next step and needs a tool we have not met yet.
# ---------------------------------------------------------------------------
