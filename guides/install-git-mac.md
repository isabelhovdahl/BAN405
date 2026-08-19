# Installing Git (Mac)

Git is the version control tool we'll use to track and share code throughout the course. We'll work with it through Positron's built-in Source Control panel rather than the command line, but Positron needs git itself installed to do that. Many Macs already have it, so start by checking.

## Step 1: Check if you already have it

1. Open the [Terminal](https://support.apple.com/en-gb/guide/terminal/apd5265185d-f365-44cb-8b09-71a064a42125/mac), type the following and press Enter:

   ```
   git --version
   ```

2. Two things can happen:
   - **A version number appears** (e.g. `git version 2.39.3`) — you're done, git is already installed. Skip to the [verification checklist](verify-installation.md).
   - **A popup appears** asking to install "Command Line Tools" — continue to Step 2 below.

## Step 2: Install via the popup

1. In the popup, click **Install**.
2. Agree to the license terms if prompted.
3. Wait for the download and installation to finish (this can take a few minutes).
4. Once done, go back to Terminal and run `git --version` again to confirm it now shows a version number.

## If neither of the above happened

On rare setups (e.g. school-managed laptops with restricted software installs), the popup may not appear. If so:

1. Install [Homebrew](https://brew.sh) by following the instructions on that page (copy the command shown into Terminal and press Enter).
2. Once Homebrew is installed, run:

   ```
   brew install git
   ```

3. Confirm with `git --version`.

## Next step

Continue to the [verification checklist](verify-installation.md).
