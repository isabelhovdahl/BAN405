# Week 01 — Home exercises

Work through these before the next lecture. They cover everything from [`01-python-basics.ipynb`](01-python-basics.ipynb): variables, numbers, strings, indexing and slicing, lists and dictionaries. 

Create your own notebook or script for your answers. Solution proposals are in this folder as `home-exercise-N-solution.py`. Try each exercise properly before you open them.

---

## Before you start

Exercise 5 needs one thing we did not cover in the lecture: the `input` function, which asks the person
running the program to type something.

```python
name = input("Please enter your name: ")

print(f"Hello, {name}!")
```

The one thing to watch out for is that **`input` always returns a string**, even when the user types a
number. So this does not do what you want:

```python
age = input("How old are you? ")

age + 1        # TypeError: cannot add a string and an integer
```

To do arithmetic on what the user typed, convert it first with `int` or `float`:

```python
age = float(input("How old are you? "))

age + 1        # works
```

> 💡 **Tip:** If you run these in a script, the prompt appears in the console. If you run these in a notebook, the input prompt appears at the top of the window rather than under the cell. The cell keeps running until you type something and press `Enter`.

---

## 📚 Exercise 1: Predict the output

For each of the six snippets below, write down what you think it will display **before** you run it.
Then run it and check.

Where your prediction was wrong, work out which rule from the lecture explains the real answer — that is
the whole point of the exercise.

**a)**

```python
x = 10
x = x + 5
x = x * 2
print(x)
```

**b)**

```python
word = "python"
word.upper()
print(word)
```

**c)**

```python
scores = [70, 85, 90]
top = scores
top.append(100)
print(scores)
```

**d)**

```python
items = ["a", "b", "c"]
items = items.append("d")
print(items)
```

**e)**

```python
letters = ["a", "b", "c"]
print(letters[1:5])
```

**f)**

```python
print(int(7.9))
print(round(7.9))
```

---

## 📚 Exercise 2: Tidy up a booking reference

A booking reference has arrived from another system, and it is a mess:

```python
booking = "   nhh-2026-oslo-bergen-0087   "
```

Write code that does the following:

1. Display the length of the string as it arrived.
2. Remove the leading and trailing spaces, and store the cleaned string in a variable called `reference`. Display its length as well.
3. Using slicing on `reference`, extract and display the **year**, the **origin**, the **destination** and the **booking number**.
4. Display a summary line built with an f-string, in the form:

   ```
   Booking 0087: OSLO to BERGEN in 2026
   ```

   Note the capitalization — you will need a string method for that.

---

## 📚 Exercise 3: Format a receipt

A small shop has sold three items. The data is stored in three lists, where the item at each position
belongs together — `items[0]` was sold in quantity `quantities[0]` at price `unit_prices[0]`, and so on.

```python
items = ["Espresso machine", "Coffee beans", "Oat milk"]
quantities = [1, 2, 3]
unit_prices = [4999.00, 149.90, 24.50]
```

Write a program that prints a receipt. It should:

1. Print a banner made of 40 asterisks, the shop name, and another banner. Do not type out 40 asterisks by hand.
2. Print one line per item showing the item name, the quantity, the unit price and the line total, with all amounts shown to **two decimals**.
3. Print the subtotal, the VAT at 25% of the subtotal, and the total including VAT. Show the total with
   a **thousands separator**.

You have not met loops yet, so write the three item lines out separately, one at a time.

> 💡 **Tip:** A format specification can set a field width as well as a number of decimals. `{name:<20}` pads a string to 20 characters on the left, and `{price:>10.2f}` right-aligns a number in 10 characters with two decimals. Use these to get the columns to line up.

---

## 📚 Exercise 4: City temperatures

The table below records the daily temperature from Monday to Friday in three different cities.

| Day       | London (°C) | Paris (°C) | Rome (°C) |
|-----------|-------------|------------|-----------|
| Monday    | 18.5        | 21.0       | 26.1      |
| Tuesday   | 19.0        | 22.5       | 27.3      |
| Wednesday | 17.8        | 20.2       | 25.0      |
| Thursday  | 20.1        | 23.1       | 26.7      |
| Friday    | 21.3        | 24.0       | 28.4      |

1. Store the data in a dictionary called `cities`, in which the keys are the city names and the values are **lists** of that city's five daily temperatures.
2. Display the temperature in Paris on Wednesday.
3. Display the average temperature for each of the three cities, rounded to one decimal.
4. Display the warmest single reading recorded in the whole table, and say which city it came from.

---

## 📚 Exercise 5: Temperature conversion program

Write a program that converts a temperature from Fahrenheit to Celsius.

The program should:

1. Print a short welcome message telling the user what the program does.
2. Use `input` to ask the user for a temperature in Fahrenheit.
3. Convert it to Celsius using the formula

   $$C = \frac{5}{9} \times (F - 32)$$

4. Display the result rounded to the nearest whole degree, in a sentence such as `98.6 degrees Fahrenheit is 37 degrees Celsius.`

Test it with a few values you can check: 32 °F is 0 °C, 212 °F is 100 °C, and −40 °F is −40 °C.
