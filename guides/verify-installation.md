# Verification checklist

Once you've installed Miniforge, Positron, and Git, go through this checklist to confirm everything is working. This should take about two minutes.

| # | Check | How | Looks right if... |
| --- | --- | --- | --- |
| 1 | Miniforge | **Windows:** open Miniforge Prompt. **Mac:** open Terminal. Run `conda info --base` | A path appears that contains `miniforge3`, e.g. `C:\Users\you\miniforge3` or `/Users/you/miniforge3` |
| 2 | Positron opens | Open Positron from the Start Menu (Windows) or Applications folder (Mac) | The window opens |
| 3 | Positron found Python | Look at the interpreter picker in the top-right corner | It names a Python that comes from `miniforge3` |
| 4 | Positron runs code | Click in the **Console** at the bottom, type `2 + 2` and press Enter | `4` appears below |
| 5 | Git | **Windows:** open Git Bash. **Mac:** open Terminal. Run `git --version` | A version number appears, e.g. `git version 2.43.0` |

## If everything shows correctly

You're all set for the first lecture — no further action needed.

## If check 1 shows a different path

Another Python installation is answering instead of Miniforge. On Windows, check that you opened the **Miniforge Prompt** and not another terminal. If it still looks wrong, note what it said and bring it to the first lecture.

## If check 3 names a different Python

Click the interpreter picker, choose **New Console Session…**, and pick the Python listed under Miniforge. If there is no Miniforge entry at all, open the Command Palette (`Ctrl + Shift + P` on Windows, `Cmd + Shift + P` on Mac), run **Interpreter: Discover All Interpreters**, and look again.

## If check 4 fails with a message about `ipykernel`

Positron normally brings everything it needs to run Python, but the automatic setup occasionally fails. Open the Miniforge Prompt (Windows) or Terminal (Mac) and run:

```
conda install ipykernel
```

Then close Positron and open it again.

