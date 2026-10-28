# Week 10 — Home exercises

Work through these after the lecture. They cover everything from [`10-linear-regression.ipynb`](10-linear-regression.ipynb): fitting a model, reading it off the results object, predictions and residuals, multiple regression, polynomials and logs, categorical variables and interactions, loops over models, and getting results out of Python.

Work in a **notebook**. Solution proposals are in this folder as `home_exercise_N_solution.ipynb`, with their output kept so you can read them without running them. Try each exercise properly before you open them.

> 📝 **Note:** Every exercise assumes your notebook sits in this week's folder, so data is at `../data/`. Start it the way the lecture notebook starts: imports first — including `statsmodels.formula.api as smf` — then `plt.style.use(...)` once for the whole notebook, then the data.

> 💡 **Tip:** Every model you fit, check `No. Observations` or `int(results.nobs)` against the number of rows you thought you had. `statsmodels` drops rows with missing values silently, and every exercise below has missing values in it somewhere.

---

## 📚 Exercise 1: One respondent out of 2,884

`../data/survey_data.csv` has 2,884 people, their hourly earnings in DKK, their years of schooling, their years of work experience, their sex and whether they work in the public or private sector. It is **colon-separated**, so it needs `sep=":"`.

This exercise is about how much one row can be worth.

1. Load the file and look at it. How many respondents earn **less than 10 DKK** an hour, and how many earn **more than 1,000**? What are the minimum and the maximum?
2. Report the mean hourly earnings for each combination of `sex` and `sector` — four numbers, in one table.
3. Draw a histogram of `hourly_earnings`. Then draw a second one with the axis limited to the bulk of the data. Say in a markdown cell which one you would show somebody and why.
4. Write a function `get_beta(data, formula, variable)` that fits a model and returns the coefficient on one named variable. Give it a docstring. Demonstrate it on

   `hourly_earnings ~ years_schooling + experience + I(experience**2)`

   and print the coefficient on `years_schooling`.
5. Now the question. **How much does the answer depend on any single respondent?** Write a loop that, for each row in turn, drops that one row, refits the model, and records the coefficient. Report the smallest and largest coefficient you get, and identify the respondent whose removal changes it most. Print that respondent's row.
6. In a markdown cell: is the coefficient on schooling robust or fragile? What would you do about the respondent you found, and what would you have to tell a reader either way?

> 💡 **Tip:** Question 5 fits nearly three thousand models and takes about half a minute. That is fine — but write it on a small slice first (`data.head(50)`) to check the loop works before you set it going on everything.

---

## 📚 Exercise 2: Which variable, and in what shape

Back to `../data/mpg.xlsx`. The lecture fitted `mpg` on horsepower as a straight line, as a polynomial and on a log scale, and left the obvious question open: is horsepower even the right variable?

1. Load the file and drop the rows with no `horsepower`.
2. Write a function `get_adj_r2(data, formula)` that fits a model and returns its adjusted R-squared.
3. Loop over the four attributes `horsepower`, `weight`, `acceleration` and `model_year`. For each one, fit **three** models — a straight line, a second-order polynomial, and a log of the predictor — and use your function to collect the adjusted R-squared of each. Put all twelve numbers into a single DataFrame with one row per attribute and one column per shape.
4. Which single attribute explains the most? For that attribute, does the shape matter much?
5. Now a question about shape of a different kind. `cylinders` is stored as a number, but it takes only five values. As a **number** it forces the model into a straight line: going from 4 to 6 cylinders must have exactly the same effect as going from 6 to 8. As a **category**, `C(cylinders)`, each value gets its own intercept and no such assumption is made. Fit `mpg ~ horsepower + cylinders` and `mpg ~ horsepower + C(cylinders)` and compare the adjusted R-squared. Print how many cars have each number of cylinders, and say in a markdown cell whether you would use the categorical version and what it costs you.
6. Finally, put your best two attributes together in one model, and say whether the whole is worth more than the parts.

> ⚠️ **Warning:** In question 3 you are comparing twelve models that all explain the **same** dependent variable, `mpg`, on the same rows — so their R-squared values are comparable. Change the left-hand side of any of them and that stops being true.

---

## 📚 Exercise 3: What makes a country emit

The emissions table you have already wrangled and plotted, now modeled. Load `../data/co2_emissions.csv` and `../data/country_info.csv`, merge them on the key that works, drop the aggregates, and add `co2_pc`.

**Use 2021, not 2023.** `renew_energy` and `nat_resources` have no values at all for 2022 or 2023, so a 2023 cross-section with those columns in it has zero complete rows. 

1. Build the 2021 cross-section, keeping the rows with a value for `co2_pc`, `gdp_pc`, `urban`, `electricity` and `renew_energy`. Report how many countries you have, and how many you lost.
2. Draw a scatter of `co2_pc` against `gdp_pc`. Then fit `co2_pc ~ gdp_pc` and add the fitted line. Report the R-squared, and say what is wrong with the picture.
3. Fit three models of the same relationship: levels, a log of GDP only, and log on **both** sides. Report the R-squared of each — and say in a markdown cell why only two of the three are comparable.
4. Interpret the log–log coefficient in one sentence, in percentages.
5. Build a set of specifications with a loop, adding one variable at a time to the log–log model: `renew_energy`, then `urban`, then `C(region)`. Collect the adjusted R-squared and the coefficient on log GDP into one table. Does the elasticity survive the controls?
6. Draw the residual plot for your preferred model. Is there structure left in it?
7. Export two things: a summary table of the mean `co2_pc` and mean `gdp_pc` by region, as `.xlsx`, and your set of models as one regression table, as `.tex`.

---

## 📚 Exercise 4: What an interaction does

Same 2021 cross-section as exercise 3. The pooled model in question 5 there gave every country in the world one elasticity. An interaction lets each region have its own — in one model, with an adjustment to the slope for every region except the reference.

This exercise builds the same thing the long way, one regression per region, to see exactly what the interaction is doing and where the two approaches part company.

1. Fit `np.log(co2_pc) ~ np.log(gdp_pc) * C(region)` on all the countries. Which region is the reference, and how can you tell from the output? Reconstruct every region's slope from the coefficients.
2. Now the long way. Loop over the seven regions. For each one with **at least ten countries**, fit `np.log(co2_pc) ~ np.log(gdp_pc)` on that region's rows alone, and record the region, the number of countries, the coefficient and its 95% confidence interval. Report which regions you skipped and why.
3. Put the slopes from the loop next to the ones you reconstructed in question 1. What do you find? And what does the interacted model report for the regions the loop skipped — should you believe it?
4. **Same slope, different uncertainty.** For the reference region, compare the 95% confidence interval from its own regression in question 2 with the interval on `np.log(gdp_pc)` in the interacted model. Which is narrower, and why?
5. Draw the slopes from the loop as a horizontal figure with error bars (see tip below) showing their confidence intervals, sorted by coefficient. Add a vertical reference line at the pooled elasticity from exercise 3.
6. Find two regions whose intervals do not overlap at all, and say in one sentence what that means in plain language about income and emissions in those parts of the world. Then pick a region whose interval contains zero: does that mean there is no relationship there?
7. Back to the interacted model. Print the p-values of the interaction terms. Which regions have a slope that differs significantly from the reference region's? In a markdown cell: what question does the interacted model answer that seven separate regressions cannot?

> 💡 **Tip:** The loop in question 2 is a pattern worth knowing. Start with an empty list; for each region, filter its rows, fit, and `append` a dictionary of the numbers you want; then `pd.DataFrame(your_list)` turns the list into a table with one row per region. A guard like `if len(group) < 10: continue` skips a region before fitting it — a regression on three rows will run, return numbers, and mean nothing, and nothing will warn you.

> 💡 **Tip:** `ax.errorbar(x, y, xerr=..., fmt="o", capsize=4)` draws points with horizontal bars through them. `xerr` takes the *distance* from each point to the ends of its bar, so for an interval that is not symmetric around the estimate, pass a list of two: `[estimate - low, high - estimate]`.
