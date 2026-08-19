# Installing Positron

Positron is the code editor we'll use throughout the course. The installation is similar on Windows and Mac, but you need to pick the right installer for your machine.

Install Miniforge first ([Windows](install-miniforge-windows.md) · [Mac](install-miniforge-mac.md)) — Positron looks for a Python installation when it starts, and Miniforge is the one it should find.

> 📝 **Already have Positron?** Nothing to do — it keeps itself up to date. Continue to the Git installation guide: [Windows](install-git-windows.md) · [Mac](install-git-mac.md).

## Step 1: Download the right installer

Go to <https://positron.posit.co/download.html> and choose the download for your computer.

**Mac** — there are two builds, one per chip:

1. Click the Apple menu and select **About This Mac**.
2. Read the **Chip** line. If it says **Apple M1/M2/M3/M4**, download the **Apple Silicon** build; if it says **Intel**, download the **Intel** build.

Installing the wrong build can still appear to work, but it will run slower, so it is worth checking now.

**Windows** — there are two kinds of installer, **System** and **User**. Choose **User install**: it works the same way and does not require administrator rights. Take the `x64` version unless you know your laptop has an ARM processor.

## Step 2: Run the installer

- **Windows:** open the downloaded `.exe` file and click through the setup wizard. The default options are fine.
- **Mac:** open the downloaded `.dmg` file, then drag the Positron icon into your **Applications** folder.

## Step 3: Open it once

Start Positron (Start Menu search on Windows, Applications folder or Spotlight search on Mac) and look at two things:

- The **Console** at the bottom of the window should start a Python session.
- The **interpreter picker** in the top-right corner should name a Python that comes from `miniforge3`.

If either of those looks wrong, don't fix it now — the [verification checklist](verify-installation.md) covers it at the end.

## Next step

Continue to the Git installation guide: [Windows](install-git-windows.md) &nbsp;·&nbsp; [Mac](install-git-mac.md).
