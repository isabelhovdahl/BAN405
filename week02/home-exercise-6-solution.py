# -*- coding: utf-8 -*-
"""
Week 02 - Home exercise 6: Leap years

Solution proposal.

A year is a leap year if it is divisible by 4, except that years divisible by
100 are not, unless they are also divisible by 400.
"""

year_text = input("Enter a year: ").strip()


if year_text.isdigit():

    year = int(year_text)

    # The whole rule, in one expression.
    #
    # Read it in the same three pieces the sentence has:
    #
    #     divisible by 4                      year % 4 == 0
    #     ... and not one of the centuries    year % 100 != 0
    #     ... unless it is a 400th year       or year % 400 == 0
    #
    # The brackets around the `or` are what make it work. Without them,
    # `and` binds tighter than `or`, so Python would read the expression as
    #
    #     (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
    #
    # which happens to give the same answers - the 400 rule implies the 4
    # rule - but says something different and is luck rather than logic.
    is_leap = (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0))

    if is_leap:
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")

else:
    print("That is not a whole number.")


# ---------------------------------------------------------------------------
# The four years that matter
#
#   2024   % 4 == 0, % 100 != 0                    ->  leap
#   2023   % 4 != 0                                ->  not leap
#   1900   % 4 == 0, % 100 == 0, % 400 != 0        ->  not leap
#   2000   % 4 == 0, % 100 == 0, % 400 == 0        ->  leap
#
# 2024 and 2023 are decided by the first clause alone, so a wrong expression
# still gets them right. 1900 and 2000 are the two that separate a correct
# expression from a plausible one - which is the general lesson: pick test
# cases that can distinguish between the answers, not test cases that are easy.
#
# The result is stored in `is_leap` rather than printed straight from the
# condition. That is deliberate: the boolean is the answer, and a program that
# needed to do anything else with it - count leap years, decide the length of
# February - already has it.
# ---------------------------------------------------------------------------
