# Guides

Setup guides and references. Work through all steps **before** the first lecture.

## Before the course

### 1. Install the software

Install in this order. Miniforge comes first because Positron looks for a Python installation when it starts, and Miniforge is the one it should find.

| # | Tool | Guide |
| --- | --- | --- |
| 1 | Miniforge | [Windows](install-miniforge-windows.md) &nbsp;·&nbsp; [Mac](install-miniforge-mac.md) |
| 2 | Positron | [Install guide](install-positron.md) (same guide for Windows and Mac) |
| 3 | Git | [Windows](install-git-windows.md) &nbsp;·&nbsp; [Mac](install-git-mac.md) |

### 2. Check that it all works

Go through the **[verification checklist](verify-installation.md)**. If something is broken, please contact me before the first lecture.

### 3. Watch the pre-work videos

These videos come from [SKL401](https://isabelhovdahl.github.io/skl401/), a companion online seminar at NHH. They get you to the point of being able to open Positron, find your files, and run some code — so that the first lecture can start on Python itself.

| Video | Covers |
| --- | --- |
| [Installing Positron](https://isabelhovdahl.github.io/skl401/01-getting-started-and-working-effectively/01-03-installing-positron.html) | A tour of Positron: the editor, console, environment, and plots panes |
| [Files, folders and paths](https://isabelhovdahl.github.io/skl401/01-getting-started-and-working-effectively/01-04-files-folders-paths.html) | Absolute and relative paths, and what a working directory is |
| [Writing scripts](https://isabelhovdahl.github.io/skl401/01-getting-started-and-working-effectively/01-05-running-scripts.html) | Running code line by line and all at once, and reading error messages |
| [Reproducible reporting with Jupyter notebooks](https://isabelhovdahl.github.io/skl401/05-analysis-reporting-and-wrap-up/05-05-notebooks.html) | What a notebook is, and why we use them: code, output, and written explanation in one document |

You will already have Positron installed by this point, so watch the first video for the tour rather than the installation. Three other things to skip on that site:

> ⚠️ **Do not install Python from the SKL401 site.** Its lesson 1.2 installs Python from python.org; this course uses Miniforge instead. Everything else on the site works the same either way.

> 📝 **Note:** The paths video builds a folder called `skl401/` and works through exercises inside it. Skip the exercises — watch it for the ideas. Your folder structure for this course comes from `ban405-workspace.zip`, described in the [main README](../README.md).

> 📝 **Note:** The notebook video is taken from the end of that seminar, so the analysis it walks through uses pandas and plotting — tools you have not met yet. Watch it for what a notebook *is* and what it is good for, and don't worry about following the code. Skip the exercises and the notebook download.

## Reference

Guides you can consult at any point during the course.

| Topic | Guide |
| --- | --- |
| Creating, sharing, and managing conda environments | [Working with conda environments](conda-environments.md) |
| Using AI tools without undermining your learning | [AI guidelines for learning to code](ai-guidelines.md) |
