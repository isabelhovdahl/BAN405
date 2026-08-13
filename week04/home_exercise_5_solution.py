# -*- coding: utf-8 -*-
"""
Week 04 - Home exercise 5: Temperature conversion program

Solution proposal.

The temperature converter, written a third time: four functions, and neither
kind of bad input can stop it any more.
"""

ABSOLUTE_ZERO_C = -273.15


# 1. Ask for the scale.
#
# This is the re-prompt loop we already had. The check is a membership test, so
# nothing is converted and no exception can arise - which is exactly why this
# one worked before try / except existed.
#
# .strip() removes stray spaces and .upper() accepts a lowercase answer, so
# "  c  " is treated as "C".
def get_scale():
    """Ask for a conversion direction, and return "C" or "F"."""
    print('\nEnter "F" to convert from Fahrenheit to Celsius')
    print('Enter "C" to convert from Celsius to Fahrenheit')

    while True:
        scale = input("\nEnter selection: ").strip().upper()

        if scale in ("C", "F"):
            return scale

        print('Invalid input! Enter "F" or "C".')


# 2. Ask for the temperature.
#
# This is the one that could not be written before. .isdigit() rejects -40 and
# 98.6, which are both perfectly good temperatures, so there was no way to
# check this input without also refusing half the valid answers.
#
# float does the check by doing the conversion. The return is inside the try
# and inside the while, so it only happens when the conversion succeeded - and
# when it does, it leaves the loop and the function together.
def get_temperature():
    """Ask for a temperature, and return it as a number."""
    while True:
        text = input("\nEnter temperature to convert: ")

        try:
            return float(text)
        except ValueError:
            print("Invalid input! Enter a number.")


# 3. The arithmetic, and nothing else.
#
# This function asks nothing and prints nothing, so it can be tested without a
# keyboard: convert_temperature(100, "C") is 212.0 or it is not.
def convert_temperature(temperature, scale):
    """
    Convert a temperature between Celsius and Fahrenheit.

    Parameters
    ----------
    temperature : float
        The temperature to convert.
    scale : str
        The scale the temperature is currently in, "C" or "F".

    Returns
    -------
    float
        The converted temperature, in the other scale.
    """
    if scale == "C":
        return 9 / 5 * temperature + 32

    return 5 / 9 * (temperature - 32)


# 4. Put the three in order and display the result.
def main():
    """Run the temperature conversion program."""
    print("*" * 54)
    print("Temperature Conversion Program")
    print("This program converts temperatures (Fahrenheit/Celsius)")
    print("*" * 54)

    scale = get_scale()
    temperature = get_temperature()

    converted = convert_temperature(temperature, scale)

    if scale == "C":
        print(f"\n{temperature} degrees Celsius equals {converted:.1f} degrees Fahrenheit.")
    else:
        print(f"\n{temperature} degrees Fahrenheit equals {converted:.1f} degrees Celsius.")

    # The sanity check.
    #
    # It has to be made on the Celsius value, whichever way round the user was
    # working - so we pick whichever of the two numbers is the Celsius one
    # rather than checking the input blindly.
    if scale == "C":
        celsius = temperature
    else:
        celsius = converted

    if celsius < ABSOLUTE_ZERO_C:
        print(f"\nWarning: {celsius:.1f} C is below absolute zero. That reading cannot be right.")


if __name__ == "__main__":
    main()


# ---------------------------------------------------------------------------
# The two kinds of validation, side by side
#
# get_scale and get_temperature have the same shape and check their input in
# completely different ways, and the reason is worth being clear about.
#
#   get_scale        the set of valid answers is two strings, and we can list
#                    them. A membership test answers the question exactly, and
#                    nothing is converted, so nothing can raise.
#
#   get_temperature  the set of valid answers is every number that exists. It
#                    cannot be listed, and no string method describes it - which
#                    is what we found when .isdigit() turned out to reject -40,
#                    98.6 and " 42 ". So we stop asking about the text and try
#                    the conversion instead, and let float report the failure.
#
# The rule that falls out: when you can list the valid answers, test membership.
# When you cannot, attempt the conversion and catch the failure.
#
# Test cases that separate a right answer from a plausible one:
#
#     -40          same in both scales. If your formula is round the wrong way
#                  this is the one input that will not tell you
#     98.6 F       -> 37.0 C, body temperature. Rejected by .isdigit()
#     0 C          -> 32.0 F
#     -300 C       triggers the absolute zero warning
#     -300 F       -> -184.4 C, which is cold but perfectly possible, and must
#                  NOT trigger the warning. Checking the input rather than the
#                  Celsius value gets this one wrong
#     cold         re-prompts instead of crashing
#     Enter alone  re-prompts: "" is not a number either
#     "  c  "      accepted, thanks to .strip().upper()
#
# What this program does NOT do:
#
# - float accepts more than you might want. "1e5" is a hundred thousand
#   degrees, "inf" is infinity and "nan" is not a number at all, and all three
#   are accepted here without complaint. Rejecting them means adding a range
#   check after the conversion, not a cleverer conversion.
# - There is no upper sanity bound. 5000 degrees Celsius is accepted silently,
#   which is hotter than the surface of the sun.
# - The absolute zero check happens after the conversion has been displayed, so
#   the user sees the impossible number first and the warning second. Checking
#   before displaying would be better and would need the two branches of the
#   output to be rearranged.
# - It converts once and stops. Doing several conversions in one run means
#   wrapping main's body in another loop and asking whether the user wants to
#   go again - which is a third re-prompt loop, of the same shape as the first.
# ---------------------------------------------------------------------------
