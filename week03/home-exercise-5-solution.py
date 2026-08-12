# -*- coding: utf-8 -*-
"""
Week 03 - Home exercise 5: The prisoner's dilemma, without giving up

Solution proposal.

The same game as before, but now it asks again instead of stopping when a
player types something invalid. Player A's loop tests at the top; player B's
tests in the middle. Both shapes do the same job.
"""

# A dictionary mapping the two valid answers to the words for them. It saves
# writing those words out four times, and it doubles as the list of valid
# answers - so there is only one place to edit if the rules ever change.
CHOICES = {
    "1": "stay silent",
    "2": "confess"
}


print("*" * 34)
print("Welcome to the prisoner's dilemma.")
print("*" * 34)
print("Press 1 to stay silent, or 2 to confess.")


# ---------------------------------------------------------------------------
# Prisoner A: a plain while loop, tested in the header
#
# The loop cannot test an answer that does not exist yet, so the first question
# has to be asked BEFORE the loop, and the same question asked again at the
# bottom of the body. That duplicated prompt is the cost of this shape.
#
# `not in` on a dictionary checks the keys, which is exactly what we want.
# ---------------------------------------------------------------------------
print("\nPrisoner A, you are up.")
choice_a = input("Your choice (1 or 2): ").strip()

while choice_a not in CHOICES:
    print("Invalid input. Please press 1 or 2.")
    choice_a = input("Your choice (1 or 2): ").strip()


# ---------------------------------------------------------------------------
# Prisoner B: while True with a break, tested in the middle
#
# `while True` is a condition that can never become false, so this loop would
# run forever if the break were not there. The break is the only exit.
#
# In exchange, the question is written once. The test sits naturally between
# asking and complaining, which is where it belongs.
# ---------------------------------------------------------------------------
print("\nPrisoner B, you are up.")

while True:
    choice_b = input("Your choice (1 or 2): ").strip()

    if choice_b in CHOICES:
        break

    print("Invalid input. Please press 1 or 2.")


# ---------------------------------------------------------------------------
# The outcome
#
# The dictionary turns the codes back into words, so the message reads like a
# sentence rather than like a form.
# ---------------------------------------------------------------------------
print(f"\nPrisoner A chose to {CHOICES[choice_a]}.")
print(f"Prisoner B chose to {CHOICES[choice_b]}.\n")

if choice_a == "1" and choice_b == "1":
    print("You both stayed silent: 1 year each.")
elif choice_a == "1" and choice_b == "2":
    print("A stayed silent, B confessed: A gets 3 years, B goes free.")
elif choice_a == "2" and choice_b == "1":
    print("A confessed, B stayed silent: A goes free, B gets 3 years.")
else:
    print("You both confessed: 2 years each.")


# ---------------------------------------------------------------------------
# The two shapes, side by side
#
#     ask                          while True:
#     while answer is bad:             ask
#         complain                     if answer is good:
#         ask                              break
#                                      complain
#
# They are the same loop. The left one tests before the body and therefore has
# to prime the variable first, which means writing the question twice. The
# right one tests in the middle of the body, so it writes the question once and
# pays for it with a loop that has no visible stopping condition.
#
# Neither is more correct. Use the left one when the test is genuinely about
# whether to enter the loop at all; use the right one when the loop naturally
# does something before it can know whether it should stop - which is the case
# whenever the thing being tested has to be fetched first.
#
# Note that both loops re-prompt forever. A user who never types a valid answer
# never gets out, and there is no way to cancel. That is deliberate here, but a
# real program would offer an escape - which is a third thing to test for in
# the condition, not a new kind of loop.
#
# What this program does NOT do:
#
# - It does not let a player quit.
# - It does not hide player A's answer from player B, so the "questioned
#   separately" part of the story survives only by politeness.
# - It accepts stray spaces, because of .strip(), but not "one" or "confess".
#   The dictionary decides what is valid and it holds two strings.
# ---------------------------------------------------------------------------
