# -*- coding: utf-8 -*-
"""
Week 02 - Home exercise 5: The prisoner's dilemma

Solution proposal.

Two prisoners choose independently whether to stay silent or to confess. The
program validates both entries and reports the outcome.

    both stay silent         1 year each
    one confesses            the confessor goes free, the other gets 3 years
    both confess             2 years each
"""

# The mapping from what the user types to what it means.
#
# One dictionary does two jobs: it turns "1" into words for the report, and
# its keys are the list of valid entries. Defining it once means the prompt
# below and the messages further down cannot drift apart.
CHOICES = {
    "1": "stay silent",
    "2": "confess"
}


print("*" * 40)
print("Welcome to the prisoner's dilemma.")
print("*" * 40)
print("Press 1 to stay silent, or 2 to confess.\n")

choice_a = input("Prisoner A, what do you choose? ").strip()
choice_b = input("Prisoner B, what do you choose? ").strip()


# Validate both entries before doing anything with either of them.
if choice_a in CHOICES and choice_b in CHOICES:

    print(f"\nPrisoner A chose to {CHOICES[choice_a]}.")
    print(f"Prisoner B chose to {CHOICES[choice_b]}.\n")

    # Four combinations, exactly one of which applies - so this is an elif
    # ladder, not four separate ifs.
    if choice_a == "1" and choice_b == "1":
        print("You both stay silent. Two years between you: 1 year each.")

    elif choice_a == "1" and choice_b == "2":
        print("Prisoner A gets 3 years. Prisoner B goes free.")

    elif choice_a == "2" and choice_b == "1":
        print("Prisoner A goes free. Prisoner B gets 3 years.")

    else:
        print("You both confess. 2 years each.")

else:
    print("\nINVALID CHOICES")
    print('Both prisoners must press either "1" or "2".')


# ---------------------------------------------------------------------------
# Three things worth noticing
#
# 1. The last branch is `else`, not `elif choice_a == "2" and choice_b == "2"`.
#    Once the first three have been ruled out and we already know both entries
#    are valid, there is only one combination left. Writing it as an else also
#    means the ladder cannot silently fall through and print nothing.
#
# 2. The dictionary and the prompt have to agree. If CHOICES said
#    "1": "confess" while the prompt said "press 1 to stay silent", the program
#    would print the opposite of what each player chose while still handing out
#    the right sentences - a bug that is invisible in the payoffs and obvious
#    in the report. Keep the single source of truth and check it once.
#
# 3. The validation is one condition with `and`, not a nested if, because
#    there is only one thing to say when it fails: somebody typed something
#    that is not 1 or 2. Compare with the random number generator, where the
#    two failures needed two different messages and therefore two levels.
#
# The dilemma itself: whatever the other prisoner does, confessing is better
# for you - so both confess and get 2 years each, when staying silent would
# have given them 1 year each. That is the point of the example.
# ---------------------------------------------------------------------------
