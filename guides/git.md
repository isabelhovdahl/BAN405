# Working with git and GitHub

**git** keeps the history of a project folder: a series of snapshots, called commits, each with a message saying what changed and why. It lives on your computer. **GitHub** is a website that keeps a copy of that folder and its whole history online, so you can back it up, work on it from another computer, share it, and work on it with other people.

In this course you use git through **Positron's Source Control panel** (the branching icon in the left sidebar), and there is almost never a reason to type a git command. The terminal commands are included below anyway, so that you can recognize them when you meet them elsewhere. Almost every git tutorial online is written for the terminal.

> 📝 **Note:** Positron is built on the same foundation as VS Code, so anything written about VS Code's Source Control panel applies to Positron as well.

---

## Quick reference

| In Positron | What it does | Terminal equivalent |
| --- | --- | --- |
| **Git: Clone** (command palette) | Copy a repository and its history from GitHub | `git clone <url>` |
| **Initialize Repository** | Start tracking the open folder | `git init` |
| The list under **Changes** | Show what has changed since the last commit | `git status` |
| Click a changed file | Show what changed inside it | `git diff <file>` |
| **+** next to a file | Stage it for the next commit | `git add <file>` |
| **−** next to a staged file | Unstage it | `git restore --staged <file>` |
| Message box + **✓ Commit** | Record the staged changes | `git commit -m "<message>"` |
| Curved arrow, **Discard Changes** | Throw away changes since the last commit | `git restore <file>` |
| **Graph** section | Show the history | `git log --oneline` |
| **Publish Branch** | Create the repository on GitHub, then push | `git remote add origin <url>` and `git push -u origin main` |
| **… → Push** | Send your commits to GitHub | `git push` |
| **… → Pull** | Fetch new commits from GitHub | `git pull` |
| **Sync Changes** | Pull, then push | `git pull` and `git push` |

The **…** menu is at the top of the Source Control panel. Every command is also available by pressing `Ctrl+Shift+P` (Windows) or `Cmd+Shift+P` (Mac) and typing **Git:**.

---

## Words you will meet

| Word | Meaning |
| --- | --- |
| **Repository** (repo) | A project folder whose history git keeps. The history lives in a hidden `.git` folder inside it. |
| **Commit** | One snapshot in the history, with a message, an author and a date. Also the verb: to record one. |
| **Hash** | The code that identifies a commit, such as `4803c4f`. The full hash is 40 characters, and the first seven are usually enough. |
| **Diff** | What changed between two versions, line by line: removed lines in red, added lines in green. |
| **Stage** | Mark a change as part of the next commit. Staging lets you choose what goes into a commit, rather than committing everything at once. |
| **Working tree** | The files as they are on your disk right now, including changes you have not committed. |
| **`.gitignore`** | A text file listing what git should never track. |
| **Branch** | A line of history. Your repository has one, called `main`, which is all you need working alone. |
| **Remote** | Another copy of the repository that yours is linked to, usually on GitHub. The standard name for it is `origin`. |
| **Clone** | Make a complete local copy of a repository, including its history, linked to the original as its remote. |
| **Push** | Send your new commits to the remote. |
| **Pull** | Fetch new commits from the remote and add them to your copy. |
| **Merge conflict** | Two copies changed the same lines in different ways, so git cannot combine them without asking you which to keep. |
| **Fork** | A copy of someone else's repository in *your* GitHub account. See [Clone, fork or template](#clone-fork-or-template). |
| **Pull request** | A request, on GitHub, for the owner of a repository to accept changes you made in your fork or branch. |

---

## Setting up git

### Tell git who you are

Git records your name and email in every commit, so it needs them before your first one. You only do this **once per computer**. Run each command in a terminal: **Terminal** on Mac, **Git Bash** on Windows.

*Mac: Terminal · Windows: Git Bash*
```
git config --global user.name "<Your Name>"
```

*Mac: Terminal · Windows: Git Bash*
```
git config --global user.email "<your.email@example.com>"
```

*Mac: Terminal · Windows: Git Bash*
```
git config --global init.defaultBranch main
```

Use the email address of your GitHub account, so that GitHub can link your commits to you. The last command makes new repositories call their branch `main`, the name GitHub uses. Older versions of git say `master` instead.

Check the result with:

*Mac: Terminal · Windows: Git Bash*
```
git config --global --list
```

### Sign in to GitHub

You do not need to set anything up in advance. The first time you publish, push or pull, Positron asks to sign in to GitHub. Your browser opens, you log in and authorize Positron, and Positron remembers you from then on. You never type a GitHub password into a terminal.

---

## Setting up a repository

A repository is a folder, so starting one is a matter of choosing the right folder.

1. Open the project's **top folder** in Positron (**File → Open Folder**).
2. In Source Control, click **Initialize Repository**.
3. Before your first commit, add a `.gitignore`. See [Ignoring files](#ignoring-files).
4. Stage everything you want to keep, and make the first commit.

**One project, one repository, at the top folder.** Never create a repository inside a folder that is already part of one. A repository inside a repository confuses git, and the outer one will not track the inner one's files. If you open a folder and Positron says it found a repository in a parent folder, you are already inside one.

**Keep other repositories somewhere else.** When you clone a project, put it next to your own project folder, not inside it.

**Keep repositories out of cloud-sync folders** such as OneDrive, Dropbox or Google Drive. Those services and git both try to manage the same files, and the result can be a damaged repository. GitHub is your backup instead.

**Starting over.** Everything git knows is in the hidden `.git` folder. Deleting it removes the whole history and leaves your files exactly as they are, after which you can initialize again. To see hidden folders: in File Explorer (Windows), **View → Show → Hidden items**. In Finder (Mac), press `Cmd+Shift+.` (period).

---

## The everyday loop

1. **Work** on your files as usual, and save.
2. **Look** at the Changes list and click files to see their diffs. This is the moment to notice a change you did not mean to make.
3. **Stage** the changes that belong together, using the **+** next to each file.
4. **Commit** with a message.
5. **Push**, when you finish working.

A file is always in one of three places: **changed** (edited since the last commit, listed under Changes), **staged** (listed under Staged Changes, going into the next commit) or **committed** (safely in the history).

### Good commits

- **Commit when you have finished something**, not when you are happy with everything. "Did I just finish a step?" is the right question.
- **One commit, one change.** A fix and a new feature are two commits. Small commits are easier to understand, and easier to undo.
- **Write the message for someone reading the history later**, which is usually you. Use the imperative, and say what the commit does:

| ❌ Unhelpful | ✅ Helpful |
| --- | --- |
| `fix stuff` | `Fix crash when the input is empty` |
| `update` | `Add absolute-zero check to the converter` |
| `final` | `Split the analysis into functions` |
| `asdf` | `Load data with a relative path` |

- **Read the diff before you commit.** A message says what you meant to do. The diff says what you did.

### Notebooks

A notebook (`.ipynb`) stores its output as well as its code, so **running** a notebook changes the file even when you did not edit anything: the output, the execution counters and some settings are rewritten. Git sees that as a change. Two consequences:

- If a notebook is listed under Changes but you did not edit it, running it is the reason. Commit it, or discard the change, as you prefer.
- Notebooks are much harder to merge than scripts. See [Working with other people](#working-with-other-people).

Plots stored in a notebook's output also make the file large, and every committed version stays in the history. Clearing the output before committing (**Clear All Outputs** in the notebook toolbar) keeps the history small, at the cost of GitHub showing the notebook without its results.

---

## Ignoring files

A `.gitignore` is a plain text file, called exactly `.gitignore`, in the top folder of the repository. Every file or folder matching a line in it is invisible to git.

**Every new repository should start with the course template: [gitignore-template.txt](gitignore-template.txt).** Copy all of it into a new file called `.gitignore`, and commit it first. The template covers what almost every Python project needs:

| Pattern | What it keeps out |
| --- | --- |
| `__pycache__/`, `*.py[cod]` | Python's cache of compiled code, which Python recreates by itself when it needs it |
| `.ipynb_checkpoints/` | Jupyter's automatic backup copies of notebooks |
| `.env` | A file for passwords, API keys and tokens |
| `.venv/`, `venv/` | Virtual environments created inside a project folder |
| `.DS_Store`, `Thumbs.db` | Files the operating system creates by itself |

Then add lines for your own project below. How patterns work:

| Pattern | Matches |
| --- | --- |
| `notes.txt` | Any file called `notes.txt`, in any folder |
| `*.png` | Every file ending in `.png` |
| `output/` | A folder called `output`, and everything in it |
| `data/raw/` | Only that folder |
| `# text` | Nothing: a comment |

### What does not belong in a repository

- **Secrets.** Passwords, API keys and tokens. Once pushed, assume they are public, even from a private repository, and even if you delete them afterwards: they are still in the history.
- **Personal data** about other people, such as customer lists or survey responses with names. This is a legal question as much as a technical one.
- **Files your code produces**, such as figures, tables and exported spreadsheets. Commit the code that makes them. If the output changes, re-running the code is what should change it.
- **Large files.** GitHub refuses files over 100 MB, and warns above 50 MB.

Small, public data files that a project needs to run are fine to commit, and make the project complete.

### A file that is already tracked

`.gitignore` only affects files git is not tracking yet. If you committed a file before ignoring it, remove it from the repository (but not from your disk) with:

*Mac: Terminal · Windows: Git Bash, in the repository's folder*
```
git rm --cached <file>
```

Use `git rm -r --cached <folder>` for a folder. Then commit.

> 💡 **Tip:** GitHub offers a much longer Python `.gitignore` when you create a repository on its website. It covers tools you are unlikely to use, and it is hard to read two hundred lines and know which ones matter. The course template is short on purpose, so you understand every line.

---

## Undoing things

| Situation | In Positron | Terminal |
| --- | --- | --- |
| Throw away changes to a file since the last commit | Curved arrow, **Discard Changes** | `git restore <file>` |
| Unstage a file, keeping the changes | **−** next to the file under Staged Changes | `git restore --staged <file>` |
| See an older version of a file | **Timeline** at the bottom of the Explorer: click a commit to see its diff | `git show <hash>:<file>` |
| Bring back a file as it was in an older commit | *(terminal)* | `git restore --source=<hash> <file>` |
| Undo a whole commit, keeping the history honest | *(terminal)* | `git revert <hash>` |

`git revert` makes a **new** commit that reverses an old one, so the mistake and its correction are both in the history. That is the safe way to undo something you have already pushed.

### Looking at an old version of the whole project

*Mac: Terminal · Windows: Git Bash, in the repository's folder*
```
git checkout <hash>
```

This makes your files look exactly as they did at that commit. It is for **looking**, not working: git warns that you are in a "detached HEAD" state, which means that new commits made here do not belong to any branch. Return to the present with:

*Mac: Terminal · Windows: Git Bash, in the repository's folder*
```
git switch main
```

### Going back in time for real

> ⚠️ **Warning:** `git reset --hard <hash>` moves your branch back to an old commit and **deletes every commit after it**, along with any changes you have not committed. There is no undo. If the commits have already been pushed, it also puts your copy out of step with GitHub. Use `git revert` instead, unless you are completely sure.

---

## GitHub

### Putting a repository on GitHub

In Source Control, click **Publish Branch**, and choose a **private** or **public** repository. Positron creates the repository on GitHub and pushes your history to it. After that, **Sync Changes** or **… → Push** sends new commits.

- **Private** repositories are visible only to you, and to people you invite.
- **Public** repositories can be read by anyone. That is useful for sharing work, and for showing it to employers. You can switch between the two under **Settings** on GitHub, at the bottom of the page.

### What GitHub shows you

- A `README.md` in the top folder is displayed on the repository's front page. It is the place to say what the project is and how to run it.
- Notebooks are displayed with their output, and markdown files are formatted.
- **Commits** (the clock icon) lists the history. Click any commit to see its diff.
- The green **Code** button gives the address you need to clone the repository.

### Cloning

**Git: Clone** in the command palette asks for the repository's address and a folder to put it in, and creates a subfolder with the repository's name. You get the files and the whole history. The copy on GitHub becomes your copy's remote, called `origin`, so you can pull future changes from it. You can also push to it, if you have permission.

A private repository asks you to sign in when you clone it.

---

## Working on two computers

Every copy of a repository is complete, and they do not update each other automatically. Keeping two copies in step is two habits:

- **Pull when you start working.**
- **Push when you finish.**

If you forget to pull and commit on an out-of-date copy, pushing is refused: GitHub has commits your copy has not seen. Pull first, then push. As long as the two copies changed *different* files, or different parts of the same file, git combines them automatically. If both changed the *same lines*, you get a merge conflict (see below).

Most conflicts on two computers come from forgetting to push before switching. So push at the end of every session, even if the work is unfinished.

Anything that adds a commit on GitHub counts as a second copy, including editing a file directly on github.com. It is best avoided in your own work, but if you do it, pull before you carry on locally.

---

## Working with other people

To give someone permission to push to your repository, open it on GitHub, choose **Settings → Collaborators → Add people**, and enter their username. They accept the invitation from an email.

With more than one person, conflicts become a normal part of the work. Four habits keep them rare:

1. **Pull when you start, push when you finish**, as with two computers.
2. **Commit small and often.** A conflict in a small commit is small.
3. **Divide the work by file.** Two people editing different files never conflict.
4. **One person per notebook, always.** See below.

### Resolving a merge conflict

When a pull hits a conflict, the file is listed under **Merge Changes** in Source Control, and the conflicting part of the file is marked like this:

```
<<<<<<< HEAD
the line as you changed it
=======
the line as the other person changed it
>>>>>>> 7bdf5419cd1ba1c0c37f2ecf3be5d7952613e72b
```

The long code on the last line is the hash of the commit you pulled.

To resolve it:

1. Open the file. Above each conflict, Positron offers **Accept Current Change** (yours), **Accept Incoming Change** (theirs) and **Accept Both Changes**. Choose one, or edit the text by hand until it is right. Make sure no `<<<<<<<`, `=======` or `>>>>>>>` lines remain.
2. Save, and stage the file with **+**. Staging tells git the conflict is resolved.
3. Commit, and push.

If you would rather stop and think, the merge can be cancelled, which puts everything back as it was before the pull:

*Mac: Terminal · Windows: Git Bash, in the repository's folder*
```
git merge --abort
```

### Conflicts in notebooks

A notebook is stored as a structured text format (JSON), with the code, the output and a lot of bookkeeping mixed together. Conflict markers inside it break that structure, and the notebook will not open until it is repaired. Two people who only *ran* the same notebook can conflict, because the execution counters differ.

Do not try to merge a notebook line by line. **Keep one whole version**, and redo the other person's change by hand:

*Mac: Terminal · Windows: Git Bash, in the repository's folder*
```
git checkout --theirs <notebook>.ipynb
```

`--theirs` keeps the version you pulled, and `--ours` keeps your own. Then stage, commit and push.

> 💡 **Tip:** The more of your code lives in `.py` files that the notebook imports, the less there is to lose in a notebook conflict. Put the functions in a script and let the notebook tell the story.

---

## Clone, fork or template

Three ways to get your own copy of a repository. They are easy to mix up.

| | What it is | Where the copy lives | Can you push to it? | Link to the original |
| --- | --- | --- | --- | --- |
| **Clone** | A git operation | On your computer | Only if you have permission to push to the original | The original is your remote |
| **Fork** | A GitHub operation (**Fork** button) | In your GitHub account | Yes, to your fork | Kept: GitHub knows where your fork came from |
| **Template** | A GitHub operation (**Use this template**) | In your GitHub account | Yes | None: a new repository with the same files and no history |

- **Clone** a repository to work with it on your computer. If it is not yours, you can commit locally but not push.
- **Fork** a repository to change someone else's project, perhaps to propose the change back to them. The usual workflow is to fork on GitHub, then clone *your fork*. To offer your change to the original project, open a **pull request** from your fork on GitHub, and the owner decides whether to accept it. This is how most open-source software is developed.
- **Use a template** to start a new project of your own from someone else's starting point, with no connection to where it came from.

---

## Troubleshooting

### "Make sure you configure your user.name and user.email"

Git does not know who you are yet. Run the commands in [Tell git who you are](#tell-git-who-you-are).

### Push is rejected: "Updates were rejected because the remote contains work that you do not have"

Someone, or you on another computer, pushed commits that your copy has not seen. **Pull**, then push again.

### Pull fails: "Need to specify how to reconcile divergent branches"

GitHub and your computer both have commits the other has not seen, and git has not been told how to combine them. Positron's **Pull** and **Sync Changes** handle this for you; the message usually comes from typing `git pull` in a terminal. Run this once, then pull again:

*Mac: Terminal · Windows: Git Bash*
```
git config --global pull.rebase false
```

### "Permission denied" or error 403 when pushing

You do not have permission to push to that repository. It is someone else's. Fork it if you want your own copy on GitHub. If it is yours, you may be signed in to Positron with a different GitHub account: check the **Accounts** icon at the bottom of the left sidebar.

### The sign-in window does not appear

Look for it behind other windows, or in your browser. If there is nothing there, sign in first through the **Accounts** icon at the bottom of Positron's left sidebar, then try again.

### Mac: "The git command requires the command line developer tools"

The first time anything uses git on a Mac, macOS offers to install Apple's developer tools. Click **Install**, wait for it to finish, and try again.

### `.gitignore` does not seem to work

Check three things:

- **The name.** It must be exactly `.gitignore`. On Windows, Notepad sometimes saves it as `.gitignore.txt`. Creating the file in Positron avoids this.
- **The place.** It must be in the top folder of the repository.
- **Whether the file was already tracked.** `.gitignore` only affects files git is not tracking yet. See [A file that is already tracked](#a-file-that-is-already-tracked).

### Positron says it found a repository in a parent folder

You opened a folder inside an existing repository. Usually that means you should open the top folder instead. If you did not expect a repository there at all, someone initialized one too high up, perhaps in your whole Documents folder. Ask for help before deleting anything.

### Everything is in a state you cannot fix

If your work is pushed to GitHub, the simplest fix is often a fresh start. Rename the broken folder, clone the repository again, and copy across any files you changed since your last push.

---

## Learning more

- [Pro Git](https://git-scm.com/book/en/v2): the standard book on git, free online. Chapters 1–3 cover everything above, and more.
- [GitHub Docs: Get started](https://docs.github.com/en/get-started): accounts, repositories, forks and pull requests, from GitHub itself.
- [Source Control in VS Code](https://code.visualstudio.com/docs/sourcecontrol/overview): the panel Positron shares with VS Code, in detail.
- [GitHub Skills](https://skills.github.com/): short interactive courses that run inside real repositories.
