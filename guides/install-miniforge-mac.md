# Installing Miniforge (Mac)

Miniforge gives us Python — the programming language we'll be coding in — along with `conda`, a tool for managing project environments.

Even if you already have Python installed in some other way, please install Miniforge — the rest of the course assumes it.

> 📝 **Already have Miniforge?** You don't need to reinstall it. Open Terminal, run `conda update -n base -c conda-forge conda`, then continue to the [Positron installation guide](install-positron.md).

## Step 1: Check your Mac's chip

Miniforge has two different versions for Mac depending on the chip inside your computer, so you'll need to check which one you have.

1. Go to Apple's guide: [Get system information about your Mac](https://support.apple.com/guide/mac-help/get-system-information-about-your-mac-syspr35536/mac)
2. Follow the steps there to find your **Chip** (Apple menu → About This Mac).
3. Note whether it says **Apple M1/M2/M3/M4** (Apple Silicon) or **Intel**.

## Step 2: Download Miniforge

Go to https://conda-forge.org/download/ and download the installer matching your chip from Step 1:

- **Apple Silicon (M1/M2/M3/M4):** [Miniforge3-MacOSX-arm64.sh](https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-MacOSX-arm64.sh)
- **Intel:** [Miniforge3-MacOSX-x86_64.sh](https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-MacOSX-x86_64.sh)

Miniforge on Mac doesn't have a click-through installer — it installs via a short Terminal command. Follow the steps below exactly.

## Step 3: Run the installer in Terminal

1. Open the **Terminal**: press `Cmd + Space`, type "Terminal," and press Enter.
2. Move into your Downloads folder by typing:

   ```
   cd ~/Downloads
   ```

3. Run the installer (use the filename matching what you downloaded — Apple Silicon shown here):

   ```
   bash Miniforge3-MacOSX-arm64.sh
   ```

   (Intel users: replace `arm64` with `x86_64` in the command above.)

4. You'll be shown a license agreement. Press `Enter` or `Space` to scroll through it, then type `yes` and press Enter to accept.
5. When asked where to install, press Enter to accept the default location.
6. When asked **"Do you wish to update your shell profile to automatically initialize conda?"**, type `yes` and press Enter.
7. Close the Terminal window and open a new one.

## Next step

Continue to the [Positron installation guide](install-positron.md).
