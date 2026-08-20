# Week 08 — Home exercises

Work through these before the next lecture. They cover everything from [`08-summarizing-and-combining.ipynb`](08-summarizing-and-combining.ipynb): grouping and aggregating, the index of a grouped result, transforming within groups, dates, `resample`, `concat`, duplicates, and `merge` together with the checks that tell you it worked.

Work in a **notebook**, as last time. Solution proposals are in this folder as `home_exercise_N_solution.ipynb`, with their output kept so you can read them without running them. Try each exercise properly before you open them.

> 📝 **Note:** Every exercise assumes your notebook sits in this week's folder, so data is at `../data/`. Start it the way the lecture notebook starts: import what you need, load your own data, and make sure the whole thing runs from top to bottom before you call it finished.

---

## Version control (optional)

If you want the practice: open a terminal in this week's folder, run `git init`, and make a first commit before you start. Then commit after each exercise, with a message saying what you did. When you are finished, `git log --oneline` shows you your own week.

Add a `.gitignore` containing `__pycache__/` and `.ipynb_checkpoints/` so that git stops offering to track files you did not write.

This is optional and nothing depends on it. A repository per week is not how you would organize a real project — it is a sandbox, so that a mess costs you one week and no more. If yours ends up in a state you cannot fix, delete the `.git` folder. Your files are untouched, and you start fresh next week.

---

## Before you start

One thing the lecture did not cover, and exercise 4 needs it.

### Asking Python what is in a folder

So far every file you have opened, you have named yourself. That stops working the moment a folder holds ten files, or a hundred, or a number that changes every month. `os.listdir` hands you the names.

```python
import os

files = os.listdir("../data/stocks")
print(files)
```

Three habits worth building around that one line.

**Filter to the files you actually want.** A folder is rarely as tidy as you hope: `.ipynb_checkpoints`, a stray `notes.txt`, a `.DS_Store` that macOS put there without telling you. Handing any of those to `read_csv` gives you an error at best.

```python
files = [f for f in os.listdir("../data/stocks") if f.endswith(".csv")]
```

**Sort it.** `os.listdir` makes no promise about order, and an analysis whose output depends on the order the operating system happened to return files in is not reproducible. `sorted()` returns a list in order and costs nothing.

**Join the folder onto the name.** `listdir` gives you `"AAPL.csv"`, not `"../data/stocks/AAPL.csv"`. `os.path.join` builds the full path with the right separator for whichever computer is running the code — which matters, because Windows and macOS disagree about which way the slash leans.

```python
for name in sorted(files):
    path = os.path.join("../data/stocks", name)
    df = pd.read_csv(path)
```

The filename itself is often data. `"AAPL.csv"` tells you which company the rows belong to, and nothing inside the file does — so you take it apart with the string methods you already know: `name.split(".")[0]` gives `"AAPL"`.

---

## 📚 Exercise 1: Predict the output

For each snippet below, write down what you think it will display **before** you run it. Then run it and check.

Where your prediction was wrong, work out which rule from the lecture explains the real answer — that is the whole point of the exercise. Every one of these runs without an error, and most of them are wrong in a way nothing warns you about.

**a)**

```python
import pandas as pd

sales = pd.DataFrame({
    "shop": ["A", "B", "A", "B"],
    "day":  [1, 1, 2, 2],
    "sold": [10, 20, 30, 40],
})

result = sales.groupby("shop")["sold"].sum()

print(type(result))
print(result)
print(result["A"])
```

**b)**

```python
print(sales.groupby("shop")["sold"].mean().shape)
print(sales.groupby("shop")["sold"].transform("mean").shape)
```

**c)**

```python
staff = pd.DataFrame({
    "team":  ["red", "blue", None, "red"],
    "hours": [10, 20, 30, 40],
})

print(staff.groupby("team")["hours"].sum())
print(staff["hours"].sum())
```

**d)**

```python
left = pd.DataFrame({"k": ["x", "y"], "v": [1, 2]})
right = pd.DataFrame({"k": ["x", "x", "y"], "w": [10, 20, 30]})

merged = left.merge(right, on="k", how="left")

print(len(left), "->", len(merged))
print(merged)
```

**e)**

```python
panel = pd.DataFrame({
    "country": ["A", "A", "B", "B"],
    "year":    [2020, 2021, 2020, 2021],
    "value":   [1.0, 2.0, 100.0, 101.0],
})

panel["change"] = panel["value"].diff()

print(panel)
```

**f)**

```python
dates = pd.DataFrame({
    "date":  ["10/01/2021", "02/11/2020", "05/06/2021"],
    "value": [1, 2, 3],
})

print(dates.sort_values("date"))
print(pd.to_datetime(dates["date"]))
```

### Then: two broken snippets

Each of the two below does not do what its comment says. Say what is wrong, and write a corrected version.

```python
# 1 - meant to report total emissions by region, for every region
co2 = pd.read_csv("../data/co2_emissions.csv")
info = pd.read_csv("../data/country_info.csv")

merged = co2.merge(info, left_on="country", right_on="name", how="inner")

print(merged.groupby("region")["co2_total"].sum())
```

```python
# 2 - meant to give each country's year-on-year change in emissions
co2 = pd.read_csv("../data/co2_emissions.csv")
co2 = co2.sort_values(["country", "year"])

co2["change"] = co2["co2_total"].diff()

print(co2[co2["country"] == "Norway"][["year", "co2_total", "change"]].head())
```

---

## 📚 Exercise 2: Summarizing the panel

Load `../data/co2_emissions.csv` and add `co2_pc` the way the lecture's `load_emissions` does.

1. Build a summary table with one row per year and three named columns: the number of entities with a `co2_total` figure, total emissions, and mean emissions per person. Round it and display the last five years.
2. Do the same by `income_group`, which you will have to build first: use `np.select` on `gdp_pc`, with the bands from last week — below 1 000 is `"low"`, below 10 000 `"lower-middle"`, below 50 000 `"upper-middle"`, and above that `"high"`. Restrict to 2023, and make sure rows with no `gdp_pc` end up as missing rather than `"high"`.

   Then check: do the group totals add up to the column total? Explain any difference in a markdown cell.
3. Add a column giving each entity's emissions per person **as a percentage of its own 24-year average**, and display Norway's last five years.

### Then: a baseline over part of the period

Climate work rarely compares a year against the whole record — it compares it against a fixed **baseline period**. Compute, for each entity, its average `co2_pc` over **2000–2009**, and then an `anomaly` column giving every row's distance from its own entity's baseline.

The baseline is an average over *some* of the rows and has to end up beside *all* of them, so `transform` will not do it on its own. Compute the baseline as its own small table, then bring it back with a merge — and validate that merge.

Display the five entities with the largest anomaly in 2023. One of the five is not a country. Say in a markdown cell how you can tell, and what you would need in order to remove it.

---

## 📚 Exercise 3: Fifty-five years of the NASDAQ

Load `../data/NASDAQ.csv` — the daily closing level of the NASDAQ Composite index — and convert `Date`
properly, saying the format explicitly.

1. Report the first and last date in the file, and how many trading days fall in each **decade**.
2. Resample to **annual** closing levels and compute the yearly percentage change. Report the five
   best and five worst years, and say what happened in the worst two.
3. Resample to **monthly** closing levels and find the three worst months in the whole series. The
   worst one is more than fifty years old — look up what happened that month.
4. Upsample the daily series to **every calendar day**. How many rows does that produce, how many are
   empty, and what are the empty ones? Then fill them forward, and write a sentence on when carrying
   the last price forward is reasonable and when it is not.
5. Compute the mean level for each month two ways — `groupby` on `.dt.month`, and `resample("ME")` —
   and report how many rows each produces. Explain in a markdown cell what each one is actually
   measuring, and why only one of them belongs on a chart with time along the bottom.

### Then: the lost decade

Using the annual series from question 2, report the closing level at the end of 1999 and at the end of
2009, and the percentage change between them. Then find the first year in which the index closed above
its 1999 level again.

Write a short markdown cell on what that means for the "shares go up over time" claim — and note that
this series is the NASDAQ, which is unusually concentrated in technology companies.

> 💡 **Tip:** `resample` needs the dates as the index and in order — `.set_index("Date").sort_index()`.

## 📚 Exercise 4: Ten files, one table

The folder `../data/stocks/` holds one CSV per company: daily prices and volume for 2020, ten tickers, same columns in each. The company name appears nowhere inside the files — only in the file name.

**Task 1.** Read all ten into a single DataFrame, using `os.listdir` and a loop as described in "Before you start". Add a `ticker` column taken from the file name, convert `Date`, and combine with `concat`. You should end up with 2 520 rows and 10 tickers.

**Task 2.** Check the combined table before you trust it: how many rows are exact duplicates, and how many `ticker`–`Date` combinations appear more than once? Say in a markdown cell why both checks are worth doing, and what it would mean if the second one found something the first did not.

**Task 3.** Compute the total monthly `Volume` for each ticker in three ways, and confirm all three agree.

1. With a **loop** and no pandas grouping at all: an outer loop over tickers, an inner loop over months, collecting the results into lists and building a DataFrame at the end.
2. With `groupby`.
3. With `resample`.

Then write a paragraph comparing them. Which would you actually write, and what did the loop cost you in lines and in the number of places a mistake could hide?

**Task 4.** Using whichever result you prefer, display the five ticker–month combinations with the highest traded volume of 2020.

> 💡 **Tip:** For the loop version, `df["Date"].dt.month` gives you the month of every row, so the inner loop can be `for month in range(1, 13)`.

---

## 📚 Exercise 5: A merge that goes wrong

The point of this exercise is the diagnosis, not the fix. Do it in order, and do not skip ahead to the answer you already know from the lecture.

Load `../data/co2_emissions.csv` and `../data/country_info.csv`.

1. Merge them with an **inner** join, matching the emissions file's `country` against the lookup file's `name`. Report how many rows you had before and how many you have after.
2. Something is missing. Redo the merge as a **left** join with `indicator=True`, and report how many rows matched and how many did not.
3. Identify the entities that failed to match, and then work out *why* they failed even though they are plainly present in both files. Print the evidence, do not just assert it.
4. Fix it **two ways**, and confirm both give the same row count: once by cleaning the key, and once by choosing a better key. Say in a markdown cell which you would use here and which you would use on a file that had no code column.
5. With the merge fixed, add `validate=` set to the shape you believe the merge has. Then deliberately claim the wrong shape and show the error.
6. Now answer the question the previous week could not: drop the aggregates and display the ten countries with the highest total emissions in 2023. Report how many entities the table had before and after dropping them.

---

## 📚 Exercise 6: A loader you will call more than once

Last week you wrote `load_emissions`, and this week's lecture opened by calling it in one line. This
exercise writes its successor — the version that also brings in the country file.

Wrapping loading and cleaning in a function is worth doing for one reason above all: **you run it more
than once.** Here that is literal, because the two questions below need the table two different ways.

Write `load_panel(emissions_path, info_path, countries_only=True)` that:

1. Reads the emissions file and drops rows with no `co2_total`.
2. Adds `co2_pc`, emissions in tonnes per person.
3. Reads the country file and merges it on, bringing across `region` and `incomeLevel`, using the key
   that works and `validate=` set to the right shape.
4. Checks that the merge did not change the row count, and **raises a `ValueError` with a useful
   message** if it did.
5. If `countries_only` is `True`, drops the entities whose region is `"Aggregates"`. If it is `False`,
   keeps them.
6. Returns the result with a clean index. It should not print anything.

Give it a docstring in the longer format, saying what each parameter does, what comes back, and what
it raises.

Then, below the function:

- Call it both ways and confirm you get 4 872 rows with the default and 5 904 with
  `countries_only=False`.
- **Use both results together**: total the 2023 emissions of the 203 countries, and compare that
  against the `World` row, which only exists in the second table. Report the difference and explain it.
- Produce a table of total emissions by region and year, as ordinary columns rather than as an index.
- For 2023, report each region's emissions **per person** — the region's total emissions divided by the
  region's total population, not the average of its countries' figures. Write the calculation as a
  function and apply it to the groups.
- Compare that against the plain average of `co2_pc` within each region, and write a short markdown
  cell on which regions the two disagree about and why.

> 💡 **Tip:** Keep the function in its own cell, with the calls that demonstrate it in the cells
below. A function tangled up with the code that uses it is a function you end up rewriting.

> 💡 **Tip:** A check that raises is worth more than a comment saying what should be true.
`if len(after) != len(before): raise ValueError(...)` turns a silent wrong answer into a stack trace,
which is the trade this whole week has been arguing for.
