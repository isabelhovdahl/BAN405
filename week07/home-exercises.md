# Week 07 — Home exercises

Work through these before the next lecture. They cover everything from [`07-pandas-basics.ipynb`](07-pandas-basics.ipynb): NumPy arrays, `Series` and `DataFrame`, the index and alignment, reading awkward files, the first look, selecting and filtering, changing values, and cleaning.

Work in a **notebook** this time rather than a script — from here on, that is the format everything in this course is written and handed in as. Solution proposals are in this folder as `home_exercise_N_solution.ipynb`, with their output kept so you can read them without running them. Try each exercise properly before you open them.

> 📝 **Note:** Every exercise assumes your notebook sits in this week's folder, so data is at `../data/`. Start it the way the lecture notebook starts: import what you need, load your own data, and make sure the whole thing runs from top to bottom before you call it finished.

---

## Version control (optional)

If you want the practice: open a terminal in this week's folder, run `git init`, and make a first commit before you start. Then commit after each exercise, with a message saying what you did. When you are finished, `git log --oneline` shows you your own week.

Add a `.gitignore` containing `__pycache__/` and `.ipynb_checkpoints/` so that git stops offering to track files you did not write.

This is optional and nothing depends on it. A repository per week is not how you would organize a real project — it is a sandbox, so that a mess costs you one week and no more. If yours ends up in a state you cannot fix, delete the `.git` folder. Your files are untouched, and you start fresh next week.

---

## Before you start

Two things the lecture did not cover.

### Looking at a DataFrame without printing it

Printing a 6 240-row table is not looking at it. Positron has two better ways.

The **Variables pane** in the sidebar lists everything currently in memory, with its type and size — so you can see at a glance that `co2` is a DataFrame of (6240, 11) and that `mask` is a Series of booleans. When a calculation goes wrong, the Variables pane usually tells you why faster than any amount of re-reading.

Click on a DataFrame there and it opens in the **data viewer**: a real spreadsheet-like grid you can scroll and sort, with each column's type in the header. Use it to *look* at data. Use `.head()`, `.info()` and `.describe()` when you want the answer recorded in your notebook, because the viewer leaves no trace in the document.

### Reading documentation with fifty parameters

Earlier in the course you looked up `randint`, which has two parameters and a one-line description. `read_csv` has more than fifty:

<https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html>

You are not meant to read that page. You are meant to *search* it. The method is:

1. Look at the raw file first and say what is wrong with it **in words** — "the columns are separated by semicolons", "there are nine junk rows above the header", "the missing values are written as `..`".
2. Search the page for that word: `sep`, `skiprows`, `na_values`.
3. Read only that parameter's description, and check the default.

Every awkward file you will meet has already been met by somebody, and the parameter is already there. Knowing what to search for is the skill; memorizing the list is not.

---

## 📚 Exercise 1: Predict the output

For each snippet below, write down what you think it will display **before** you run it. Then run it and check.

Where your prediction was wrong, work out which rule from the lecture explains the real answer — that is the whole point of the exercise.

**a)**

```python
import numpy as np

print(np.array([1, 2, 3.5]))
print(np.array([1, 2, "3"]))
print(np.array([12, 14, np.nan]).dtype)
```

**b)**

```python
import pandas as pd

a = pd.Series([10, 20, 30], index=["Norway", "Sweden", "Denmark"])
b = pd.Series([1, 2, 3], index=["Denmark", "Norway", "Finland"])

print(a + b)
```

**c)**

```python
df = pd.DataFrame({"x": [10, 20, 30, 40, 50]})

print(len(df.loc[1:3]))
print(len(df.iloc[1:3]))
```

**d)**

```python
df = pd.DataFrame({"city": ["Oslo", "Bergen"], "temp": [4.2, 7.8]})

df[df["city"] == "Oslo"]["temp"] = 99

print(df)
```

**e)**

```python
df = pd.DataFrame({"year": [2020, 2021], "value": [5, 15]})

print(df[df["year"] == 2020 and df["value"] > 10])
```

**f)**

```python
titanic = pd.read_csv("../data/titanic.csv")

print(titanic["Age"].dtype)
print(titanic["Age"].astype(int))
```

### Then: two broken snippets

Each of the two below does not do what its comment says. Say what is wrong, and write a corrected version.

```python
# 1 - meant to keep the rows for 2023 where emissions are above 100
co2 = pd.read_csv("../data/co2_emissions.csv")

subset = co2[co2["year"] == 2023 & co2["co2_total"] > 100]
```

```python
# 2 - meant to report the average emissions per country in 2023
co2 = pd.read_csv("../data/co2_emissions.csv")

avg = co2["co2_total"].mean()

print(f"Average emissions in 2023: {avg:.1f}")
```

---

## 📚 Exercise 2: The receipt, vectorized

You have written this receipt twice already — once by hand, and once with a loop. Write it a third time with no loop at all.

```python
items = ["Espresso machine", "Coffee beans", "Oat milk", "Filter papers"]
quantities = [1, 2, 3, 4]
unit_prices = [4999.00, 149.90, 24.50, 39.00]
```

1. Turn `quantities` and `unit_prices` into NumPy arrays.
2. Compute the line total for every item **in one expression**, with no loop.
3. Compute the subtotal, the VAT at 25%, and the total including VAT.
4. Using a boolean array, report how many items had a line total above 100, and what share of the subtotal those items accounted for.
5. Display the four line totals rounded to two decimals.

Then look back at your loop version from the earlier set of exercises and write a sentence in a markdown cell: what did the loop do that the array version does not have to?

> 💡 **Tip:** `array.round(2)` rounds every element. And remember that summing a boolean array counts the `True` values, because `True` is 1.

---

## 📚 Exercise 3: Two awkward files

In the lecture we wrote a pipe-delimited file and then read it back, which was easy because we knew what was in it. These two files came from somebody else, and nobody told you anything about them.

Neither opens correctly with `pd.read_csv(path)` or `pd.read_excel(path)`. Open each one and look at it before you write any code — in Positron, or in Excel, or in a text editor.

For each file, read it into a DataFrame properly and display its shape and its column names.

1. `../data/survey_data.csv`
2. `../data/eurostat.xlsx` — this one needs three arguments, not one. It should end up with 24 columns.

For the second file, also answer in a markdown cell: the first column of the result is not really a country name for every row. Which rows are not countries, and how would you recognize them if nobody told you?

---

## 📚 Exercise 4: First look at the emissions data

The first thing to do with an unfamiliar dataset is find out what is in it. Load `../data/co2_emissions.csv` and report, each in its own cell with a sentence saying what the answer means:

1. How many rows and columns there are.
2. The type of every column, and which column types would surprise somebody who had not read the lecture.
3. How many distinct entities the data covers, and which years.
4. How many values are missing in each column, and which two columns have none.
5. The five entities with the highest total emissions in 2023. Are they all countries?
6. All rows for Norway, showing only `year`, `co2_total` and `gdp_pc`, for the last five years in the data.
7. The rows for **2020** where GDP per capita was above 50 000 **and** renewable energy was above 40% of final consumption. How many are there, and which countries?

   Then try the same query for 2023 and explain, in one sentence, why the answer is what it is. Your answer to question 4 has the reason in it.

> 💡 **Tip:** Question 5 needs `.sort_values()`, which the lecture did not cover. Look it up — `help(pd.DataFrame.sort_values)` — and note the `ascending` parameter. That is exactly the documentation-searching skill from "Before you start".

---

## 📚 Exercise 5: Cleaning decisions

Every question here has more than one defensible answer. What is being marked is that you say which one you chose and why.

Load `../data/co2_emissions.csv`.

1. For each of `co2_total`, `gdp_pc` and `renew_energy`, report how many values are missing **in 2005 and in 2023 separately**. Write a sentence about what the difference tells you.
2. Report how many rows survive each of: `dropna()`, `dropna(subset=["co2_total"])`, and `dropna(subset=["co2_total", "gdp_pc"])`. Say which one you would use if you were about to study the relationship between emissions and income, and why the other two are wrong for that purpose.
3. Fill the missing `renew_energy` values with the column mean, and then report the mean and standard deviation of the column before and after. Explain in a markdown cell what happened to the standard deviation and why that might matter.
4. The column below arrived as text. Convert it to numbers so that the unusable entries become `NaN` rather than stopping the program, and report how many became `NaN`.

   ```python
   messy = pd.Series(["41.6", "434.3", "n/a", "", "43.5", "1 200", "12.4"])
   ```

---

## 📚 Exercise 6: A function that loads and cleans

Turn the work of this week into something you can call in one line — and that you will call again next week.

Write a function `load_emissions(path, drop_missing=True)` that:

1. Reads the emissions CSV at `path`.
2. Adds a column `co2_pc` holding emissions in tonnes per person. `co2_total` is in millions of tonnes and `population` is a count of people.
3. If `drop_missing` is `True`, drops rows with no `co2_total`. If it is `False`, keeps them.
4. Adds a column `income_group` labeling each row from `gdp_pc`, using `np.select`: below 1 000 is `"low"`, below 10 000 is `"lower-middle"`, below 50 000 is `"upper-middle"`, and anything above that is `"high"`. Rows with no GDP figure must end up as missing, **not** as `"high"`.
5. Returns the resulting DataFrame. It should not print anything.

Give it a docstring in the longer format, saying what each parameter does and what comes back.

Then, below the function:

- Call it and confirm you get 5 904 rows with the default, and 6 240 with `drop_missing=False`.
- Check that `income_group` has the number of missing values you expect, and say in a markdown cell what would have happened if you had left them to the `default`.
- Display the five entities with the highest emissions **per person** in 2023.
- Then display the five entities with the highest **total** emissions in 2023.
- Compare the two lists in a markdown cell. One of them is usable as it stands and the other is not. Say which, why, and what would have to be done to the data to fix it.

> 💡 **Tip:** Keep the function in its own cell, with the calls that demonstrate it in the cells below. You will want this function again next week, and a function that is tangled up with the code that uses it is a function you end up rewriting.

> 💡 **Tip:** To leave the rows with no GDP figure as missing, set them with `.loc` after the `np.select` call, as in the lecture. Passing `default=np.nan` looks like it should work and raises a `TypeError` instead — `np.select` refuses to mix a numeric default with text choices.
