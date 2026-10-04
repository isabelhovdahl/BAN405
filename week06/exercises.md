# Week 06 — Workshop exercises

Last week you put your BAN405 folder on GitHub, so your work can no longer be lost. Today is about making it **run**: on any computer, and from the right place:

| Exercise | What you do | Where |
| --- | --- | --- |
| 1 | Create an environment and use it | Terminal, then Positron |
| 2 | Write an environment to a file, delete it, and rebuild it | Terminal |
| 3 | Build the course environment | Terminal, then Positron |
| 4 | Read a data file from a notebook | Positron |
| 5 | Run someone else's project | Positron, then the terminal |
| 6 | Make your own repository runnable | Positron and GitHub |

Every command below is given exactly. Copy and paste it rather than typing it, and run commands one at a time. The line above each command says which terminal it goes in: **Mac: Terminal**, **Windows: Miniforge Prompt**. Not Git Bash, and not the terminal inside Positron.

For explanations, options and what to do when something goes wrong, see the **[conda guide](../guides/conda-environments.md)**.

---

## Before you start

Open a terminal. **Mac:** open **Terminal**. **Windows:** open **Miniforge Prompt** from the Start menu. The prompt should start with `(base)`.

Check that conda works, and see which environments you already have:

```
conda --version
```
```
conda env list
```

Now check where conda gets its packages from:

```
conda config --show channels
```

You should see `conda-forge` at the top of the list. [conda-forge](https://conda-forge.org) is a large online collection of packages, maintained by a community of volunteers. Every time you create an environment or install a package today, conda downloads it from there. Open [conda-forge.org/packages](https://conda-forge.org/packages/), search for `pandas`, and look at how many versions of it exist.

> ⚠️ **Warning:** If `conda-forge` is not at the top of the list, follow [Where packages come from](../guides/conda-environments.md#where-packages-come-from-conda-forge) in the guide before you go on. If `conda` is not recognized at all, ask for help.

---

## Exercise 1 — Create an environment and use it

An **environment** is a folder with its own copy of Python and its own set of packages. Make one, and see that what is installed in it is separate from everything else on your computer.

### Part A: in the terminal

Create an environment called `practice`, with Python 3.14 and pandas. conda shows you what it is going to download, and asks you to confirm with `y`:

```
conda create --name practice python=3.14 pandas
```

Creating an environment does not start using it. Switch to it, and ask which version of pandas it has:

```
conda activate practice
```
```
conda list pandas
```

The prompt now starts with `(practice)` instead of `(base)`. Go back to `base`, and ask the same question there:

```
conda deactivate
```
```
conda list pandas
```

> **Check:** inside `practice`, `conda list pandas` shows a version number. In `base` it shows either nothing, or a different version that you installed for something else at some point. Write down the version in `practice`: you need it in Exercise 3.

### Part B: in Positron

The terminal is where environments are made. Positron is where you choose which one runs your code.

1. In Positron, open your **BAN405 folder** with **File → Open Folder**, as always.
2. Choose **File → New File…** and then **Jupyter Notebook**. Save it with `Ctrl+S` (Windows) or `Cmd+S` (Mac) in the `week06` folder, as `checks.ipynb`.
3. Click the **kernel selector** at the top right of the notebook, and pick the entry that names `practice`.
4. Paste this into the first cell and run it:

   ```python
   import sys
   print(sys.executable)

   import pandas
   print(pandas.__version__)
   ```

5. Now switch the kernel to **base**, the Python you have used so far in the course, and run the same cell again.

`sys.executable` is the path to the Python that is running your code.

> **Check:** with `practice`, the path ends in `envs`, then `practice`, then `python.exe` (Windows) or `bin/python` (Mac). An environment really is just a folder. The version is the one you wrote down. With `base`, the path has no `envs` in it, and the second line prints a different version or fails with `ModuleNotFoundError`. Same code, same computer, different result: it depends on which environment runs it.

*Guide: [Creating an environment](../guides/conda-environments.md#creating-an-environment) · [Using an environment in Positron](../guides/conda-environments.md#using-an-environment-in-positron)*

---

## Exercise 2 — Write it down, delete it, rebuild it

An environment can be written down as a small text file. That file, not the environment itself, is what you keep and share.

**1. Go to your `week06` folder in the terminal.** A terminal is always *in* a folder, and a new one starts in your home folder. Type `cd`, a space, and the path to your `week06` folder. Copy the path rather than typing it:

- **Windows:** in File Explorer, right-click the `week06` folder → **Copy as path**, and paste into Miniforge Prompt with `Ctrl+V`.
- **Mac:** type `cd ` with the space, then drag the `week06` folder from Finder onto the Terminal window.

Press Enter.

```
cd <path-to-your-week06-folder>
```

> **Check:** on Windows, the prompt now ends in `week06>`. On a Mac, the prompt shows `week06`, and `pwd` prints the whole path.

**2. Export the environment to a file.**

```
conda activate practice
```
```
conda env export --from-history > practice.yml
```

Open `week06/practice.yml` in Positron and read it. It names the environment, says where its packages come from, and lists what you asked for: Python 3.14 and pandas. The last line, `prefix`, is where the environment lives on your computer.

A project's file is usually called `environment.yml`. This one is only practice, so it gets its own name.

**3. Delete the environment.** In Positron, check that `checks.ipynb` is running on **base**, not `practice`: an environment that is in use cannot be deleted. Then, in the terminal:

```
conda deactivate
```
```
conda env remove --name practice
```
```
conda env list
```

`practice` is gone.

**4. Rebuild it, the next day.** Close the terminal window, and open a new one, as if you came back to this tomorrow. Rebuild the environment from the file:

```
conda env create --file practice.yml
```

It fails. Read the error: it names the full path where conda looked for `practice.yml`. The new terminal started in your home folder, the file is in `week06`, and conda only looked where the terminal *is*.

Go to `week06` again, the same way as in step 1, and run the same command again:

```
conda env create --file practice.yml
```
```
conda env list
```

> **Check:** `practice` is back in `conda env list`. You destroyed an environment and rebuilt it from a text file. And the one time something went wrong, the code was fine: it was run from the wrong folder. Remember that error, because you will meet it again in Exercise 4.

*Guide: [Saving an environment to a file](../guides/conda-environments.md#saving-an-environment-to-a-file) · [Creating an environment from a file](../guides/conda-environments.md#creating-an-environment-from-a-file) · [Moving to a folder](../guides/conda-environments.md#moving-to-a-folder)*

---

## Exercise 3 — Build the course environment

The rest of the course runs in an environment called `ban405`. Its file is published with the course material, and conda can build it straight from the web address, without downloading anything first. It works from any folder:

```
conda env create --file https://raw.githubusercontent.com/isabelhovdahl/BAN405/main/week06/environment.yml
```

This takes a few minutes. While it runs, read [the file itself](environment.yml). Every version is pinned exactly, and the comments say why.

When it has finished:

```
conda env list
```

Then, in Positron, switch `checks.ipynb` to the **`ban405`** kernel, and run the cell again.

> **Check:** the path ends in `envs` and `ban405`, and pandas is exactly `3.0.3`, the same on every laptop in the room. Compare it with the version you wrote down for `practice` in Exercise 1. `practice` got whatever version was newest on the day you built it; `ban405` gets the version written in its file, whenever and wherever it is built. That is what pinning buys you.

From now on, every notebook in this course runs on the `ban405` kernel.

> 💡 **Finished early?** Find pandas on [conda-forge.org/packages](https://conda-forge.org/packages/), and check which version is the newest today.

*Guide: [Creating an environment from a file](../guides/conda-environments.md#creating-an-environment-from-a-file)*

---

## Exercise 4 — Where your notebook looks for files

Exercise 2 showed that a terminal looks for files in its working directory. A notebook does exactly the same, except that nothing on the screen tells you which folder that is. This exercise is where the `../data/` in the course's notebooks comes from.

The code below uses pandas and matplotlib, which you have not met yet. That is fine: read it as a demonstration. Both are the subject of the rest of the course.

### Part A: a notebook in a week folder

Add each of these to `checks.ipynb` as a new cell, still on the `ban405` kernel, and run them one at a time.

**1. Which folder is this notebook running in?**

```python
import os
print(os.getcwd())
```

**2. Read the data file by its name.** `titanic.csv` is one of the files in your `data` folder.

```python
import pandas as pd
titanic = pd.read_csv("titanic.csv")
```

It fails with `FileNotFoundError`. The file exists, but not in the working directory.

**3. What is in the folder above?** `..` means "the folder above this one":

```python
print(os.listdir(".."))
```

There it is: `data`, next to `week06` and the other week folders. The path to the file therefore goes up one folder, and then into `data`:

```python
titanic = pd.read_csv("../data/titanic.csv")
titanic.head()
```

**4. And now that the data is in, a quick figure:**

```python
import matplotlib.pyplot as plt

titanic["Age"].plot(kind="hist", title="Age of the passengers on the Titanic")
plt.show()
```

> **Check:** `os.getcwd()` prints the path of your `week06` folder, `os.listdir("..")` includes `data`, and the histogram appears. A notebook's working directory is **the folder the notebook is saved in**. That is why every notebook in a week folder reads its data with `../data/`.

### Part B: the same line, in a different place

Not every project keeps its notebooks in subfolders. Often the notebook sits at the top of the project, with `data/` right next to it.

1. Create a new notebook as before, but save it in the **top of your BAN405 folder**, next to `data`, as `top.ipynb`. Select the `ban405` kernel.
2. Paste and run:

   ```python
   import os
   import pandas as pd

   print(os.getcwd())
   titanic = pd.read_csv("../data/titanic.csv")
   ```

3. It fails. Change the path to `"data/titanic.csv"`, and run it again.

> **Check:** the working directory is now your BAN405 folder itself, `"../data/titanic.csv"` fails, and `"data/titanic.csv"` works. The data did not move; the notebook did. **A path in a notebook is written from the folder the notebook is saved in.** If you know where the notebook is and where the data is, you can always write the path.

When you are done, delete `top.ipynb`: right-click it in Positron's Explorer → **Delete**.

> 📝 **Note:** Scripts work differently. A `.py` file run with the ▶ button runs from the folder that is open in Positron (your BAN405 folder), not from the folder the script is in. Everything in the rest of this course is a notebook, so this rarely matters here. But when a script cannot find a file that a notebook next to it finds without trouble, this is why.

---

## Exercise 5 — Run someone else's project

A colleague has turned your temperature converter into a small web app, and put it on GitHub. Can you run it?

**1. Clone it.** In Positron, open the Command Palette (`Ctrl+Shift+P` on Windows, `Cmd+Shift+P` on Mac), run **Git: Clone**, and paste:

```
https://github.com/isabelhovdahl/temperature-app.git
```

Choose your **`git-practice`** folder, next to BAN405, not inside it. When Positron asks, click **Open**.

**2. Read the README.** Open `README.md`. It says what the project is, and exactly how to run it. Look at `environment.yml` too: it lists what the app needs, and one of those packages is `dash`, which you have never installed.

**3. Try to run it in the course environment.** In the terminal, go to the `temperature-app` folder with `cd`, the same way as in Exercise 2. Then:

```
conda activate ban405
```
```
python app.py
```

It fails: `ModuleNotFoundError: No module named 'dash'`. Even the course environment cannot run this project. It needs its own.

**4. Follow the README.** Build the project's environment from its file, switch to it, and start the app:

```
conda env create --file environment.yml
```
```
conda activate temperature-app
```
```
python app.py
```

The terminal says `Dash is running on http://127.0.0.1:8050/`, and stays busy: the app is running.

**5. Use it.** Open <http://127.0.0.1:8050> in your browser. Choose **Fahrenheit to Celsius**, and enter `212`.

> **Check:** the app answers `= 100.0 °C`. You ran a project you have never seen, built with a package you have never used, without installing anything by hand: the `environment.yml` and the README were all you needed. And look at the converter: the formula is the fixed one. Whoever wrote the app found the bug before you did.

**6. Stop the app.** Click in the terminal and press `Ctrl+C`.

> 💡 **Finished early?** Open `app.py` in Positron. You will not understand all of it, and you do not need to. But find the line that imports `convert_temperature`, and the one place where the app calls it. The function is used exactly as your own program used it: it returns a number, and the app decides how to show it.

---

## Exercise 6 — Make your own repository runnable

Your BAN405 repository is on GitHub, but someone who cloned it would not know what it needs in order to run. Give it what `temperature-app` had: an environment file and instructions.

1. Open your **BAN405 folder** in Positron again: **File → Open Recent**.
2. Open [the course environment file](environment.yml) on GitHub and click **Copy raw file** at the top right.
3. In Positron's Explorer, create a new file named `environment.yml` at the **top** of your BAN405 folder, next to `README.md` (not inside `week06`). Paste, and save.
4. Open your `README.md`, and add this section at the bottom:

   ````
   ## How to run

   The notebooks run in the `ban405` conda environment. Build it once, from this folder:

   ```
   conda env create --file environment.yml
   ```

   Then open this folder in Positron, and select `ban405` as the notebook kernel.
   ````

5. In Source Control, stage `environment.yml` and `README.md`, and commit with the message `Add environment file and instructions for running`.
6. Stage what is left from today, `week06/checks.ipynb` and `week06/practice.yml`, and commit with `Add week 06 workshop files`.
7. Click **Sync Changes** to push.

> **Check:** on github.com, your repository's front page lists `environment.yml`, and the README ends with *How to run*. Anyone with access to your repository now has everything they need to run your work: the code, the data, the environment, and the instructions.

From now on, every session in this course ends the same way: **commit as you work, push when you finish.**

*Guide: [The everyday loop](../guides/git.md#the-everyday-loop)*

---

## At home

### Tidy up

Environments take up disk space. `practice` and `temperature-app` were for today only, so delete them. You still have `practice.yml`, and `temperature-app` has its own file, so you can rebuild either at any time. That is rather the point.

```
conda env remove --name practice
```
```
conda env remove --name temperature-app
```

**Keep `ban405`.** You need it for the rest of the course.

### Optional: two more ways to point at a file

In Exercise 4 you used relative paths: written from where the notebook is. There are two other ways to point at a file, and it is worth knowing why the course uses neither.

1. In `checks.ipynb`, read `titanic.csv` with its **absolute path**: the full path from the top of your disk. Copy it from the file itself and paste it between the parentheses of `pd.read_csv()`:
   - **Windows:** right-click the file in File Explorer → **Copy as path**. The path comes with quotes around it. Put an `r` in front of the first quote, `r"C:\Users\..."`, so that Python reads the backslashes as they are.
   - **Mac:** hold `Option`, right-click the file in Finder → **Copy "titanic.csv" as Pathname**, and put quotes around it.
2. Read it from a **web address**:

   ```python
   titanic = pd.read_csv("https://raw.githubusercontent.com/isabelhovdahl/BAN405/main/data/titanic.csv")
   ```

Both work, so why not use them? An absolute path works only on your own computer: it contains your user name and your folder layout, and on anyone else's computer it fails. A web address works on any computer, but only with an internet connection, and only for as long as the file stays where it is. A relative path keeps working when the whole project is copied, cloned or zipped to somewhere else, as long as the notebook and the data keep their places relative to each other.


