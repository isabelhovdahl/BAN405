# Installing Git (Windows)

Git is the version control tool we'll use to track and share code throughout the course. We'll work with it through Positron's built-in Source Control panel rather than the command line, but Positron needs git itself installed to do that.

> 📝 **Already have Git?** Run the installer anyway — it upgrades your existing installation rather than adding a second one.

## Steps

1. Go to [https://git-scm.com/download/win](https://git-scm.com/download/win)
2. Click the link to download the most recent version of Git for Windows.
3. Open the downloaded installer and click Next through the setup wizard. The default options are fine, with one exception — see the next step.
4. Stop at the screen titled **"Choosing the default editor used by Git"**. Open the dropdown and select **"Use Notepad as Git's default editor"**, then carry on clicking Next.
5. Finish the installation.

Why bother: git occasionally opens a text editor by itself, and the installer's default choice is **Vim**, which is hard to use and famously hard even to exit if you have never seen it before. Notepad is a poor editor, but it opens and closes the way you expect. Positron is not offered in this dropdown, so it is not an option here.

The installer also adds **Git Bash**, a terminal available from the Start menu. We won't need it, but it is there if you ever want to use git from the command line.

## Next step

Continue to the [verification checklist](verify-installation.md).
