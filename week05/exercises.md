# Week 05 — Workshop exercises

Today there is no notebook. You will work through five exercises, and each one adds a single new thing you can do with git:

| Exercise | New skill | Where you work |
| --- | --- | --- |
| 1 | Read a history | On github.com |
| 2 | Clone and commit | In a copy of someone else's project |
| 3 | Start a repository | In your own BAN405 folder |
| 4 | Push | From your BAN405 folder to GitHub |
| 5 | Pull | Your BAN405 repository on two computers |

Everything happens in **Positron's Source Control panel**, the branching icon in the left sidebar. The one exception is a single setup step in Exercise 2, which is done in a terminal, and the instructions say exactly which one.

For explanations, options and what to do when something goes wrong, see the **[git guide](../guides/git.md)**. It is a reference you can come back to at any point.

> 📝 **Note:** Positron's buttons do not always use git's own words. **Sync Changes** means "pull, then push", and **Publish Branch** means "create the repository on GitHub, then push". The [quick reference](../guides/git.md#quick-reference) lists them side by side.

---

## Before you start

You need a GitHub account. If you do not have one yet, create it at [github.com](https://github.com) now, and confirm your email address. Pick a username you would be happy to show an employer.

---

## Exercise 1 — Read a history

Before you make any history of your own, look at someone else's. You need nothing but a browser.

1. Open [github.com/isabelhovdahl/temperature-converter](https://github.com/isabelhovdahl/temperature-converter). It is the temperature conversion program you have written yourself, built up in the same steps.
2. Read the README at the bottom of the page, then click `convert.py` and `temperature_tools.py` to read the code.
3. Go back to the repository's front page and click **Commits** (the clock icon above the file list). Every commit has a message, an author, a date and a short code called its **hash**.
4. Click the commit **Split into functions and handle bad input**. This is its **diff**: red lines were removed, green lines were added. Check that it matches what you remember changing when you rewrote the program with functions.

Now the actual task. Someone ran the latest version and got this:

```
212.0 degrees Fahrenheit equals 85.8 degrees Celsius.
```

212 °F is the boiling point of water, so the answer should be 100.

5. Find the commit that broke it, and the line it changed. Use the diffs, not the messages.

> 💡 **Hint:** read the diff of **Tidy up formatting** closely. Does it only tidy?

> 💡 **Finished early?** Pick another commit, and before you open it, predict from its message what its diff will show. Then check.

---

## Exercise 2 — Clone it and fix it

Now make your own copy of the project, fix the bug, and record the fix in the history.

**1. Tell git who you are.** Git writes your name and email into every commit you make, so it needs them before your first one. You do this once per computer, never again.

Open a terminal. **Mac:** open **Terminal**. **Windows:** open **Git Bash** from the Start menu. Run these three commands one at a time, using your own name and the email address you used for GitHub in the first two:

```
git config --global user.name "Your Name"
```
```
git config --global user.email "your.email@example.com"
```
```
git config --global init.defaultBranch main
```

The last one is a setting you will not notice: it makes new repositories use the same branch name as GitHub, `main`.

Check what you entered:

```
git config --global --list
```

You can close the terminal now. You will not need it again today.

**2. Make a practice folder.** In File Explorer (Windows) or Finder (Mac), create a folder called `git-practice` **next to** your BAN405 folder, not inside it. Everything you clone today goes in here.

**3. Clone the repository.**

1. In Positron, press `Ctrl+Shift+P` (Windows) or `Cmd+Shift+P` (Mac), type **Git: Clone**, and press Enter.
2. Paste `https://github.com/isabelhovdahl/temperature-converter.git` and press Enter.
3. Choose your `git-practice` folder.
4. When Positron asks whether to open the cloned repository, click **Open**.

You now have a complete copy of the project on your computer, and its whole history with it. Open the Source Control panel and look at the **Graph** section: the same six commits you saw on GitHub.

**4. Run it and see the bug.** Open `convert.py` and run it with the ▶ button at the top right of the editor. Enter `F`, then `212`.

> **Check:** the program says `85.8 degrees Celsius`, just as you found in Exercise 1.

**5. Add a file that must never be shared.** Imagine that the program will one day fetch temperatures from a weather service. Services like that give you a **key**, which works like a password, and programs usually keep it in a file called `.env`.

1. In Positron's Explorer, right-click an empty area under the files, choose **New File**, and name it exactly `.env`: with the dot at the start, and nothing after it.
2. Write this line in it, and save:

   ```
   WEATHER_API_KEY=not-a-real-key
   ```

3. Look at the Source Control panel. Under **Changes**, git lists `.env`, ready to be committed like any other file.

If this were a real key and you pushed it to GitHub, anyone could find it: automated programs scan GitHub for leaked keys within minutes of a push. You need to tell git to ignore the file.

**6. Add a `.gitignore`.** A `.gitignore` is a plain text file listing what git should never track. Every repository you ever create should have one, and you do not need to write it from scratch: the course has a template.

1. Open the [.gitignore template](../guides/gitignore-template.txt) and click the **Copy raw file** button at the top right of the file.
2. In Positron's Explorer, create a new file named exactly `.gitignore`, the same way you created `.env`.
3. Paste the template, and save.

> **Check:** `.env` has disappeared from Changes, and `.gitignore` has appeared instead. The file is still on your computer; git just no longer offers to track it.

The template covers more than secrets: for example, the cache files Python creates when a program is run from a terminal. Read its comments to see what each line is for.

*Guide: [Ignoring files](../guides/git.md#ignoring-files)*

**7. Make your first commit.** A commit takes two steps: first you **stage** the changes that belong together, then you **commit** them with a message.

1. In Source Control, hover over `.gitignore` under Changes and click the **+**. It moves to **Staged Changes**.
2. Type a message in the box at the top of the panel: `Add .gitignore`.
3. Click **✓ Commit**.

> If Positron says that it needs your `user.name` and `user.email`, step 1 did not work. Go back and run the commands again.

**8. Fix the bug.**

1. Open `temperature_tools.py` and put the parentheses back: `5 / 9 * (temperature - 32)`. Save.
2. The file appears under Changes with an **M** for modified. Click it: Positron shows the old and new versions side by side, with the change highlighted.
3. Run `temperature_tools.py` itself with the ▶ button. Its last three lines are quick checks against values we know.
4. Stage the file, write a message that says what you fixed, for example `Fix Fahrenheit to Celsius formula`, and commit.

> **Check:** `temperature_tools.py` prints `0.0`, `100.0` and `212.0`.

**9. Break something, then undo it.** This is the undo you will use most often.

1. In `convert.py`, delete the whole `get_temperature` function and save.
2. Run `convert.py`. It fails: `main` calls a function that no longer exists.
3. In Source Control, hover over `convert.py` and click the curved arrow, **Discard Changes**, then confirm.

> **Check:** `get_temperature` is back, exactly as it was at your last commit. The Graph shows eight commits: the original six, with your two on top.

> ⚠️ **Warning:** Source Control now offers to **Sync Changes**. Don't. This repository belongs to someone else, and you do not have permission to push to it. Your own commits stay on your computer, which is fine here: this copy was for practice. Next you make a repository that is yours.

> 💡 **Finished early?** Select `temperature_tools.py` in the Explorer and open the **Timeline** section at the bottom of the Explorer. It lists every commit that changed this one file. Click the entries to see how it grew, and find your own fix at the top.

*Guide: [The everyday loop](../guides/git.md#the-everyday-loop) · [Undoing things](../guides/git.md#undoing-things)*

---

## Exercise 3 — Start your own repository

Time for your own project: the BAN405 folder you have been working in all along, with `data/` and a folder for each week. (If you unzipped the workspace without renaming it, the folder is called `ban405-workspace`.)

**The rule for this course: one repository, and it is the whole BAN405 folder.** Never create a repository inside one of its week folders, and never clone anything into it. Other projects go next to it, the way `git-practice` does.

1. In Positron, choose **File → Open Folder** and open your **BAN405 folder**, the one that contains `data/`. From now on, always open this folder, never a week folder inside it.
2. In Source Control, click **Initialize Repository**. Everything in the folder appears under Changes: git sees your files but is not tracking them yet.

   > ⚠️ **Warning:** If Positron says it found a git repository in a parent folder, stop and ask for help. It means your BAN405 folder is already inside a repository, and a second one would cause trouble.

3. Create a `.gitignore` in the BAN405 folder itself, not in a week folder, the same way as in Exercise 2: new file, paste the template, save.
4. Stage everything at once with the **+** on the **Changes** heading, write the message `Start tracking my BAN405 work`, and commit.

> **Check:** Changes is empty, and the Graph shows one commit. With hidden files shown, your BAN405 folder now contains a `.git` folder: that is where the history lives.

> 💡 **Tip:** A notebook changes when you *run* it, not only when you edit it, because it stores its output. So if a notebook shows up under Changes and you did not edit anything, that is why. It is harmless: commit it along with your other work. Do not discard it. **Discard Changes** throws away everything since your last commit, including anything you typed into the notebook.

> 💡 **Finished early?** Open one of your notebooks, run it, and click it under Changes to see what running it changed.

*Guide: [Setting up a repository](../guides/git.md#setting-up-a-repository)*

---

## Exercise 4 — Put it on GitHub

So far the history lives only on your computer. Now give it a copy on GitHub.

1. In Source Control, click **Publish Branch**.
2. Positron asks to sign in to GitHub. Allow it: your browser opens, you log in and authorize, and you return to Positron. You only do this once.
3. Choose **Publish to GitHub private repository**. 
4. When it finishes, click **Open on GitHub** in the notification. Your files are there, and so is your commit.
5. Back in Positron, create a file called `README.md` directly in the BAN405 folder. Write one or two lines saying what the repository is, for example:

   ```
   # BAN405

   My work for BAN405 Python Programming for Data Science at NHH.
   ```

6. Save, stage, commit with the message `Add README`, and click **Sync Changes** to push.
7. Refresh the page on GitHub.

> **Check:** your README is displayed on the repository's front page, and the history shows two commits. From now on, the loop is: commit as you work, and push when you finish.

The repository is private: only you can see it. You can make it public later, under **Settings** on GitHub.

> 💡 **Finished early?** Make your README worth reading: add a list of the course weeks, or a sentence about what you hope to learn. GitHub formats markdown the same way notebooks do; see [GitHub's guide to formatting](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax). Commit and push, and refresh the page to see the result.

*Guide: [GitHub](../guides/git.md#github)*

---

## Exercise 5 — Work from a second computer

A repository on GitHub means you can work on it from more than one computer: a laptop on campus and a desktop at home, for example. On the second computer you would clone the repository, as you did in Exercise 2. From then on, each computer has its own complete copy, and **the copies do not update each other.** GitHub is where they meet: you push from one computer, and pull on the other.

You only have one computer here, so GitHub will stand in for the second one. Editing a file directly on github.com creates a commit on GitHub that your computer has not seen yet, which is exactly what a push from your other computer would do.

> 📝 **Note:** Editing on github.com is only a stand-in for this exercise. In your own work, make changes on your computer and push them.

1. **On "your other computer":** open your repository on github.com and click `README.md`. Click the pencil icon (**Edit this file**) and add a line at the bottom, such as `Edited on my other computer.` Click **Commit changes…**, leave **Commit directly to the `main` branch** selected, and click **Commit changes**.
2. **Back on this computer:** open `README.md` in Positron. It still has the old text. Your copy knows nothing about the new commit yet.
3. Open the **…** menu at the top of the Source Control panel and choose **Pull**.

> **Check:** the new line appears in `README.md` in Positron, and the Graph shows the commit from "your other computer". Two computers stay in step only when you push as you finish and pull as you start.

*Guide: [Working on two computers](../guides/git.md#working-on-two-computers)*

### Optional: what happens when you forget to pull

If you finish early, see what happens when both computers change the same line before they are back in step.

1. **On "your other computer":** on github.com, edit the line below the heading in `README.md` and commit, as before.
2. **On this computer, without pulling first:** change the same line in Positron to something different. Save, stage and commit.
3. Click **Sync Changes**. Git pulls first, and stops: both copies changed the same line, so it cannot combine them by itself. `README.md` is listed under **Merge Changes**. This is a **merge conflict**.
4. Resolve it by following the guide below, then stage the file, commit, and **Sync Changes** again.

*Guide: [Resolving a merge conflict](../guides/git.md#resolving-a-merge-conflict)*

---

## At home

### Put your earlier work under version control

Your BAN405 repository already contains the programs you wrote for the home exercises so far. Record them properly:

- Commit them **one exercise at a time**, each with a message saying what that program does, for example `Add temperature converter with input validation`. In Source Control, stage only the files for one exercise, commit, and repeat.
- When you are done, push, and look at the history on GitHub.

If you have already committed everything in one go, commit your next piece of work one step at a time instead. The habit matters more than the past.

### Optional: two people, one repository

In Exercise 5 you were the only person writing to your repository. Working with someone else raises a new problem, and it is worth meeting once with a classmate.

1. **One of you** creates a new repository on github.com called `conflict-practice`, ticking **Add a README file**. Under **Settings → Collaborators**, add the other person by their GitHub username.
2. **The other** accepts the invitation from the email GitHub sends.
3. You **both** clone `conflict-practice` into your `git-practice` folders.
4. Each of you edits a **different** file (for example, one edits the README and the other creates `notes.md`), and commits. Then both of you push. The first push goes through. The second is refused, because GitHub now has a commit that computer has not seen: that person pulls, git combines the two changes by itself because they are in different files, and then pushes again. Finally, the first person pulls, and both computers are in step.
5. Now both of you change **the same line** of the README without pulling first, and commit. Again the second push is refused, but this time pulling gives a **merge conflict**: git cannot decide which version of that line to keep, so it asks you.
6. Resolve it together using the guide below. Then commit and push.

*Guide: [Working with other people](../guides/git.md#working-with-other-people)*
