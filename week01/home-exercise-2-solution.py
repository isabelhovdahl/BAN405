# -*- coding: utf-8 -*-
"""
Week 01 - Home exercise 2: Tidy up a booking reference

Solution proposal.

A booking reference has arrived from another system with stray whitespace:

    booking = "   nhh-2026-oslo-bergen-0087   "

1. Display the length of the string as it arrived.
2. Strip the whitespace, store it in `reference`, and display its length.
3. Extract the year, origin, destination and booking number by slicing.
4. Display a summary line built with an f-string.
"""

booking = "   nhh-2026-oslo-bergen-0087   "

# 1. Length as it arrived
print(f"Length as received: {len(booking)}")

# 2. Remove leading and trailing whitespace
reference = booking.strip()

print(f"Length after strip: {len(reference)}")
print(reference)

# 3. Extract the parts by slicing
#
#    n  h  h  -  2  0  2  6  -  o  s  l  o  -  b  e  r  g  e  n  -  0  0  8  7
#    0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
#
# Remember that the stop index is excluded, so [4:8] gives exactly 4 characters.

year = reference[4:8]
origin = reference[9:13]
destination = reference[14:20]
number = reference[-4:]          # counting from the end is safest for the tail

print(f"Year:        {year}")
print(f"Origin:      {origin}")
print(f"Destination: {destination}")
print(f"Number:      {number}")

# 4. Summary line
#
# .upper() gives us OSLO and BERGEN. Note that we have to call it on the
# extracted pieces, not on `reference`, since we only want part of it in caps.

print(f"\nBooking {number}: {origin.upper()} to {destination.upper()} in {year}")


# ---------------------------------------------------------------------------
# Alternative for step 3
#
# The reference is a sequence of fields separated by dashes, and Python has a
# string method that splits on a separator - which is far less fragile than
# counting characters. We come back to it later in the course:
#
#     parts = reference.split("-")
#     year, origin, destination, number = parts[1], parts[2], parts[3], parts[4]
#
# Slicing is the right tool when the positions are fixed and guaranteed
# (product codes, dates, account numbers). Splitting is the right tool when the
# fields can vary in length.
# ---------------------------------------------------------------------------
