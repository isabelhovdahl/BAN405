# data

All datasets used in the course live here, in a single flat folder — one copy of each file, no
subfolders.

Lecture notebooks sit in a week folder next to this one, so they load data with a path like:

```python
df = pd.read_excel("../data/mpg.xlsx")
```

This is why you need the folder structure from `ban405-workspace.zip` rather than just a loose
notebook. See week 6 for the full treatment of relative paths, absolute paths and URLs.

> 📝 Note that Assignment 2 and the exam use a different layout — the notebook sits at the project
> root with `data/` beside it, so the path there is `data/x.csv` with no `../`. Understanding why
> the two differ is the point.

*Datasets will be added here before the course starts.*
