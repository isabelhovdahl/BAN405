# Week 03 — Home exercises

Work through these before the next lecture. They cover everything from [`03-loops.ipynb`](03-loops.ipynb): `for` loops and `range`, the accumulator pattern, `break` and `continue`, `enumerate` and `zip`, looping over dictionaries, `while` loops, nested loops, `.split()` and `.join()`, and list comprehension.

Create your own **scripts** for your answers. Solution proposals are in this folder as `home_exercise_N_solution.py`. Try each exercise properly before you open them.

> 💡 **Tip:** Several of these programs ask the user to type something. Write them as **scripts** rather than notebooks — in a notebook the prompt appears at the top of the window rather than under the cell, which gets tiresome once a program asks three questions in a row.

---

## Before you start

Three things the lecture did not cover. Exercise 7 needs the first, exercise 3 is easier with the second, and the third is worth reading before you run any `while` loop of your own.

### Writing a string over several lines

A normal string has to fit on one line. A string delimited by **triple** quotes does not, and it keeps the line breaks you typed:

```python
report = """Bergen is the second largest city in Norway.
It is known for rain, fish and seven mountains."""

print(report)
```

This is the easiest way to paste a paragraph into a program.

> 📝 **Note:** `.split()` with no argument splits on *any* whitespace, and a newline is whitespace. So a triple-quoted paragraph splits into words exactly as a single-line string would — the line breaks need no special handling.

### Making a random program repeatable

`randint` does not produce truly random numbers. It produces them with a formula, starting from a value called the **seed**, which Python normally picks for you from the clock. Set the seed yourself and you get the same sequence every single time:

```python
import random

random.seed(405)

print(random.randint(1, 6))
print(random.randint(1, 6))
```

Run that twice. You get the same two numbers both times.

That is not a way of cheating at dice — it is how you debug a program whose output changes on every run, and it is how you let somebody else reproduce exactly what you got. 

### If your loop runs away

You will write a loop that never stops. It is not a matter of if.

- In a **notebook**, use the interrupt button beside the cell, as in the lecture.
- In a **script** running in the console, press `Ctrl` + `C` in the console.

The habit that prevents most of them: before you run a `while` loop for the first time, find the line inside it that changes the variable in the condition. If there is no such line, do not run it.

---

## 📚 Exercise 1: Predict the output

For each snippet below, write down what you think it will display **before** you run it. Then run it and check.

Where your prediction was wrong, work out which rule from the lecture explains the real answer — that is the whole point of the exercise.

**a)**

```python
prices = [100, 200, 300]

for price in prices:
    price = price + 50

print(prices)
```

**b)**

```python
for num in [1, 2, 3, 4]:
    total = 0
    total += num

print(total)
```

**c)**

```python
print(range(3))
print(list(range(3)))
print(len(range(1, 5)))
```

**d)** **Do not run this one.** Work it out on paper instead.

```python
which = "C"

while which != "F" or which != "C":
    print("Invalid input.")
    which = "F"
```

Why does this loop never end — whatever value `which` is given? Then write a condition that is `True` exactly when `which` is neither `"F"` nor `"C"`, and check it on `"F"`, `"C"` and `"x"`.

**e)**

```python
for row in [[1, 2], [3, 4], [5, 6]]:
    for value in row:
        if value == 3:
            break

        print(value)
```

**f)**

```python
squares = [print(num ** 2) for num in [1, 2, 3]]

print(squares)
```

**g)**

```python
print("a,,b".split(","))
print("  a  b  ".split())
print("".split(","))
```

### Then: two broken loops

Each of the two snippets below runs without an error and gives the wrong answer. Say what is wrong with it, and write a corrected version.

```python
# 1 - meant to add up the whole numbers from 1 to 10
total = 0

for num in range(1, 10):
    total += num

print(total)
```

```python
# 2 - meant to report whether the list contains a negative number
values = [4, 9, 2, 7]

for value in values:
    if value < 0:
        print("Found a negative number.")
    else:
        print("No negative numbers.")
```

---

## 📚 Exercise 2: `for` versus `while`

When the number of passes is known in advance, a `for` loop is the better choice. But most tasks can be written either way, and writing one both ways is a good way to see what the `while` loop is doing by hand.

Write a program that asks the user for a positive whole number `N` and displays the sum of the first `N` whole numbers, that is 1 + 2 + 3 + ... + N.

The program should:

1. Display a short welcome message saying what it does, and stating that `N` must be a **positive whole number**.
2. Ask for `N` and check that it really is one. If it is not, display a message saying so, and stop.
3. Calculate the sum with a **`for`** loop and display it.
4. Calculate the same sum again with a **`while`** loop and display it.
5. Calculate it a third time in a single line, without any loop at all, using `sum` and `range`.

Test it with 10 (the answer is 55), with 1, with `0`, and with `five`.

> 💡 **Tip:** `.isdigit()` is the right check here and only because the welcome message promised a positive whole number. Remember that `"0".isdigit()` is `True`, so "positive" needs a test of its own.

---

## 📚 Exercise 3: Random code generator

In the previous set of exercises you wrote a program that drew a single random number. Extend it so that it draws a whole **code** — a string of random digits, like the ones a bank sends you.

The program should:

1. Display a welcome message saying what it does, and stating that the length must be a whole, non-negative number.
2. Ask the user how many digits the code should have, and check the input. If it is not valid, display a message saying so, and stop.
3. Use a `for` loop and `randint` to draw that many random digits between 0 and 9, storing each one in a list.
4. Display the code as a **single string** — `481902`, not `[4, 8, 1, 9, 0, 2]`. Use `.join()`.
5. Finally, build the same list again in one line with a list comprehension, and check that it works the same way.

Test it with `6`, with `1`, with `0`, and with `"abc"`. Say in a comment what a length of 0 should reasonably produce, and check that your program actually does that.

> 💡 **Tip:** `.join()` refuses to join numbers. You will have to convert each digit to a string somewhere — either as you build the list, or as you join it.

---

## 📚 Exercise 4: The receipt, finished

In the first set of exercises you printed a receipt for three items, and you had to write the three item lines out by hand because you had no loops. Now you do.

```python
items = ["Espresso machine", "Coffee beans", "Oat milk"]
quantities = [1, 2, 3]
unit_prices = [4999.00, 149.90, 24.50]
```

Write a program that prints the receipt. It should:

1. Print a banner made of 40 asterisks, the shop name, and another banner.
2. Print one line per item, **numbered**, showing the item name, the quantity, the unit price and the line total, with all amounts to two decimals and the columns lined up.
3. Accumulate the subtotal **in the same loop** rather than working it out separately.
4. Print the subtotal, the VAT at 25% of the subtotal, and the total including VAT, showing the total with a thousands separator.
5. Finish by reporting which item contributed the largest line total, and how much it was.

Then add a fourth item to the three lists and run it again. Nothing except the data should need to change — if something does, that part of your program is doing by hand what the loop should be doing.

> 💡 **Tip:** The three lists belong together by position, so `zip` walks all three at once: `for item, quantity, price in zip(items, quantities, unit_prices):`. To number the lines as well, wrap the whole thing in `enumerate`, or keep a counter of your own.

---

## 📚 Exercise 5: The prisoner's dilemma, without giving up

In the previous set of exercises you wrote the prisoner's dilemma, and it stopped dead as soon as somebody typed something other than `1` or `2`. Fix that: keep asking until each player has made a valid choice.

The sentences, as before:

|  | **B stays silent** | **B confesses** |
|---|---|---|
| **A stays silent** | A: 1 year<br>B: 1 year | A: 3 years<br>B: goes free |
| **A confesses** | A: goes free<br>B: 3 years | A: 2 years<br>B: 2 years |

The program should:

1. Display a welcome message and explain the two options: press `1` to stay silent, `2` to confess.
2. Ask prisoner A for a choice, re-prompting until it is valid. Write this one as a plain `while` loop with the test in the header.
3. Ask prisoner B for a choice, re-prompting until it is valid. Write this one as a `while True` loop with a `break`, so that you have written both shapes.
4. Accept an answer with stray spaces around it.
5. Display which choice each prisoner made, in words rather than as numbers, and then the outcome for both of them.

Test it by typing several invalid answers in a row before a valid one, and by pressing Enter without typing anything.

> 💡 **Tip:** Compare your two loops when you are finished. One writes the prompt twice and one writes it once. That difference is the whole reason both shapes exist.

---

## 📚 Exercise 6: Phonebook

Write a program that builds a phonebook and then searches it.

The program should:

1. Create an empty dictionary to hold names and phone numbers.
2. Use a `while` loop to ask repeatedly for a name and then a phone number, storing each pair in the dictionary. Pressing Enter without typing a name ends the loop — the empty string is the **sentinel**.
3. Display the finished phonebook, one numbered line per entry, using a `for` loop over the dictionary's items.
4. Ask the user for the first digits of a phone number, for example `47`, and display every entry whose number starts with those digits. If nothing matches, display a message saying so.

Test it by adding three entries, by searching for something that matches two of them, by searching for something that matches none, and by pressing Enter immediately so that the phonebook stays empty.

> 💡 **Tip:** Step 4 is the search pattern, and it needs a flag — not to stop the loop this time, but to remember afterwards whether anything at all was found.

---

## 📚 Exercise 7: Text statistics

Write a program that reports on a piece of text.

```python
text = """The quick brown fox jumps over the lazy dog.
Bergen is the second largest city in Norway, and it rains
there rather a lot. Programming is mostly a matter of
breaking a large problem into smaller problems."""
```

The program should display:

1. How many words the text contains.
2. The longest word, and how many letters it has.
3. The average word length, to one decimal.
4. How many words are longer than four letters — counting only those, and using `continue` to skip the rest.
5. A table showing, for each of the five vowels, how many words contain that vowel:

   ```
   a: 12
   e: 15
   ...
   ```

Step 5 needs a **nested** loop: one loop over the words, and inside it one loop over the vowels. Store the counts in a dictionary and display it with a loop over its items.

> 💡 **Tip:** Splitting on whitespace leaves the punctuation attached, so `"dog."` counts as four letters rather than three. `.strip(".,")` removes any of those characters from **both ends** of a string — the same `.strip()` you already know, given something specific to remove. Clean each word as you go.
