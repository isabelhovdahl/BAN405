# Week 04 — Home exercises

Work through these before the next lecture. They cover everything from [`04-functions.ipynb`](04-functions.ipynb): defining functions, `return` versus `print`, arguments and default values, scope, mutable arguments, docstrings, exceptions and `try` / `except`.

Create your own **scripts** for your answers. Solution proposals are in this folder as `home_exercise_N_solution.py`. Try each exercise properly before you open them.

---

## Before you start

Three things the lecture did not cover. The first is worth reading before you run any of these, the second explains the docstrings you will see in the solution proposals, and the third is a small piece of Python you will meet constantly in other people's code.

### Reading a traceback in a script

The lecture read tracebacks in a notebook, where the report appears under the cell that produced it. In a script it appears in the **console** instead, and it looks slightly different:

```
Traceback (most recent call last):
  File "C:\Users\you\ban405\week04\receipt.py", line 24, in <module>
    main()
  File "C:\Users\you\ban405\week04\receipt.py", line 18, in main
    print(format_line(item, quantity, price))
  File "C:\Users\you\ban405\week04\receipt.py", line 11, in format_line
    return f"{item:<20}{total:>9.2f}"
TypeError: unsupported format string passed to str.__format__
```

The rule is the same as in the lecture: **read the last line first**, then walk up. What is new is that each frame names a **file** and a **line number**, and in Positron those are clickable — clicking one takes you straight to the line.

Once a program has several functions, the innermost frame is often not the one with the mistake in it. Here the crash is on line 11, but the bad value was handed over on line 18, and it came from somewhere in `main`. Read all of the frames, not only the last one.

### The longer docstring format

The lecture used one-line docstrings, which are the right default. When a function has several parameters whose meaning is not obvious from their names, the longer form earns its keep — and it is what the solution proposals in this folder use, so it is worth being able to read:

```python
def eff_interest_rate(r, n=1):
    """
    Return the effective annual interest rate.

    Parameters
    ----------
    r : float
        The nominal annual interest rate, as a decimal, so 0.059 for 5.9%.
    n : int, optional
        The number of times per year that interest is compounded. Default is 1.

    Returns
    -------
    float
        The effective annual rate, as a decimal.
    """
    return (1 + r / n) ** n - 1
```

Three sections: what the function does, what goes in, what comes out. `help(eff_interest_rate)` displays all of it, and so does hovering over the name in Positron.

Typing all of that out by hand is tedious, and you do not have to.

> 💡 **Tip:** Positron can write the skeleton for you, once you add an extension. Open the **Extensions** view in the sidebar, search for **autoDocstring**, and install it.
>
> Then put the cursor on the line directly under a `def`, type `"""` and press Enter. The extension reads the function header and generates the whole block — one line per parameter, with the names already filled in and a `Returns` section waiting. You write the descriptions; it writes the scaffolding.
>
> It produces Google-style docstrings by default rather than the NumPy style above. To switch, open Settings (`Ctrl` + `,`), search for `autoDocstring: Docstring Format`, and choose `numpy`.

### Using a function you wrote in another file

Once you have written a good function you will want it in your next program too, and copying it is the wrong answer — the same reason copying a formula three times was the wrong answer.

Any `.py` file can be **imported** into another one. Make two files in the same folder.

`temperature_tools.py`:

```python
def to_fahrenheit(celsius):
    """Return a Celsius temperature converted to Fahrenheit."""
    return 9 / 5 * celsius + 32


print("Testing:", to_fahrenheit(100))
```

`report.py`:

```python
from temperature_tools import to_fahrenheit

print(to_fahrenheit(4.2))
```

Now run `report.py`. You get **two** lines, not one:

```
Testing: 212.0
39.56
```

Importing a file **runs** it, top to bottom. Python has to execute the `def` statement to learn what `to_fahrenheit` is, and while it is in there it executes everything else too — including the test line you left at the bottom.

The fix is a special variable that Python sets in every file it runs. In the file you started, `__name__` is the string `"__main__"`; in a file that was merely imported, it is the file's own name. So a block guarded like this runs when the file is the program, and is skipped when the file is a library:

```python
def to_fahrenheit(celsius):
    """Return a Celsius temperature converted to Fahrenheit."""
    return 9 / 5 * celsius + 32


if __name__ == "__main__":
    print("Testing:", to_fahrenheit(100))
```

Run `temperature_tools.py` and the test line runs. Run `report.py` and it does not. That is the whole trick, and it is why almost every serious Python file you will ever open ends with those two lines. The solution proposals in this folder use it, so you can import any function out of them without their demonstration code going off.

> ⚠️ **Warning:** A file you intend to import must have a name Python can write in an `import` statement — letters, digits and underscores, not starting with a digit. `temperature_tools.py` is fine; `temperature tools.py`, `temperature-tools.py` and `2024_tools.py` are not. A hyphen means subtraction in Python, so `import temperature-tools` is read as a sum and fails before it ever looks for the file.

---

## 📚 Exercise 1: Predict the output

For each snippet below, write down what you think it will display **before** you run it. Then run it and check.

Where your prediction was wrong, work out which rule from the lecture explains the real answer — that is the whole point of the exercise.

**a)**

```python
def add_vat(price):
    total = price * 1.25


print(add_vat(100))
```

**b)**

```python
def total_of(values):
    total = 0

    for value in values:
        total += value
        return total


print(total_of([10, 20, 30]))
```

**c)**

```python
count = 10


def bump():
    count = 99
    return count


print(bump())
print(count)
```

**d)**

```python
def add_zero(values):
    values.append(0)
    return values


def add_one(number):
    number = number + 1
    return number


readings = [4, 9]
n = 4

print(add_zero(readings), readings)
print(add_one(n), n)
```

**e)**

```python
def divide(a, b=2):
    return a / b


print(divide(10))
print(divide(10, 5))
print(divide(b=10, a=5))
print(divide(b=10))
```

**f)** For each of these five expressions, name the exception it raises. Predict first, then run them one at a time.

```python
float("12,50")
[1, 2, 3][3]
{"a": 1}["b"]
10 / 0
"3" + 3
```

**g)**

```python
def read_number(text):
    try:
        return flooat(text)
    except:
        return None


print(read_number("42"))
```

Why does that happen, and what would the program have told you if the `except` had named `ValueError` instead?

### Then: two broken functions

Each of the two functions below runs without stopping and gives the wrong answer. Say what is wrong with it, and write a corrected version.

```python
# 1 - meant to report whether a list contains any negative value
def has_negative(values):
    for value in values:
        if value < 0:
            return True
        else:
            return False


print(has_negative([4, 9, -2]))
```

```python
# 2 - meant to return the average, or 0 for an empty list
def average(values):
    try:
        return sum(values) / len(values)
    except:
        return 0


print(average([4, 9, 2]))
print(average([]))
print(average(["4", "9"]))
```

---

## 📚 Exercise 2: Effective interest rate

You have received two offers on a savings account:

- 5.9%, with interest paid **quarterly**
- 6%, with interest paid **twice a year**

The headline rates are not comparable, because interest paid more often earns interest of its own. The comparable number is the **effective** annual rate:

$$R = \left(1 + \frac{r}{n}\right)^n - 1$$

where $r$ is the nominal annual rate and $n$ is the number of times per year that interest is compounded.

Write a program that:

1. Defines a function `eff_interest_rate` with two parameters, `r` and `n`, that **returns** the effective rate. Give `n` a default of `1`, since a rate compounded once a year is the ordinary case.
2. Documents the function with a docstring saying what it returns and what its two parameters mean.
3. Uses the function to display the effective rate of each offer, as a percentage to two decimals.
4. Displays which offer is better, working it out with an `if` rather than by reading the two numbers yourself.
5. Makes one of the two calls using **keyword arguments** and the other **positionally**, so that you have written both.

Then check your default by calling `eff_interest_rate(0.06)`. Compounding once a year changes nothing, so the answer should be 0.06 — look closely at what you actually get, and at what you already know about floats.

> 💡 **Tip:** The function should return a decimal such as `0.0609`, not a percentage such as `6.09`. Converting for display is the calling code's job — that is the division of labor the lecture argued for.

---

## 📚 Exercise 3: Random character, and a code generator

Earlier you wrote a program that drew a code of random digits with a loop. Now build the same thing out of two functions, one of which is general enough to be worth keeping.

The program should:

1. Define `random_character(characters)`, which takes a string of characters and **returns** one of them, chosen at random. Draw a random position with `randint` and index into the string.
2. Decide what `random_character("")` should do, and say why in a comment. There is no character to return, so there are three defensible answers: return the empty string, return `None`, or do nothing special and let the call fail with whatever exception it produces. Try the third one first and see which exception you actually get — it is not the one most people guess. Then pick one and write it deliberately.
3. Define `make_code(length)`, which returns a code of that many random digits as a **single string** — `481902`, not `[4, 8, 1, 9, 0, 2]`. It should call `random_character` rather than drawing digits itself.
4. Give both functions a docstring.
5. Display codes of length 6, of length 1 and of length 0. Say in a comment what a length of 0 should reasonably produce, and check that your program actually does that.

Then call `random_character` on `"abcdefghijklmnopqrstuvwxyz"` to confirm it is not secretly specific to digits — a function that only works for the one case you wrote it for is not reusable, whatever its name says.

> 💡 **Tip:** Set `random.seed` at the top while you are developing. A program whose output changes on every run is a program you cannot tell you have fixed.

---

## 📚 Exercise 4: The receipt, refactored

You have written this receipt twice: once by hand, and once with a loop. Write it a third time, as a set of functions.

```python
items = ["Espresso machine", "Coffee beans", "Oat milk"]
quantities = [1, 2, 3]
unit_prices = [4999.00, 149.90, 24.50]
```

Write four functions and a `main`:

1. `line_total(quantity, unit_price)` — returns the total for one line.
2. `format_line(item, quantity, unit_price)` — **returns** one formatted line as a string, with the columns lined up and the amounts to two decimals. It should call `line_total` rather than multiplying again.
3. `receipt_totals(quantities, unit_prices)` — returns **three** values: the subtotal, the VAT at 25% of the subtotal, and the total including VAT.
4. `print_receipt(items, quantities, unit_prices)` — prints the banner, one line per item, and the three totals, calling the functions above. This is the only one of the four that prints anything.
5. `main()` — holds the three lists and calls `print_receipt`. No variable in your program should be defined outside a function.

Give every function a docstring, and call `main()` at the end.

Then test the pieces separately, which is the point of having written it this way: `line_total(3, 24.50)` should give `73.5`, and `receipt_totals([1], [100.0])` should give `100.0`, `25.0` and `125.0`. You can check both without printing a receipt at all.

> 💡 **Tip:** Step 3 returns three values, so the call unpacks into three names: `subtotal, vat, total = receipt_totals(quantities, unit_prices)`.

---

## 📚 Exercise 5: Temperature conversion program

You have written a temperature converter twice. The first version stopped as soon as anything was wrong, and the second one could re-prompt for the scale but still crashed if the temperature was not a number — because `.isdigit()` rejects `-40` and `98.6`, which are both perfectly good temperatures.

That is now fixable. Rewrite the program so that it runs entirely out of functions and never gives up on bad input.

The program should consist of four functions:

- `get_scale()` — asks which direction to convert, and returns `"C"` or `"F"`. Re-prompts until it gets one of them, accepting lowercase and stray spaces.
- `get_temperature()` — asks for the temperature and returns it as a number. Re-prompts until the input can actually be converted, using `try` / `except`.
- `convert_temperature(temperature, scale)` — returns the converted temperature. This function asks nothing and prints nothing.
- `main()` — displays the welcome message, calls the other three, and displays the result.

$$C = \frac{5}{9} \times (F - 32) \qquad\qquad F = \frac{9}{5} \times C + 32$$

Here is what a run can look like:

```
*********** Temperature Conversion Program ***********
This program converts temperatures (Fahrenheit/Celsius)
******************************************************

Enter "F" to convert from Fahrenheit to Celsius
Enter "C" to convert from Celsius to Fahrenheit

Enter selection: K
Invalid input! Enter "F" or "C".

Enter selection: c

Enter temperature to convert: cold
Invalid input! Enter a number.

Enter temperature to convert: 10

10.0 degrees Celsius equals 50.0 degrees Fahrenheit.
```

Finally, add a sanity check to `main`: nothing can be colder than absolute zero, −273.15 °C. If the temperature in Celsius is below that, display a warning that the reading cannot be right.

Test it by typing several invalid answers in a row before a valid one, by pressing Enter without typing anything, and with `-40`, `98.6` and `-300`.

> 💡 **Tip:** Catch `ValueError` by name, not with a bare `except:`. If you misspell something inside the `try`, a bare `except` will tell you the user typed it wrong, forever.

---

## 📚 Exercise 6: A loop that survives bad data

Real data has holes in it. A column of readings arrives as text, and some of the entries are not numbers: a blank field where nobody recorded anything, the code `-999` standing in for a missing reading, and the occasional `n/a` typed by a person. A program that stops at the first of these is useless, and a program that silently treats them as zero is worse.

```python
rows = ["12.5", "14.0", "-999", "", "13.2", "n/a", "11.0", "  9.8  ", "-999"]
```

Write a program that:

1. Defines `parse_reading(text)`, which returns the reading as a number, or `None` if the text cannot be read as one. Treat a blank or whitespace-only field as unreadable too. Give it a docstring.
2. Loops over `rows`, calling `parse_reading` on each entry and sorting it into one of three groups: a usable reading, a **missing** one (the sentinel `-999`), or an **unreadable** one.
3. Accumulates the total and the count of the usable readings only.
4. Displays how many entries fell into each of the three groups, and the average of the usable readings to one decimal.
5. Displays a message rather than crashing if there were no usable readings at all — test this by running it on `["n/a", "", "-999"]`.

The answer for the list above: 5 usable readings averaging 12.1, 2 missing and 2 unreadable.

> 💡 **Tip:** `parse_reading` decides whether the text *is* a number. Whether `-999` counts as data is a question about this particular dataset, not about text, so it belongs in the loop rather than in the function. Keeping the two apart is what makes `parse_reading` reusable on the next dataset, where the missing-value code will be something else.
