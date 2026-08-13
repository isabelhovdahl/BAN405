# -*- coding: utf-8 -*-
"""
Week 02 - Home exercise 3: Temperature conversion, in either direction

Solution proposal.

1. Show a menu.
2. Ask which direction to convert in, and validate the answer.
3. Ask for the temperature and convert it.
4. Warn if the result is below absolute zero.
"""

# 1. The menu.
#
# If a program is going to reject an answer, it has to say what a good answer
# looks like first.
print("*" * 46)
print("****  Temperature conversion program      ****")
print("*" * 46)
print("Enter F to convert Fahrenheit -> Celsius")
print("Enter C to convert Celsius -> Fahrenheit\n")


# 2. Ask, and normalize before comparing.
#
# .strip() removes stray spaces, .upper() removes the difference between "c"
# and "C". Doing both means the user does not have to guess our formatting.
choice = input("Enter your selection: ").strip().upper()


# 3. Validate with `in`, which is the tidiest way to check a value against a
# short list of allowed options.
if choice in ("F", "C"):

    temperature = float(input("Enter the temperature to convert: "))

    if choice == "F":
        celsius = (temperature - 32) * 5 / 9
        print(f"\n{temperature} degrees Fahrenheit is {celsius:.1f} degrees Celsius.")

    else:
        celsius = temperature
        fahrenheit = (9 / 5) * temperature + 32
        print(f"\n{temperature} degrees Celsius is {fahrenheit:.1f} degrees Fahrenheit.")

    # 4. The sanity check.
    #
    # Both branches above leave the Celsius value in `celsius`, whichever
    # direction we converted in, so one check covers both cases. Writing the
    # test twice - once per branch - would be two places to keep in step.
    if celsius < -273.15:
        print("\nWarning: that is below absolute zero, so the reading cannot be right.")

else:
    print("\nINVALID SELECTION")
    print('You must enter either "F" or "C".')


# ---------------------------------------------------------------------------
# Check it against values you can verify
#
#    F, 32     ->    0.0 C
#    C, 100    ->  212.0 F
#    C, -300   -> -508.0 F, plus the absolute-zero warning
#    x         -> invalid selection
#
# Two things this program does NOT do.
#
# It does not cope with a user who types "cold" instead of a number: float()
# stops the program with a ValueError. You cannot fix that with .isdigit(),
# because .isdigit() is False for "-40" and for "98.6", which are both
# perfectly good temperatures - so the check would reject more valid input
# than invalid. The tool for this is error handling, and it comes later in the
# course. Leaving the gap is the right call for now; papering over it with a
# check that rejects negative temperatures would be worse than the crash.
#
# It also stops after one conversion. Asking again until the user gives a
# valid answer needs a loop, which you have not met yet.
# ---------------------------------------------------------------------------
