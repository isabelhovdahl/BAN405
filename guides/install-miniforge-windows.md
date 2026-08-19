# Installing Miniforge (Windows)

Miniforge gives us Python — the programming language we'll be coding in — along with `conda`, a tool for managing project environments.

Even if you already have Python installed in some other way, please install Miniforge — the rest of the course assumes it.

> 📝 **Already have Miniforge?** You don't need to reinstall it. Open the **Miniforge Prompt** from the Start Menu, run `conda update -n base -c conda-forge conda`, then continue to the [Positron installation guide](install-positron.md).

## Step 1: Download Miniforge

Download the installer from here: https://conda-forge.org/download/. Click on the button for Windows. 

## Step 2: Run the installer

Open the downloaded `.exe` file and go through the setup wizard. When you reach the installation options screen, use these settings:

| Option | Setting |
| --- | --- |
| Create shortcuts | ✅ Ticked (default) |
| Add Miniforge3 to my PATH environment variable | ❌ **Leave unticked** (the installer itself recommends this) |
| Register Miniforge3 as my default Python | ✅ Tick this |
| Clear the package cache upon completion | ✅ Tick this |

Click Install and wait for it to finish.

## Next step

Continue to the [Positron installation guide](install-positron.md).
