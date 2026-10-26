# Week 09 — Home exercises

Work through these before the next lecture. They cover everything from [`09-visualization.ipynb`](09-visualization.ipynb): `fig` and `ax`, reshaping with `pivot`, the four chart types and the box plot, customizing a figure, several panels in one figure, writing a function that draws one, saving it, and a line drawn through missing data.

Work in a **notebook**. Solution proposals are in this folder as `home_exercise_N_solution.ipynb`, with their output kept so you can read them without running them. Try each exercise properly before you open them.

> 📝 **Note:** Every exercise assumes your notebook sits in this week's folder, so data is at `../data/`. Start it the way the lecture notebook starts: import what you need — including `matplotlib.pyplot as plt` — and, for every exercise that uses the emissions data, copy the lecture's `load_panel` function into the top of your notebook and call it. Make sure the whole thing runs from top to bottom before you call it finished.

---

## Before you start

Three things the lecture did not cover, each needed by one of the exercises below.

### A second y-axis: `ax.twinx()`

Sometimes two quantities belong on the same figure but are measured in units nowhere near the same size. `ax.twinx()` makes a second set of axes that shares the x-axis of `ax` and has its own y-axis on the right:

```python
right = ax.twinx()

right.plot(x, other_values, color="tab:orange")
right.set_ylabel("Other quantity, units", color="tab:orange")
```

Everything you know about `ax` works on `right`. A reader cannot tell which line belongs to which axis, so give each line its own color and write its axis label in the same color. Exercise 2 uses it.

### Choosing the ticks on a date axis

The lecture used `set_major_formatter` to change how a tick value is *written*. On a date axis you usually want to change **which** ticks appear as well. matplotlib picks them for you, and on a thirty-five year series its choice is often not the one you want.

The date versions live in a module of their own, `matplotlib.dates`:

```python
import matplotlib.dates as mdates

ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
```

A **locator** decides where the ticks go; a **formatter** decides what they say. `YearLocator(5)` puts one every five years, and `DateFormatter` takes the same `%Y`, `%b`, `%m` codes you already used with `pd.to_datetime`.

`mdates.MonthLocator()` does the same job for a shorter series, and `mdates.DateFormatter("%b %Y")` gives you `Jan 2020` instead of `2020`. Exercise 3 uses it.

### Pointing at something: `ax.annotate`

`ax.text` puts words at a position. `ax.annotate` puts words at one position and draws an arrow to another, which is what you want when the thing you mean is a single point — a peak, a low, one odd observation:

```python
ax.annotate(
    "the low",
    xy=(low_date, low_value),
    xytext=(pd.Timestamp("2005-01-01"), 300),
    arrowprops={"arrowstyle": "->"},
)
```

`xy` is the point the arrow points **at**, and `xytext` is where the words go. Both are in the units of the data, so on a date axis the x coordinates are dates. `arrowprops` is a dictionary describing the arrow, and `{"arrowstyle": "->"}` is a plain one. Exercise 3 uses it.

---

## 📚 Exercise 1: Two wide tables, and when to stack

The lecture moved between a long and a wide table and drew one line per region from each. This exercise takes the wide shape somewhere the lecture did not: a stacked bar chart, and the question of when stacking is allowed at all.

Load the data with `load_panel`.

1. Build a **wide** table of the average `co2_pc` across the countries of each region: one row per year, one column per region. Report its shape.
2. Draw it in **one** call, one line per region, with labels, a title that says which average this is, and a legend.
3. Build a **second** wide table, this time of *total* `co2_total` by region and year, and draw it as a **stacked** bar chart — one bar per year, one segment per region. `df.plot(kind="bar", stacked=True)` does it in one line. Then answer in a comment: why does stacking make sense for this table and not for the one you built in question 1?
4. From the totals table, compute East Asia & Pacific's and North America's share of the world total in 2000 and in 2023. Which part of the stacked chart shows that change, and how easy is it to read off?
5. In a markdown cell, answer two questions. If you were saving these numbers to a file, would you save them long or wide, and why? And the lecture drew one line per region both with a loop and in one call — which of the two would you rather come back to in six months?

> 💡 **Tip:** Question 5 is the point of the exercise. Both shapes and both chart cells are correct, so there is no right answer to look up — there is only the one you can defend.

---

## 📚 Exercise 2: Four questions about 398 cars

`../data/mpg.xlsx` has 398 American, European and Japanese cars from model years 1970 to 1982, with their fuel economy in miles per gallon, their weight, their engine size and where they were built. It is a small table with four genuinely different questions in it, and this exercise asks one of each.

Load it, and look at it before you draw anything: shape, columns, and how many values are missing in each column.

1. **How did something change over time?** Draw a line chart of average `mpg` by `model_year`. Then add a line per `origin` to the same axes, with a legend. Say in a markdown cell what happened between 1979 and 1980, and how confident you are that the chart shows what it appears to show.
2. **How do categories compare?** Draw a bar chart of average `mpg` by `origin`. Then draw the same comparison as a box plot, one box per origin, and say in a markdown cell what the box plot shows that the bars do not.
3. **Are two variables related?** Draw a scatter plot of `horsepower` against `mpg`. How many cars are in your figure, and why is it not 398? Then color the points by `origin` and add a legend.
4. **How is one variable spread out?** Draw a histogram of `mpg`. Try at least two different values of `bins` and keep the one that shows the most, then mark the mean and the median with vertical lines.
5. **Two quantities, two scales.** Cars got lighter and more efficient over the period, and the two numbers are nowhere near the same size — weight is in thousands of pounds, `mpg` is in tens. Draw average `weight` and average `mpg` by `model_year` on one figure, with a second y-axis from `ax.twinx()` (see **Before you start**). Label both y-axes, and give each line a color that matches its axis label.
6. In a markdown cell, write the single sentence each of your figures is making. If two of them make the same sentence, say which one you would drop.

> ⚠️ **Warning:** One of the lines in question 1 has a 1982 average computed from a very small number of cars. Find it before you write anything about a trend.

> ⚠️ **Warning:** A twin-axis chart lets you put any two series side by side at any scale, so it can make almost anything look related. Use it when both quantities genuinely belong on the same figure, and never without labeling which line belongs to which axis.

---

## 📚 Exercise 3: Three crashes, finished properly

The lecture took `../data/NASDAQ.csv` from 1971 and finished one figure: a log scale, the dot-com crash shaded, and its fall written on the chart. This exercise starts where the lecture stopped and adds the two crashes that came after.

Load it, convert `Date` with an explicit format, set it as the index and sort it.

1. Resample to **monthly** closing levels and draw everything from 1990 onwards as a line on a log scale, labeled so the reader knows it is one.
2. Shade the **financial crisis**, from the October 2007 peak to the March 2009 low, and the **COVID crash**, from the February 2020 peak to the March 2020 low. Find those four dates from the data rather than typing them in — `idxmax` and `idxmin` on a slice of the daily series give you the date of the highest and lowest value in it.
3. Report the percentage fall in each crash, computed from the **daily** series. Then look at your monthly line around 2020 and say in a comment why the COVID crash barely shows on it.
4. Write each fall onto the figure with `ax.annotate` (see **Before you start**), with the arrow pointing at the low.
5. Add a grid, a title, axis labels, and a tick every five years using the locator and formatter from **Before you start**. Then save the figure as a `.png` at 300 dpi with the whitespace cropped.
6. Now a different chart of the same data: compute the **annual return** for every year from 1990, and draw it as a bar chart with one bar per year. Color the negative years differently from the positive ones. In a markdown cell, say which of your two figures you would put in a report about the NASDAQ, and what question each one answers.

> 💡 **Tip:** For question 6 you need a list of colors, one per bar. A list comprehension over the returns gives you one in a single line, and `ax.bar` accepts it as its `color` argument.

---

## 📚 Exercise 4: One function, any country

**This exercise deliberately repeats the lecture.** The lecture wrote `plot_region`; this is its sibling, and it is the shape of function most worth being able to write from memory. So close the lecture notebook and write it without looking.

Load the data with `load_panel`.

Write `plot_country(data, country)` that:

1. Raises a `ValueError` with a useful message if `country` does not appear in `data["country"]`.
2. Draws emissions per person over time for that country as a line.
3. Adds a horizontal reference line at the **world figure for 2023** — total emissions of every country divided by total population, which is 4.68 tonnes per person. Label it so the reader knows what the line is.
4. Labels both axes with units, and puts the country's name in the title.
5. Starts the y-axis at zero, so that the size of the change is honest.
6. Returns the figure.

Give it a docstring in the longer format, saying what each parameter does, what comes back and what it raises.

Then, below the function:

- Demonstrate it for `"China"` and for `"United States"`.
- Show the error by calling it with a country name that is not in the file.
- In a markdown cell, say what the two figures together show, and what a reader would miss if you only showed one of them.

> 💡 **Tip:** The reference line is a constant, so it goes in the function as a default argument rather than being hard-coded in the middle of it. `def plot_country(data, country, reference=4.68):` costs nothing and lets the caller change it.

---

## 📚 Exercise 5: A figure per group, and a grid

Two ways of showing several groups at once, and they are not interchangeable.

Load the data with `load_panel`.

1. **One file per group.** Loop over the seven regions and, for each one, draw total emissions over time and save it as its own `.png`. Build the file name from the region with an f-string. Check afterwards that seven files appeared, using `os.listdir`.
2. Several of the region names contain characters that make an awkward file name — four of them have an `&`, and one has a comma as well. Deal with it — `.replace()` on the string is enough — and say in a comment what you would do if the names came from a file you did not control.
3. **One figure, several panels.** Draw a 2×2 grid comparing `"China"`, `"United States"`, `"India"` and `"Germany"`: emissions per person over time, one country per panel, on a **shared y-axis**. Add the same dashed reference line at 4.68 tonnes to every panel, and give the figure a `suptitle`. Make sure a reader can tell what the dashed line is, without repeating the same legend four times.
4. Draw the grid a second time *without* sharing the y-axis, and in a markdown cell say what a reader would conclude from each version and which conclusion is right.
5. Finally, put all four countries on **one** set of axes as four lines with a legend. In a markdown cell, say which of the three figures you would use, and for what.

> 💡 **Tip:** In question 1, end the loop body with `plt.close(fig)` once the figure is saved. Without it every figure stays open — in a notebook all seven are drawn under the cell, and in a loop over two hundred countries the kernel slows to a crawl.

> 💡 **Tip:** Question 5 is the real question. A grid of panels and a single chart with several lines answer different questions: one is *"what did each of these look like?"* and the other is *"how do these compare?"* Neither is the default.

---

## 📚 Exercise 6: A gap in the line

The lecture's Timor-Leste figure showed a line chart drawing straight through years with no data. Timor-Leste is not the only country in the file where that happens.

Load the data with `load_panel`.

1. Find every country whose `nat_resources` series has a gap **inside** it: missing in at least one year, with figures both before and after. Missing years at the start or the end of a series do not count — there is nothing on the other side for a line to join them to.
2. Pick the country on your list that is not Timor-Leste, and draw its `nat_resources` twice, side by side on a shared y-axis: on the left after `dropna()`, on the right with the missing years left in. Give each panel a title saying which is which.
3. In a markdown cell, say what the left-hand panel claims about the missing years, and what the data actually says about them.

> 💡 **Tip:** For question 1, compare two numbers per country: how many years have a figure, and how many years lie between the first and the last year with a figure. If the second is larger, something is missing in between. `groupby` with `.agg()` gives you all three ingredients in one table.
