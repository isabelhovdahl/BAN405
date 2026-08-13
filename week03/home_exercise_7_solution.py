# -*- coding: utf-8 -*-
"""
Week 03 - Home exercise 7: Text statistics

Solution proposal.

Split a paragraph into words and report on it, ending with a nested loop that
counts how many words contain each vowel.
"""

text = """The quick brown fox jumps over the lazy dog.
Bergen is the second largest city in Norway, and it rains
there rather a lot. Programming is mostly a matter of
breaking a large problem into smaller problems."""


# ---------------------------------------------------------------------------
# Split, then clean
#
# .split() with no argument splits on any run of whitespace and discards the
# empties, so the line breaks in the triple-quoted string need no special
# handling at all.
#
# Splitting leaves the punctuation attached, though: "dog." would otherwise
# count as four letters and "Norway," as seven. .strip(".,") removes any of
# those characters from both ends - the same .strip() as always, given
# something specific to remove instead of whitespace.
#
# The cleaning is done once, into a new list, so that every question below asks
# about the same words. Doing it inside each loop instead would work and would
# be four chances to do it slightly differently.
# ---------------------------------------------------------------------------
words = []

for raw_word in text.split():
    words.append(raw_word.strip(".,").lower())


# 1. How many words.
print(f"Words: {len(words)}")


# ---------------------------------------------------------------------------
# 2. The longest word
#
# The search pattern without a break, because we are looking for the best match
# rather than the first one and cannot know we have it until the end.
#
# longest starts as the empty string rather than as words[0], so the loop also
# behaves sensibly on an empty text. A plain > means the first of several
# equally long words wins.
# ---------------------------------------------------------------------------
longest = ""

for word in words:
    if len(word) > len(longest):
        longest = word

print(f"Longest word: {longest} ({len(longest)} letters)")


# ---------------------------------------------------------------------------
# 3. Average word length
#
# A sum accumulator over the lengths, divided at the end. Note that the
# division happens AFTER the loop - averaging as you go is a different and much
# harder problem.
# ---------------------------------------------------------------------------
total_letters = 0

for word in words:
    total_letters += len(word)

print(f"Average word length: {total_letters / len(words):.1f}")


# ---------------------------------------------------------------------------
# 4. Words longer than four letters
#
# continue deals with the short words at the top and leaves the rest of the
# body at one level of indentation. With a body this small an `if len(word) > 4`
# would read just as well; the shape earns its keep once the body is longer.
# ---------------------------------------------------------------------------
long_words = 0

for word in words:
    if len(word) <= 4:
        continue

    long_words += 1

print(f"Words longer than four letters: {long_words}")


# ---------------------------------------------------------------------------
# 5. Vowel counts: the nested loop
#
# The outer loop walks the words; for each word, the inner loop walks the five
# vowels. Five passes of the inner loop for every one pass of the outer, so the
# body runs 5 x len(words) times.
#
# vowel_counts is initialized BEFORE the outer loop, because it accumulates
# across all the words. Contrast the average-per-student example in the
# lecture, where the total had to be reset inside the outer loop - the rule is
# always the same question: does this variable start again for each outer pass,
# or not?
#
# The counter is a dictionary rather than five separate variables, which is
# what makes the inner loop possible at all: `vowel_counts[vowel] += 1` says
# "add one to whichever vowel we are on", and five named variables could not.
# ---------------------------------------------------------------------------
vowel_counts = {
    "a": 0,
    "e": 0,
    "i": 0,
    "o": 0,
    "u": 0
}

for word in words:
    for vowel in vowel_counts:
        if vowel in word:
            vowel_counts[vowel] += 1

print("\nWords containing each vowel:")

for vowel, count in vowel_counts.items():
    print(f"  {vowel}: {count}")


# ---------------------------------------------------------------------------
# Note what the vowel count actually measures
#
# It counts WORDS CONTAINING the vowel, not occurrences of it - "problems" adds
# one to "o" even though it holds two. That is what the exercise asked for, and
# the reason it is a nested loop with an `if` rather than a nested loop with a
# counter: `in` answers "is it there at all" and stops looking.
#
# Counting occurrences instead would mean looping over the characters of the
# word rather than testing membership:
#
#     for character in word:
#         if character in vowel_counts:
#             vowel_counts[character] += 1
#
# which is a single loop over characters, not a nested loop at all. Worth
# noticing: the two questions look almost identical in English and have quite
# different shapes in code.
#
# What this program does NOT do:
#
# - It crashes on an empty text, at the division in step 3. Everything else
#   survives an empty word list; the average is the one calculation that has no
#   answer when there is nothing to average.
# - .strip(".,") does not remove semicolons, quotation marks, brackets or
#   dashes, so a text with any of those still has punctuation glued to some
#   words.
# - It treats "the" and "The" as the same word, because of .lower(), but it
#   also treats "dog" and "dogs" as different ones. Deciding what counts as
#   "the same word" is most of the work in real text analysis.
# - y is not counted as a vowel. That is a choice, not an oversight.
# ---------------------------------------------------------------------------
