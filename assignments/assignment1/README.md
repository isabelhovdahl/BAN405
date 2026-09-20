# Assignment 1 — Password Strength Checker

In this assignment, you will write a program that checks how strong a password is. The program counts the different kinds of characters in a password, checks the password against a set of rules, gives it a score, and rates it from "very weak" to "strong". Finally, the program uses these checks to help the user choose a strong password.

The assignment draws on everything from the course so far: strings, lists, decisions, loops and functions. Using functions is **optional** — the assignment can be solved completely with or without them (see [Organizing your code](#organizing-your-code)).

**Before you start:**

- Download the starter script [`password_checker.py`](password_checker.py), and write your program in it. It already contains the special characters, the list of common passwords, and the test passwords you will need.
- Build the program in the four parts below, **in order**. Each part adds to the one before it, and your program should run after each part.
- Parts 1–3 work on the password that is already set in the starter script, so you can just run the script to see what your program does.
- Your output doesn't have to match the examples in this assignment character for character, but it should show the same information.

> 💡 **Tip:** If you use an AI assistant, read the [AI guidelines](../../guides/ai-guidelines.md) first. This assignment is a chance to practice, and you only get the practice by writing the code yourself.

---

## The rules

Everything in Parts 1–3 follows from the rules in this section. Come back to it whenever you are unsure what your program should do.

### Character types

Each character in a password belongs to one of these four types, or to none of them:

| Type | A character `char` is this type if... |
| --- | --- |
| Uppercase letter | `char.isupper()` is `True` |
| Lowercase letter | `char.islower()` is `True` |
| Digit | `char.isdigit()` is `True` |
| Special character | `char in special_characters` is `True` |

`special_characters` is defined in the starter script as `"!@#$%&*?"`. Any other character, such as a space, a period or a comma, is allowed in a password. It counts towards the length of the password, but not towards any of the types.

### The five rules

A password should:

1. be at least 8 characters long
2. contain at least one uppercase letter
3. contain at least one lowercase letter
4. contain at least one digit
5. contain at least one special character

### The score

The score is a number from 0 to 6, made up of two parts:

- **Length points:** 0 points for fewer than 8 characters, 1 point for 8–11 characters, and 2 points for 12 characters or more.
- **Type points:** 1 point for each character type that appears in the password at least once (0–4 points).

### The rating

Go through these conditions **in this order**, and use the first one that applies:

| | Condition | Rating |
| --- | --- | --- |
| 1 | The password is in `common_passwords`, when compared in lowercase | `very weak` |
| 2 | The password has fewer than 8 characters (whatever its score), **or** the score is 0–2 | `weak` |
| 3 | The score is 3–4 | `medium` |
| 4 | The score is 5–6 | `strong` |

The order matters:

- `Ban405!` contains all four character types and scores 4, but it is still `weak`, because it is too short.
- `Password123!` scores a full 6, but it is `very weak`, because it is one of the most common passwords there is.

The passwords in `common_passwords` are all in lowercase. "Compared in lowercase" means that `PASSWORD123!` and `Password123!` both count as common, since both are `password123!` once converted to lowercase.

---

## Part 1 — Analyze the password

Write a program that analyzes the characters in `password`:

- Count the number of **uppercase letters**, **lowercase letters**, **digits** and **special characters** in the password.
- Display the **length** of the password, and each of the four counts.

For `Sunshine26`, the output could look like this:

```
Length:             10
Uppercase letters:  1
Lowercase letters:  7
Digits:             2
Special characters: 0
```

> 💡 **Tip:** A string method like `isdigit` checks the *whole* string at once: `"Sunshine26".isdigit()` is `False`, because not every character is a digit. To count the digits, you need to look at the characters **one at a time**. Recall from the [loops lecture](../../week03/03-loops.ipynb) that a `for` loop can go through a string one character at a time.

---

## Part 2 — Check the rules

Extend your program to check the password against each of the [five rules](#the-five-rules):

- For **each** rule, display whether the password passes or fails it.

For `Sunshine26`, which has no special characters, the output could look like this:

```
[OK]   At least 8 characters
[OK]   At least one uppercase letter
[OK]   At least one lowercase letter
[OK]   At least one digit
[FAIL] At least one special character (!@#$%&*?)
```

---

## Part 3 — Score and rate the password

Extend your program to [score](#the-score) and [rate](#the-rating) the password:

- Calculate the score of the password, and display it out of 6.
- Rate the password, and display the rating.

`Sunshine26` has 10 characters, which gives 1 length point, and contains three of the four character types, which gives 3 type points. The output could look like this:

```
Score: 4 / 6
Rating: medium
```

### Test your program

Before you move on to Part 4, check your program against the test passwords below. They are all in the starter script: switch between them by moving the `#`, run your program, and compare the result with the table.

| Password | What it tests | Score | Rating |
| --- | --- | --- | --- |
| `Sunshine26` | The example used in this assignment | 4 | `medium` |
| `hello` | Short, with only one character type | 1 | `weak` |
| `Ban405!` | All four character types, but too short | 4 | `weak` |
| `sunshine` | Exactly 8 characters | 2 | `weak` |
| `abcdefghij1` | 11 characters | 3 | `medium` |
| `abcdefghijk1` | 12 characters | 4 | `medium` |
| `Ban405rock!` | Passes every rule | 5 | `strong` |
| `Blåbær!2` | Norwegian letters | 5 | `strong` |
| `correct horse battery` | Spaces | 3 | `medium` |
| `Password123!` | A common password | 6 | `very weak` |
| `PASSWORD123!` | A common password, in uppercase | 5 | `very weak` |

If your program gives a different score or rating for one of them, the "What it tests" column tells you where to start looking.

---

## Part 4 — Choose a password

Finally, use your program to help the user choose a password, the way a website does when you create a new account: the program keeps asking for a password until the user picks one that is strong enough.

- Until now, your program has checked the password set in the starter script. Replace it with `input()`, so that the user types in the password they want to use.
- Keep asking for a password, and check each one as in Parts 1–3, until **either**:
  - the user picks a password that is rated `strong`, which is then accepted, **or**
  - the user presses Enter without typing anything, to quit without choosing a password.
- When the program stops, display whether a password was accepted, and how many passwords were checked. Pressing Enter to quit doesn't count as checking a password.

A run could look like this (the details of each check are shortened to `...`):

```
Choose a password (or press Enter to quit): sunshine
...
Score: 2 / 6
Rating: weak

Choose a password (or press Enter to quit): Ban405rock!
...
Score: 5 / 6
Rating: strong

Password accepted! Passwords checked: 2
```

And like this, if the user quits:

```
Choose a password (or press Enter to quit): hello
...
Score: 1 / 6
Rating: weak

Choose a password (or press Enter to quit):
No password chosen. Passwords checked: 1
```

> 📝 **Note:** In Part 4, everything from Parts 1–3 has to run once for every password the user enters. If you wrote those parts without functions, this means moving all of that code inside the loop. If you wrote functions, the loop only needs to call them.

---

## Organizing your code

Whether you use functions or not, a program of this size is much easier to write, read and fix when it is divided into **logical blocks**, where each block does one specific task: counting the character types, checking the rules, deciding the rating, and so on. Start each block with a short comment that says what it does.

### Using functions (optional)

Functions are a way of turning those blocks into named, reusable pieces. Whether you use them — and if so, which ones — is up to you.

If you do use functions:

- **Give each function one specific task**, and a name that says what that task is. A single function that does everything is no easier to follow than no functions at all.
- **Return a result rather than printing it** whenever the rest of your program needs that result, such as a count or a score. See the section on `return` in the [functions lecture](../../week04/04-functions.ipynb).

Here are some examples of names that each describe one specific task:

- `count_digits` — counts the digits in a password
- `is_common_password` — checks whether a password is in the list of common passwords
- `display_rules` — displays which rules a password passes and fails

These are examples of how much a single function should do, **not** a plan to follow. Your program may need other functions than these, or fewer, or more.

---

## What to submit

Upload your `password_checker.py` to Canvas.

Submit what you have, even if not every part of your program works. What matters is that you have made an honest attempt at the assignment.
