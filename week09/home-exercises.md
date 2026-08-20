# Week 09 — Home exercises

Work through these before the next lecture. They cover everything from [`09-visualization.ipynb`](09-visualization.ipynb): `fig` and `ax`, reshaping with `pivot` and `melt`, the four chart types, customizing a figure, several panels in one figure, writing a function that draws one, and saving it.

Work in a **notebook**, as last time. Solution proposals are in this folder as `home_exercise_N_solution.ipynb`, with their output kept so you can read them without running them. Try each exercise properly before you open them.

> 📝 **Note:** Every exercise assumes your notebook sits in this week's folder, so data is at `../data/`. Start it the way the lecture notebook starts: import what you need — including `matplotlib.pyplot as plt` — load your own data, and make sure the whole thing runs from top to bottom before you call it finished.

> 💡 **Tip:** Every figure below needs axis labels with units and a title. That is not a house style; it is the difference between a figure and a sketch, and it is worth marks on anything you ever submit. Get into the habit now, while the charts are small enough that adding them is trivial.

---

## Version control (optional)

If you want the practice: open a terminal in this week's folder, run `git init`, and make a first commit before you start. Then commit after each exercise, with a message saying what you did. When you are finished, `git log --oneline` shows you your own week.

Add a `.gitignore` containing `__pycache__/`, `.ipynb_checkpoints/` and `*.png`. The last line matters this week: exercises 3 and 5 write image files, and a saved figure is something your code produced rather than something you wrote. Commit the code, not its output — if the figure changes, re-running the notebook is what should change it.

This is optional and nothing depends on it. If yours ends up in a state you cannot fix, delete the `.git` folder. Your files are untouched, and you start fresh next week.

---

## 📚 Exercise 1: The same chart, two shapes

The lecture drew one chart from a long table and the same chart from a wide one. This exercise makes you do both, and then decide.

Load `../data/co2_emissions.csv` and `../data/country_info.csv`, merge them so that every row carries a `region`, and drop the entities whose region is `"Aggregates"`.

1. Build a **long** table of the average `co2_pc` for each region in each year — one row per region per year, three columns. Report its shape.
2. Draw a chart with one line per region, **working from the long table**, using a loop and one call to `ax.plot` per group. Label the axes, give it a title, and add a legend.
3. Turn the long table into a **wide** one with `pivot`: one row per year, one column per region. Report its shape, and check that it holds the same number of numbers as the long table did.
4. Draw the same chart again from the wide table, in **one** call. It should look identical.
5. Use `melt` to turn the wide table back into a long one, and confirm you get the same number of rows you started with.
6. In a markdown cell, answer two questions. Which of the two tables would you save to a file, and why? And which of the two chart cells would you rather come back to in six months?

> 💡 **Tip:** Question 6 is the point of the exercise. Both charts are correct, so there is no right answer to look up — there is only the one you can defend.

---

## 📚 Exercise 2: Four questions about 398 cars

`../data/mpg.xlsx` has 398 American, European and Japanese cars from model years 1970 to 1982, with their fuel economy in miles per gallon, their weight, their engine size and where they were built. It is a small table with four genuinely different questions in it, and this exercise asks one of each.

Load it, and look at it before you draw anything: shape, columns, and how many values are missing in each column.

1. **How did something change over time?** Draw a line chart of average `mpg` by `model_year`. Then add a line per `origin` to the same axes, with a legend. Say in a markdown cell what happened between 1979 and 1980, and how confident you are that the chart shows what it appears to show.
2. **How do categories compare?** Draw a bar chart of average `mpg` by `origin`. Put the number of cars behind each bar somewhere a reader will see it.
3. **Are two variables related?** Draw a scatter plot of `weight` against `mpg`. Then color the points by `origin` and add a legend. Report the correlation between the two variables.
4. **How is one variable spread out?** Draw a histogram of `mpg`. Try at least two different values of `bins` and keep the one that shows the most, then mark the mean and the median with vertical lines.
5. In a markdown cell, write the single sentence each of the four figures is making. If two of them make the same sentence, say which one you would drop.

> ⚠️ **Warning:** One of the four charts in question 1 has a group whose 1982 average is computed from a very small number of cars. Find it before you write anything about a trend.

---

## 📚 Exercise 3: Fifty-five years, finished properly

You have used `../data/NASDAQ.csv` before, to answer questions. This time the answer *is* the figure, so it has to be finished.

Load it, convert `Date` with an explicit format, set it as the index and sort it.

1. Resample to **monthly** closing levels and draw everything from 1990 onwards as a line. Notice how bad it looks, and say in a comment why.
2. Fix the vertical axis so that a percentage fall in 1995 takes up the same space as the same percentage fall in 2020. Label it so the reader knows what you did.
3. Shade the **dot-com crash**, from the March 2000 peak to the October 2002 low, and the **financial crisis**, from the October 2007 peak to the March 2009 low. Find those four dates from the data rather than typing them in — `idxmax` and `idxmin` on a slice of the series give you the date of the highest and lowest value in it.
4. Report the percentage fall in each of the two crashes, and write both onto the figure with `ax.text`.
5. Add a grid, a title, and axis labels, and save the figure as a `.png` at 300 dpi with the whitespace cropped.
6. Now a different chart of the same data: compute the **annual return** for every year from 1990, and draw it as a bar chart with one bar per year. Color the negative years differently from the positive ones. In a markdown cell, say which of your two figures you would put in a report about the NASDAQ, and what question each one answers.

> 💡 **Tip:** For question 6 you need a list of colors, one per bar. A list comprehension over the returns gives you one in a single line, and `ax.bar` accepts it as its `color` argument.

---

## 📚 Exercise 4: One function, any country

The lecture wrote `plot_region`. This is its sibling, and it is the shape of function most worth being able to write from memory.

Load and merge the two data files as in exercise 1, drop the aggregates, and add `co2_pc`.

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

Use the same merged table as exercise 4.

1. **One file per group.** Loop over the seven regions and, for each one, draw total emissions over time and save it as its own `.png`. Build the file name from the region with an f-string. Check afterwards that seven files appeared, using `os.listdir`.
2. Two of the region names contain characters that make an awkward file name. Deal with it — `.replace()` on the string is enough — and say in a comment what you would do if the names came from a file you did not control.
3. **One figure, several panels.** Draw a 2×2 grid comparing `"China"`, `"United States"`, `"India"` and `"Germany"`: emissions per person over time, one country per panel, on a **shared y-axis**. Give the figure a `suptitle`.
4. Draw the grid a second time *without* sharing the y-axis, and in a markdown cell say what a reader would conclude from each version and which conclusion is right.
5. Finally, put all four countries on **one** set of axes as four lines with a legend. In a markdown cell, say which of the three figures you would use, and for what.

> 💡 **Tip:** Question 5 is the real question. A grid of panels and a single chart with several lines answer different questions: one is *"what did each of these look like?"* and the other is *"how do these compare?"* Neither is the default.
