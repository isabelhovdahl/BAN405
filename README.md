# BAN405 — Python Programming for Data Science

Course material for **BAN405** at NHH Norwegian School of Economics (7.5 ECTS, autumn semester).
Course description: <https://www.nhh.no/en/courses/python-programming-for-data-science/>

> ⚠️ **Material is subject to change until the link for that week has been posted on Canvas.**
> Everything is published up front so you can work ahead if you want to — but until a week goes
> live on Canvas, its content may still be revised.

---

## What this course is

The course is a full programming course in two parts.

**Part 1 (weeks 1–4) — Python basics.** You build programs: variables and data structures, control
flow, loops, functions, error handling. No data analysis yet, and that is deliberate — you learn to
write and reason about code before you learn to analyse with it.

**Interlude (weeks 5–6) — the tools of the trade.** Version control with git and GitHub, conda
environments, project structure and file paths. These are the things that turn a script into work
someone else can reproduce.

**Part 2 (weeks 7–11) — data analysis.** pandas, plotting with matplotlib, data wrangling, linear
regression, and exam preparation.

If you have taken the **SKL401** seminar, you have met many of these topics already. BAN405 covers
them considerably more deeply, spends four weeks on programming before touching data, and adds
version control, environments and reproducibility, which SKL401 does not cover at all.

---

## Getting started

1. Install the software — see [`guides/`](guides/).
2. Download **`ban405-workspace.zip`** from this repository and unzip it somewhere sensible on your
   computer (**not** in OneDrive, Dropbox or Google Drive). It contains the datasets and an empty
   folder for each week.
3. Each week, follow the Canvas link to that week's material, click **Download raw file**, and save
   the notebook into the matching week folder in your workspace.

Your workspace should end up looking like this:

```
BAN405/
├── data/          ← datasets, already filled in
├── images/
├── week01/        ← put week 1's notebook here
├── week02/
└── …
```

Keeping this structure matters: the notebooks load data with paths like `../data/mpg.xlsx`, which
only work if the notebook sits in a week folder next to `data/`.

> 📝 **Please don't clone this repository.** Download the individual files instead. If you clone and
> then edit the notebooks, you will hit merge conflicts every time the material is updated. (We come
> back to exactly why in week 5.)

---

## Schedule

| Week | Topic | Material | |
|---|---|---|---|
| 1 | Python basics | [`week01/`](week01/) | |
| 2 | Decisions | [`week02/`](week02/) | |
| 3 | Loops | [`week03/`](week03/) | |
| 4 | Functions and error handling | [`week04/`](week04/) | Assignment 1 out |
| 5 | Terminal, git and GitHub | [`week05/`](week05/) | |
| 6 | Conda environments and project structure | [`week06/`](week06/) | Assignment 1 due |
| 7 | Pandas basics | [`week07/`](week07/) | |
| 8 | Plotting | [`week08/`](week08/) | |
| 9 | Data wrangling | [`week09/`](week09/) | Assignment 2 out |
| 10 | Linear regression | [`week10/`](week10/) | |
| 11 | Exam preparation | [`week11/`](week11/) | Assignment 2 due |

Assignments: [`assignments/`](assignments/) · Guides: [`guides/`](guides/)

---

## Assessment

- **6-hour digital school exam** with access to Python. There is **no internet** in the exam, so
  everything you write must run from local files.
- **Two mandatory assignments**, both of which must be approved for course approval.

---

## Software

| Tool | |
|---|---|
| [Positron](https://positron.posit.co/) | The editor used throughout the course |
| [Miniforge](https://github.com/conda-forge/miniforge) | Python distribution and the `conda` package manager |
| [Git](https://git-scm.com/) | Version control, from week 5 |

Installation instructions are in [`guides/`](guides/).

---

## License

Material in this repository is licensed under
[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). See [`LICENSE`](LICENSE).

Author: Isabel Hovdahl, NHH Norwegian School of Economics.
