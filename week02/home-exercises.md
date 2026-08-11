# Week 02 — Home exercises

Work through these before the next lecture. They cover everything from [`02-decisions.ipynb`](02-decisions.ipynb): boolean expressions, comparison and membership operators, logical operators and precedence, truthiness, string analysis, and `if` / `elif` / `else`.

Create your own notebook or script for your answers. Solution proposals are in this folder as `home-exercise-N-solution.py`. Try each exercise properly before you open them.

---

## Before you start

Two things the lecture did not cover. Exercise 4 needs both.

### Using a package

Everything we have written so far uses only what is built into the language itself. Most real Python work also uses **packages**: collections of functions somebody else has written and made available for anyone to use.

A package has to be **imported** before you can use anything in it:

```python
import random

print(random.randint(1, 6))
```

The `import` line goes at the top of the file, and it only has to run once. After that, everything in the package is available with the `random.` prefix in front of it.

If you only need one function from a package, you can import that function by name and then use it without the prefix:

```python
from random import randint

print(randint(1, 6))
```

Both forms are common. The first makes it obvious where a function came from, which matters once a program imports several packages and you are trying to work out what `choice` refers to.

> 📝 **Note:** `random` is part of Python's standard library, which means it comes with Python and there is nothing to install. Many of the packages we use later in the course do not come with Python. Getting hold of those — and making sure that everyone running your program has the same versions of them — is a topic we come back to.

### Reading the documentation for a function

`randint` is not a function you can guess your way into. What arguments does it take? Can it return the upper bound itself, or does it stop one short? The answer is in the documentation:

<https://docs.python.org/3/library/random.html#random.randint>

It says:

> `random.randint(a, b)` — Return a random integer *N* such that `a <= N <= b`.

Two useful facts in one line. It takes exactly two arguments, and **both ends are included**, so `randint(1, 6)` really can return 1 and really can return 6. Plenty of things in Python exclude the upper end — slicing, for one — so this is worth reading rather than assuming.

Getting comfortable with a documentation page is part of learning to program. You will not remember what every function does, and you are not supposed to.

---

## 📚 Exercise 1: Predict the output

For each snippet below, write down what you think it will display **before** you run it. Then run it and check.

Where your prediction was wrong, work out which rule from the lecture explains the real answer — that is the whole point of the exercise.

**a)** Two blocks that differ by three characters:

```python
score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
```

```python
score = 85

if score >= 90:
    print("A")
if score >= 80:
    print("B")
if score >= 70:
    print("C")
```

**b)**

```python
print(0.1 + 0.2 == 0.3)
print(round(0.1 + 0.2, 2) == 0.3)
```

**c)**

```python
is_member = False
age = 70

print(is_member and age >= 18 or age >= 67)
print(is_member and (age >= 18 or age >= 67))
```

**d)**

```python
answer = "B"

print(answer == "A" or "B")
print(answer == "A" or answer == "B")
```

**e)**

```python
print("3.14".isdigit())
print("-7".isdigit())
print("".isdigit())
```

**f)**

```python
code = ""

print(len(code) > 0 and code[0] == "N")
```

**g)**

```python
print(bool(" "))
print(bool(0))
print(bool("0"))
```

### Then: three broken conditions

Each of the three snippets below is wrong. Say what is wrong with it, and write a corrected version.

```python
# 1
if grade = "A":
    print("Top marks")
```

```python
# 2 - meant to accept any score from 0 to 100
if 0 < score or score > 100:
    print("Valid score")
```

```python
# 3 - meant to check that a name starts with a capital letter
if name[0].isupper() and len(name) > 0:
    print("Starts with a capital")
```

---

## 📚 Exercise 2: Password strength

A website wants to tell people whether the password they have chosen is any good.

Write a program that starts from a password stored in a variable:

```python
password = "CopyCat1337"
```

1. Work out each of the following rules separately, storing each answer in its own variable with a
   sensible name:

   - it is at least 8 characters long
   - it contains at least one uppercase letter
   - it is not made up entirely of letters
   - it does not start with a digit

2. Display all four results, each on its own line, so you can see which rules the password passed.

3. Combine the four into a single variable called `strong`, which is `True` only when all four rules
   hold.

4. Finish with an `if` / `elif` / `else` chain that displays one of:

   - `Strong password.` — all four rules hold
   - `Long enough, but it breaks at least one of the other rules.`
   - `Too short.`

5. Test your program on all five of these:

   ```
   "CopyCat1337"    "copycat"    "12345678"    "Bergen!!"    ""
   ```

> ⚠️ **Warning:** One of the four rules will crash on the empty password unless you think about the order of the parts of your condition. That is not an accident — it is the same trap as the guard in the lecture.

> 💡 **Tip:** "Contains at least one uppercase letter" is the rule we looked at in the lecture, and `.islower()` is not the way to write it.

---

## 📚 Exercise 3: Temperature conversion, in either direction

In the previous set of exercises you wrote a program that converted Fahrenheit to Celsius. It only went one way. Extend it so the user chooses the direction.

The program should:

1. Display a short menu explaining the two options.
2. Ask the user which conversion they want: `F` to convert Fahrenheit to Celsius, or `C` to convert
   Celsius to Fahrenheit.
3. Accept the answer whether it was typed in upper or lower case, and with stray spaces around it.
   If it is anything other than F or C, display a message saying the selection was not valid — and
   the program should then do nothing further.
4. Otherwise, ask for the temperature and convert it, using

   $$C = \frac{5}{9} \times (F - 32) \qquad\qquad F = \frac{9}{5} \times C + 32$$

5. Display the result to one decimal, in a full sentence.
6. Finally, add a sanity check: nothing can be colder than absolute zero, which is −273.15 °C. If
   the temperature in Celsius is below that, display a warning that the reading cannot be right.

Test it with 32 °F, 100 °C, and −300 °C.

> 📝 **Note:** This program still stops with an error if the user types `cold` instead of a number. You cannot fix that properly with what we have covered — `.isdigit()` rejects `-40` and `98.6` too, which are both perfectly good temperatures. Leave it. There is a proper tool for this, and it comes later in the course.

---

## 📚 Exercise 4: Random number generator

Write a program that draws a random whole number between two bounds chosen by the user.

The program should:

1. Display a welcome message saying what the program does, and stating that both bounds must be
   **whole numbers that are not negative**.
2. Ask the user for a lower bound and an upper bound.
3. Check that both are whole, non-negative numbers. If either is not, display a message saying so,
   and stop.
4. If they are, check that the lower bound is not larger than the upper bound. If it is, display a
   *different* message saying that, and stop.
5. Otherwise, draw a random number between the two bounds with `randint` and display it in a
   sentence.

Write steps 3 and 4 as a **nested** conditional rather than as one condition joined with `and`, so that the two ways of getting it wrong produce two different messages. Notice while you are writing it that you could not do it any other way round: asking whether the lower bound is smaller is meaningless until you know both inputs are numbers at all.

Test it with `2` and `8`, with `8` and `2`, with `two` and `8`, and by pressing Enter without typing anything.

---

## 📚 Exercise 5: The prisoner's dilemma

The prisoner's dilemma is a standard example from game theory. Two prisoners are questioned separately, and each must choose whether to stay silent or to confess, without knowing what the other one chose. The sentences are:

|  | **B stays silent** | **B confesses** |
|---|---|---|
| **A stays silent** | A: 1 year<br>B: 1 year | A: 3 years<br>B: goes free |
| **A confesses** | A: goes free<br>B: 3 years | A: 2 years<br>B: 2 years |

Write a program that plays the game:

1. Display a welcome message and explain the two options: press `1` to stay silent, `2` to confess.
2. Ask prisoner A for their choice, then prisoner B for theirs.
3. Check that both entries are valid. If either one is not, display a message saying the choices
   were invalid, and stop.
4. Otherwise, display which choice each prisoner made, in words rather than as numbers, and then
   the outcome for both of them.

> 💡 **Tip:** A dictionary mapping `"1"` and `"2"` to the words `"stay silent"` and `"confess"` will save you writing those words out four times, and it gives you something to check the input against as well.

---

## 📚 Exercise 6: Leap years

A year is a leap year if it is divisible by 4 — except that years divisible by 100 are not leap years, unless they are also divisible by 400.

Write a program that:

1. Asks the user for a year.
2. Checks the input is a whole, non-negative number, and says so if it is not.
3. Stores the answer in a variable called `is_leap`, using a **single boolean expression** — no `if`
   statement, and no intermediate variables.
4. Displays a sentence saying whether that year is a leap year.

Check your expression against 2024 (leap), 2023 (not), 1900 (not) and 2000 (leap). If you get 1900 or 2000 wrong, the brackets are in the wrong place.

> 💡 **Tip:** The modulo operator `%` gives the remainder, so a year is divisible by 4 exactly when `year % 4 == 0`.
