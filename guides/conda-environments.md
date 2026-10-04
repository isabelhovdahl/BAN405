# Working with Conda Environments

A **virtual environment** is an isolated folder containing its own copy of Python and its own set of packages. Each project gets its own environment, so the packages one project needs can never interfere with another project's.

> ⚠️ **Never install packages into the `base` environment.** `base` is the environment conda creates for itself when you install Miniforge. Keep it clean and create a new environment for each project instead.

## Quick reference

| Task | Command |
| --- | --- |
| Check conda is working | `conda --version` |
| List all your environments | `conda env list` |
| Create an environment | `conda create --name my_env python=3.14` |
| Activate an environment | `conda activate my_env` |
| Deactivate (return to `base`) | `conda deactivate` |
| Install a package (into the active environment) | `conda install numpy` |
| List packages in the active environment | `conda list` |
| Check whether one package is installed | `conda list numpy` |
| Save an environment to a file | `conda env export --from-history > environment.yml` |
| Create an environment from a file | `conda env create --file environment.yml` |
| Delete an environment | `conda env remove --name my_env` |
| Check where packages come from | `conda config --show channels` |

## Opening a terminal

All conda commands are typed into a terminal:

- **Windows:** open **Miniforge Prompt** from the Start Menu.
- **Mac:** open **Terminal** from the Applications folder (or via Spotlight search).

Use these, not Positron's built-in terminal: which shell it opens, and whether conda works there, depends on your settings.

You'll know conda is available if the prompt starts with `(base)`. To confirm, run:

```
conda --version
```

### Moving to a folder

A terminal is always *in* a folder, called its **working directory**. A new terminal starts in your home folder. Commands that read or write a file, such as creating an environment from `environment.yml`, look for it there unless you say otherwise.

**Where am I?** On Windows, the prompt shows the whole path: `(base) C:\Users\you\BAN405>`. On a Mac, the prompt shows only the folder's name; `pwd` prints the whole path.

**Moving somewhere else:** type `cd`, a space, and the folder's path, then press Enter. The easiest way to get the path right is to copy it rather than type it:

- **Windows:** in File Explorer, right-click the folder → **Copy as path**, and paste into Miniforge Prompt with right-click or `Ctrl+V`.
- **Mac:** type `cd ` with the space, then drag the folder from Finder onto the Terminal window, and press Enter.

```
cd <path-to-folder>
```

> 💡 **Tip:** `cd ..` moves one folder up. On Windows, a folder on another drive needs `/d`: `cd /d D:\path\to\folder`.

## Where packages come from: conda-forge

Every `conda create` and `conda install` downloads its packages from a **channel**: an online collection of packages. The one this course uses is [conda-forge](https://conda-forge.org), a large collection maintained by a community of volunteers. You can search it at [conda-forge.org/packages](https://conda-forge.org/packages/) and see every version of every package it has.

Check which channels your conda uses:

```
conda config --show channels
```

Miniforge is set up with `conda-forge` and nothing else, which is what you want. If you see something else, for example `defaults`, your conda probably comes from an older Anaconda or Miniconda installation. That is fine, as long as `conda-forge` is at the top of the list. If it isn't, add it:

```
conda config --add channels conda-forge
```

and run `conda config --show channels` again: `conda-forge` is now first.

> 📝 **Note:** An `environment.yml` file names its own channels. The course's files list `conda-forge` and `nodefaults`, which means "conda-forge, and nothing else", so they install the same packages whichever conda you have.

## Creating an environment

```
conda create --name my_env python=3.14 numpy
```

This creates an environment called `my_env` containing Python 3.14 and numpy. Breaking down the command:

- `--name my_env` — the name of the environment. Use something descriptive; the project name is usually a good choice.
- `python=3.14` — the Python version. Always include this, otherwise conda decides for you.
- `numpy` — any packages you want installed right away. You can list several, separated by spaces, or none at all.

Conda will show you what it plans to install and ask you to confirm with `y`.

> 📝 **Note:** You can pin a specific version of any package with `=`, e.g. `numpy=2.1`. Pinning matters when a project needs an exact version; otherwise conda installs the newest version that works.

Environments are stored centrally (inside your Miniforge folder), not in your project folder — so it doesn't matter which folder you are in when you create one.

## Activating and deactivating

Creating an environment does not start using it. To activate it:

```
conda activate my_env
```

Your prompt changes from `(base)` to `(my_env)`, telling you which environment is currently active. Any package you install now goes into `my_env`.

To leave the environment and return to `base`:

```
conda deactivate
```

## Installing packages

With the environment activated:

```
conda install pandas matplotlib
```

To check what's installed in the active environment:

```
conda list
```

Or check a single package (the output is empty if it isn't installed):

```
conda list pandas
```

## Using an environment in Positron

Creating an environment in the terminal is only half the job — you also need to tell Positron to use it. Positron finds conda environments on its own, so this is a matter of picking the right one.

**For Python scripts (`.py`):**

1. Open your project folder in Positron (**File → Open Folder**).
2. Click the **interpreter picker** in the top-right corner.
3. Choose **New Console Session...**, then pick your environment from the list.

The picker always shows which environment the console is currently running. The ▶ button at the top of a script runs it in this console, with this environment.

**For notebooks (`.ipynb`):**

1. Open the notebook.
2. Click the **kernel selector** in the notebook's toolbar.
3. Pick your environment.

The notebook and the console are two separate choices. A notebook can run in one environment while the console runs in another.

To check from inside Python which environment is running, print `sys.executable`. It is the path to the Python that is running your code, and an environment's path ends in `envs` followed by its name:

```python
import sys
print(sys.executable)
```

> 💡 **Tip:** A newly created environment usually appears straight away. If it doesn't, open the Command Palette (`Ctrl+Shift+P` on Windows, `Cmd+Shift+P` on Mac) and run **Interpreter: Discover All Interpreters**.

Positron brings its own Jupyter kernel, so you don't normally need to install `ipykernel` into an environment yourself. If a notebook refuses to start and names `ipykernel`, activate the environment and run `conda install ipykernel`.

## Saving an environment to a file

To let someone else (or your future self) recreate an environment exactly, export it to an `environment.yml` file.

1. Activate the environment you want to export:

   ```
   conda activate my_env
   ```

2. Navigate to the folder where you want to save the file:

   ```
   cd <path-to-your-project-folder>
   ```

3. Export it:

   ```
   conda env export --from-history > environment.yml
   ```

The resulting file lists the environment's name, its channels, and the packages you asked for. It's a small text file — open it in Positron and read it. The last line, `prefix`, is where the environment lives on your computer; you can delete it before sharing the file.

> 💡 **Tip:** Use `--from-history`. Without it, conda exports *every* package in the environment, including ones that were installed automatically as dependencies, pinned to versions that may only exist on your operating system. That makes the file long and often unusable on a different computer.

> ⚠️ **Warning:** `--from-history` only records packages installed with `conda`. If you installed anything with `pip` (see below), you'll need to add it to the file by hand.

## Creating an environment from a file

Given an `environment.yml` file, anyone can rebuild the same environment:

1. Navigate to the folder containing the file:

   ```
   cd <path-to-folder>
   ```

2. Create the environment:

   ```
   conda env create --file environment.yml
   ```

The environment's name comes from inside the file, so you don't specify it. Check that it worked with `conda env list`, then activate it as usual.

You can also create an environment directly from a file published online, without downloading it first:

```
conda env create --file https://example.com/path/to/environment.yml
```

## Deleting an environment

Environments take up disk space, so it's worth removing ones you no longer use. You can't delete an environment while it's in use, so deactivate it first, and make sure no notebook or console in Positron is running it:

```
conda deactivate
conda env remove --name my_env
```

Confirm it's gone with `conda env list`.

## conda vs. pip

`conda` is not the only way to install Python packages — Python's own package installer, `pip`, is also available inside every conda environment:

```
pip install some-package
```

Both work, but they aren't interchangeable:

- **Prefer `conda`.** It checks that all your packages are compatible with each other before installing anything, which prevents a lot of broken environments.
- **Use `pip` when conda can't help.** Some packages aren't distributed through conda channels at all, and brand-new releases usually appear on PyPI (pip's repository) before conda-forge.
- **Install conda packages first, then pip packages.** Installing with conda after pip can overwrite what pip did.

## Troubleshooting

**`conda: command not found` or `'conda' is not recognized`**
On Windows, conda is only set up in the **Miniforge Prompt** by default — use that rather than Command Prompt, PowerShell, or Positron's built-in terminal.

On Mac, run `~/miniforge3/bin/conda init zsh`, then close Terminal and open it again.

**`EnvironmentFileNotFound: '…/environment.yml' file not found`**
conda looked for the file in the terminal's working directory, and it isn't there. The error shows the full path it tried. Move to the folder that contains the file with `cd` (see [Moving to a folder](#moving-to-a-folder)), and run the command again.

**Deleting an environment fails, or says a file is in use**
Something is still running in that environment, usually a notebook or console in Positron. Switch the notebook to another kernel, or close Positron, then try again.

**Conda takes a very long time, or fails with a message about conflicts**
Conda is trying to find a combination of package versions that work together, and there may not be one. Try pinning fewer versions — for example, ask for `numpy` rather than `numpy=1.21`.

**`PackagesNotFoundError`**
The package isn't available on conda-forge under that name. Check the spelling, then try installing it with `pip` instead.

**A package is installed, but Python says `ModuleNotFoundError`**
The package is probably installed in a different environment than the one that's running your code. Check which environment is active in your terminal (the `(name)` prefix). In Positron, check the notebook's kernel selector, or the interpreter picker in the top-right corner for the console and for scripts: they are separate choices. `print(sys.executable)` settles it.

**I don't know which environment I'm in**
Run `conda env list` — the active one is marked with an asterisk `*`.

## Best practices

- **One environment per project.** Keeps dependencies isolated and makes each project reproducible.
- **Never install into `base`.** Keep your base installation clean.
- **Use descriptive names**, usually matching the project name.
- **Pin versions for packages that matter** to the project, so it keeps working later.
- **Export an `environment.yml`** and keep it alongside your project code, so others can rebuild it.
- **Delete environments you no longer use.**
