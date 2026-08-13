# -*- coding: utf-8 -*-
"""
Week 03 - Home exercise 6: Phonebook

Solution proposal.

Build a dictionary of names and numbers with a sentinel-terminated while loop,
display it, and then search it by the start of the number.
"""

# 1. The dictionary starts empty and grows inside the loop. This is the
# accumulator pattern again, with a dictionary instead of a number or a list.
phonebook = {}


print("*" * 32)
print("Phonebook")
print("*" * 32)
print("Enter a name and a number for each entry.")
print("Press Enter without typing a name to finish.\n")


# ---------------------------------------------------------------------------
# 2. The sentinel loop
#
# The empty string is the sentinel: the value that means "no more data". We
# cannot know in advance how many entries the user will type, so there is no
# sequence for a for loop to walk over. This is what while loops are for.
#
# The condition uses truthiness directly: a non-empty string is truthy and the
# empty string is falsy, so `while name:` reads as "while the user typed
# something". Writing `while name != "":` would be equally correct.
# ---------------------------------------------------------------------------
name = input("Name: ").strip()

while name:
    number = input(f"Number for {name}: ").strip()

    phonebook[name] = number
    print(f"Added {name}.\n")

    name = input("Name: ").strip()


# ---------------------------------------------------------------------------
# 3. Display the finished phonebook
#
# .items() gives the name and the number together, and enumerate supplies the
# line number. Three names in the loop header, and no indexing at all.
# ---------------------------------------------------------------------------
print("\n" + "-" * 32)
print("Your phonebook")
print("-" * 32)

for line_no, (name, number) in enumerate(phonebook.items(), start=1):
    print(f"{line_no}. {name:<15}{number}")


# ---------------------------------------------------------------------------
# 4. Search by the start of the number
#
# This is the search pattern, with one difference: we are not stopping at the
# first match, so there is no break. The flag is still needed, and for the same
# reason as always - after the loop we have to say something, and "nothing
# matched" is a statement about the WHOLE list that no single pass can make.
#
# Note that a dictionary lookup cannot help here. `in` on a dictionary asks
# about a key, and we are asking a question about the values, and not even an
# exact one. That is what a loop is for.
# ---------------------------------------------------------------------------
prefix = input("\nSearch for numbers starting with: ").strip()

found_any = False

for name, number in phonebook.items():
    if number.startswith(prefix):
        print(f"  {name}: {number}")
        found_any = True

if not found_any:
    print("  No numbers start with that.")


# ---------------------------------------------------------------------------
# The empty phonebook
#
# Press Enter immediately and the while loop runs zero times, because the
# condition is false before the first pass. Everything after it still works:
# the display loop runs zero times, the search loop runs zero times, and
# found_any stays False so the user is told nothing matched.
#
# Not one of those three is a special case that had to be written. A loop over
# an empty collection does nothing, which is almost always the right answer,
# and it is worth trusting rather than guarding against.
#
# Test it with:
#     three entries, then a prefix matching two of them
#     a prefix matching none          -> "No numbers start with that."
#     Enter pressed immediately       -> an empty phonebook, no crash
#     an empty prefix                 -> every entry, because every string
#                                        starts with the empty string
#
# What this program does NOT do:
#
# - Entering the same name twice overwrites the first number rather than
#   keeping both, because a dictionary key is unique. A phonebook where one
#   person can have two numbers needs a list as the value.
# - It does not check that the number is a number, or that it has a sensible
#   length. Anything typed is accepted.
# - It forgets everything when the program ends. Keeping the phonebook between
#   runs means writing it to a file, which comes later in the course.
# - The empty prefix matching everything is a genuine quirk of .startswith()
#   rather than a bug here, but a real search box would probably want to
#   refuse it.
# ---------------------------------------------------------------------------
