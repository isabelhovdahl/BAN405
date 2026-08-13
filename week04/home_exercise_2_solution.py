# -*- coding: utf-8 -*-
"""
Week 04 - Home exercise 2: Effective interest rate

Solution proposal.

Compares two savings offers with different compounding frequencies by turning
each nominal rate into the effective annual rate it really pays.
"""


# 1 and 2. The function, with a default and a docstring.
#
# The default of n = 1 is the case where interest is paid once a year, which
# changes nothing: (1 + r/1)**1 - 1 is just r. So the default makes the
# function usable for an ordinary rate without thinking about compounding at
# all, and the parameter is there for when it matters.
def eff_interest_rate(r, n=1):
    """
    Return the effective annual interest rate.

    Parameters
    ----------
    r : float
        The nominal annual interest rate, as a decimal, so 0.059 for 5.9%.
    n : int, optional
        The number of times per year that interest is compounded. Default is 1.

    Returns
    -------
    float
        The effective annual rate, as a decimal.
    """
    return (1 + r / n) ** n - 1


if __name__ == "__main__":

    # 3 and 5. One call positional, one with keyword arguments.
    #
    # The function returns a decimal. Multiplying by 100 for display is done
    # here, in the calling code, and not inside the function - a function that
    # returns a percentage is a function that has decided how it will be shown.
    quarterly = eff_interest_rate(0.059, 4)
    twice_a_year = eff_interest_rate(r=0.06, n=2)

    print("Offer (i):  5.9% paid quarterly")
    print(f"            effective rate {100 * quarterly:.2f}%\n")

    print("Offer (ii): 6.0% paid twice a year")
    print(f"            effective rate {100 * twice_a_year:.2f}%\n")

    # 4. Let the program do the comparison.
    if quarterly > twice_a_year:
        print("Offer (i) is better.")
    elif twice_a_year > quarterly:
        print("Offer (ii) is better.")
    else:
        print("The two offers are equally good.")

    # Checking the default: compounding once a year should change nothing.
    print(f"\nCheck: eff_interest_rate(0.06) = {eff_interest_rate(0.06)}")


# ---------------------------------------------------------------------------
# Things worth noticing
#
# The headline rates rank the offers the wrong way round. 5.9% looks worse than
# 6%, and paid quarterly it comes to 6.03% against 6.09% - so 6% twice a year
# still wins, but by far less than the headline suggests. Compounding four
# times instead of twice is worth about a seventh of a percentage point here.
# That is the entire reason the effective rate exists as a concept, and it is
# why banks are required to quote it.
#
# The function is five lines long, and four of them are the docstring. That is
# not a bad ratio. The formula is the easy part; remembering a year later that
# `r` is a decimal rather than a percentage is the hard part, and the docstring
# is the only place that is written down.
#
# Notice which one has the default. `r` could not have one - there is no
# sensible interest rate to guess - and Python would refuse the definition
# anyway, because a parameter with a default cannot come before one without.
# The order of the parameters and the choice of default are the same decision.
#
# The check at the end does not print 0.06. It prints 0.06000000000000005,
# because (1 + 0.06/1)**1 - 1 adds 1 and then takes it away again, and a float
# does not always survive the round trip. Algebraically the answer is exactly
# 0.06; in binary it is not. This is the same limited precision that made
# 0.1 + 0.2 == 0.3 come out False, and it is why a test like
# `eff_interest_rate(0.06) == 0.06` would fail while being perfectly right.
# Compare floats with round() or with a tolerance, never with ==.
#
# What this program does NOT do:
#
# - It does not check that its inputs make sense. eff_interest_rate(0.06, 0)
#   raises a ZeroDivisionError, and eff_interest_rate(0.06, -2) cheerfully
#   returns a negative effective rate for a positive nominal one. Compounding
#   a negative number of times a year is meaningless, and nothing here says so.
# - It assumes the rate is given as a decimal. Pass 5.9 instead of 0.059 and
#   it returns an effective rate of 3652%, with no complaint at all. A function
#   cannot tell the difference between a number that is wrong and a number that
#   is large, and this is the kind of mistake no exception will ever catch for
#   you - only the docstring says which unit is meant.
# - It compares the two offers on the interest rate alone. Fees, minimum
#   balances, notice periods and whether the rate is fixed all matter more in
#   practice than a seventh of a percentage point.
# ---------------------------------------------------------------------------
