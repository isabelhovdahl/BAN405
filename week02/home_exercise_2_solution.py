# -*- coding: utf-8 -*-
"""
Week 02 - Home exercise 2: Password strength

Solution proposal.

Check a password against four rules, report each rule separately, combine them
into a single verdict.

To test the other passwords, change the value on the first line and run the
program again.
"""

password = "CopyCat1337"


# 1. The four rules, one variable each.
#
# Naming each rule is not decoration. It means the combined test on the next
# page reads like the specification, and it means that when one of them is
# wrong you can see which.

long_enough = len(password) >= 8

# "Contains at least one uppercase letter."
#
# NOT `not password.islower()`. .islower() requires at least one cased
# character, so it is False for "1337" - which has no letters at all - and
# `not` would then claim there is a capital in there.
#
# A string contains an uppercase letter exactly when lowercasing it changes it.
has_upper = password != password.lower()

# "Is not made up entirely of letters", i.e. there is at least one digit or
# symbol somewhere. .isalpha() is True only when every character is a letter.
not_only_letters = not password.isalpha()

# "Does not start with a digit."
#
# The order inside the brackets matters: password[0] would raise an IndexError
# on the empty password, so the length check has to come first and let
# short-circuiting stop the rest.
no_leading_digit = not (len(password) > 0 and password[0] in "0123456789")


# 2. Report each rule.
print(f"Checking the password: {password}")
print(f"  at least 8 characters:      {long_enough}")
print(f"  has an uppercase letter:    {has_upper}")
print(f"  not only letters:           {not_only_letters}")
print(f"  does not start with digit:  {no_leading_digit}")


# 3. Combine.
#
# The rules are already booleans, so there is no if statement to write here -
# `and` does the whole job.
strong = long_enough and has_upper and not_only_letters and no_leading_digit


# 4. The verdict.
print()

if strong:
    print("Strong password.")
elif long_enough:
    print("Long enough, but it breaks at least one of the other rules.")
else:
    print("Too short.")


# ---------------------------------------------------------------------------
# What the five test passwords give
#
#   password       long  upper  not only letters  no leading digit   verdict
#   ------------   ----  -----  ----------------  ----------------   -------
#   "CopyCat1337"  True  True   True              True               strong
#   "copycat"      False False  False             True               too short
#   "12345678"     True  False  True              False              long enough
#   "Bergen!!"     True  True   True              True               strong
#   ""             False False  True              True               too short
#
# Two of these are worth a second look.
#
# "12345678" passes "not only letters" and fails everything else that matters.
# A rule set is only as good as the passwords it rejects, and this one lets a
# lot through - real strength checks also test against lists of common
# passwords, which is a different kind of problem entirely.
#
# The empty string passes "not only letters", because .isalpha() is False for
# an empty string and we negated it. That is defensible but it is an accident
# rather than a decision, and it is exactly the kind of edge case that only
# turns up if you actually test it.
#
# Note also that nothing here needed an if statement until step 4. Steps 1 to 3
# are boolean expressions assigned to names. Reaching for an if to produce a
# True or a False is almost always a sign that the expression itself was the
# answer.
# ---------------------------------------------------------------------------
