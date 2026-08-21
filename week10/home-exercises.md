# Week 10 — Home exercises

Work through these after the lecture. They cover everything from [`10-linear-regression.ipynb`](10-linear-regression.ipynb): fitting a model, reading it off the results object, predictions and residuals, multiple regression, polynomials and logs, categorical variables and interactions, loops over models, and getting results out of Python.

Work in a **notebook**. Solution proposals are in this folder as `home_exercise_N_solution.ipynb`, with their output kept so you can read them without running them. Try each exercise properly before you open them.

> 📝 **Note:** Every exercise assumes your notebook sits in this week's folder, so data is at `../data/`. Start it the way the lecture notebook starts: imports first — including `statsmodels.formula.api as smf` — then `plt.style.use(...)` once for the whole notebook, then the data.

> 💡 **Tip:** Every model you fit, check `No. Observations` or `int(results.nobs)` against the number of rows you thought you had. `statsmodels` drops rows with missing values silently, and every exercise below has missing values in it somewhere.

The lecture used `mpg.xlsx` throughout. These use two datasets you have not modeled before — which is the point, because that is what an exam question does.

---

## Version control (optional)

If you want the practice: open a terminal in this week's folder, run `git init`, and make a first commit before you start. Then commit after each exercise, with a message saying what you did.

Add a `.gitignore` containing `__pycache__/`, `.ipynb_checkpoints/`, `*.png`, `*.xlsx` and `*.tex`. The last three matter this week: exercises 3 and 4 write figures and tables, and a result your code produced is not something to commit. If your raw data lives in the same folder, name the derived files something you can match on — `output-*.xlsx` — rather than excluding every spreadsheet you own.

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

Back to `../data/mpg.xlsx`. The lecture fitted `mpg` on horsepower three different ways and left the obvious question open: is horsepower even the right variable?

1. Load the file and drop the rows with no `horsepower`.
2. Write a function `get_adj_r2(data, formula)` that fits a model and returns its adjusted R-squared.
3. Loop over the four attributes `horsepower`, `weight`, `acceleration` and `model_year`. For each one, fit **three** models — a straight line, a second-order polynomial, and a log of the predictor — and use your function to collect the adjusted R-squared of each. Put all twelve numbers into a single DataFrame with one row per attribute and one column per shape.
4. Which single attribute explains the most? For that attribute, does the shape matter much?
5. Now the same question about `cylinders`, which is stored as a number but takes only five values. Fit `mpg ~ horsepower + cylinders` and `mpg ~ horsepower + C(cylinders)` and compare the adjusted R-squared. Print how many cars have each number of cylinders, and say in a markdown cell whether you would use the categorical version and what it costs you.
6. Finally, put your best two attributes together in one model, and say whether the whole is worth more than the parts.

> ⚠️ **Warning:** In question 3 you are comparing twelve models that all explain the **same** dependent variable, `mpg`, on the same rows — so their R-squared values are comparable. Change the left-hand side of any of them and that stops being true.

---

## 📚 Exercise 3: What makes a country emit

The table from the last three weeks, modeled. Load `../data/co2_emissions.csv` and `../data/country_info.csv`, merge them on the key that works, drop the aggregates, and add `co2_pc`.

**Use 2021, not 2023.** `renew_energy` and `nat_resources` have no values at all for 2022 or 2023, so a 2023 cross-section with those columns in it has zero complete rows. Confirm that for yourself before you take my word for it.

1. Build the 2021 cross-section, keeping the rows with a value for `co2_pc`, `gdp_pc`, `urban`, `electricity` and `renew_energy`. Report how many countries you have, and how many you lost.
2. Draw a scatter of `co2_pc` against `gdp_pc`. Then fit `co2_pc ~ gdp_pc` and add the fitted line. Report the R-squared, and say what is wrong with the picture.
3. Fit three models of the same relationship: levels, a log of GDP only, and log on **both** sides. Report the R-squared of each — and say in a markdown cell why only two of the three are comparable.
4. Interpret the log–log coefficient in one sentence, in percentages.
5. Build a set of specifications with a loop, adding one variable at a time to the log–log model: `renew_energy`, then `urban`, then `C(region)`. Collect the adjusted R-squared and the coefficient on log GDP into one table. Does the elasticity survive the controls?
6. Draw the residual plot for your preferred model. Is there structure left in it?
7. Export two things: a summary table of the mean `co2_pc` and mean `gdp_pc` by region, as `.xlsx`, and your set of models as one regression table, as `.tex`.

---

## 📚 Exercise 4: One model per region

Same 2021 cross-section as exercise 3. The pooled model in question 5 gave every country in the world one elasticity. This exercise asks whether that was a fair thing to do.

1. Loop over the seven regions. For each one with **at least ten countries**, fit `np.log(co2_pc) ~ np.log(gdp_pc)` and record the region, the number of countries, the coefficient and its 95% confidence interval. Report which regions you skipped and why.
2. Put the results in a DataFrame sorted by coefficient, and draw them as a horizontal figure with error bars showing the confidence intervals. Add a vertical reference line at the pooled elasticity from exercise 3.
3. Find two regions whose confidence intervals do not overlap at all. Name them, and say in one sentence what that means in plain language about income and emissions in those parts of the world.
4. Some of the intervals contain zero. Pick one, say what that means, and say whether it means the relationship is absent there.
5. Now fit the interacted model `np.log(co2_pc) ~ np.log(gdp_pc) * C(region)` on all the countries at once. Reconstruct each region's slope from the coefficients and check them against the ones from your loop.
6. In a markdown cell: which of the two — seven separate models or one interacted model — would you put in a report, and what question is each one answering?

> 💡 **Tip:** In question 5 the reference region is the one with no term of its own in the output. Every other region's slope is the baseline coefficient **plus** its interaction term.
