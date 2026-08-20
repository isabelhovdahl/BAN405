# BAN405 — Python Programming for Data Science

Author: Isabel Hovdahl, NHH Norwegian School of Economics.

Course material for **BAN405** at NHH Norwegian School of Economics.
Course description: <https://www.nhh.no/en/courses/python-programming-for-data-science/>

The course is a full programming course in two parts.

**Part 1 (weeks 1–4) — Python basics.** You build programs: variables and data structures, control flow, loops, functions, error handling. 

**Interlude (weeks 5–6) — the tools of the trade.** Version control with git and GitHub, and conda environments. These are the things that turn code into work someone else can reproduce.

**Part 2 (weeks 7–10) — data analysis.** pandas, summarizing and combining data, visualization with matplotlib, and linear regression.

---

## Course schedule

Weeks are numbered relative to the start of the course, not by calendar week — week 01 is the first lecture.

| Week | Topic |
|---|---|
| [01](week01/) | Positron and Python basics |
| [02](week02/) | Decisions |
| [03](week03/) | Loops |
| [04](week04/) | Functions |
| [05](week05/) | The terminal, git and GitHub |
| [06](week06/) | Conda and project structure |
| [07](week07/) | Pandas basics |
| [08](week08/) | Summarizing and combining data |
| [09](week09/) | Visualization |
| [10](week10/) | Linear regression |

Each week folder holds that week's lecture notebook, a `home-exercises.md` to work through before the next session, and a solution proposal for each home exercise. Some weeks also have slides.

---

## Getting started

1. Install the software and watch the pre-work videos — see [`guides/`](guides/).
2. Download **`ban405-workspace.zip`** from this repository and unzip it somewhere sensible on your computer (**not** in OneDrive, Dropbox or Google Drive). It contains the datasets and an empty folder for each week.
3. Each week, follow the Canvas link to that week's material, click **Download raw file**, and save the notebook into the matching week folder in your workspace.

Your workspace should end up looking like this:

```
BAN405/
├── data/          ← datasets, already filled in
├── week01/        ← put week 1's notebook here
├── week02/
└── …
```

Keeping this structure matters: the notebooks load data with paths like `../data/mpg.xlsx`, which only work if the notebook sits in a week folder next to `data/`.

> ⚠️ **Material is subject to change until the link for that week has been posted on Canvas.**
> Everything is published up front so you can browse ahead if you want to — but until a week goes live on Canvas, its content will still be revised.

---

## License

Material in this repository is licensed under
[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). You are welcome to use the material for your own teaching or study. If you find the material useful, I would be glad to hear about it.
