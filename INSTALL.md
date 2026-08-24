RajClean Turbo Pro Installation

RajClean Turbo Pro is distributed through the official RajClean APT repository for Termux.

Requirements

- Android device
- Termux
- Internet connection
- "aarch64" Android devices are supported by the current repository

Install

Open Termux and run:

pkg update
pkg install rajclean

Then verify the installation:

rajclean --version

You should see:

RajClean Turbo Pro 8.2

Run RajClean

Start the interactive cleaner with:

rajclean

Show Help

To view available command-line options:

rajclean --help

Or:

rajclean -h

Show Version

Use:

rajclean --version

Or:

rajclean -v

Update RajClean

If a newer version is published:

pkg update
pkg upgrade rajclean

You can check the installed version with:

dpkg -s rajclean | grep -E '^(Package|Version|Architecture):'

Uninstall

To remove RajClean:

pkg uninstall rajclean

Repository

RajClean packages are distributed through the official RajClean APT repository:

https://github.com/mdhhraj/rajclean-repo

Repository metadata is GPG signed.

Users should not disable APT signature verification or use an unsigned repository to install RajClean.

Troubleshooting

If Termux cannot find the package, refresh the package lists:

pkg clean
pkg update

Then try:

pkg install rajclean

Check whether APT can see the package:

apt policy rajclean

A correctly configured repository should show an available RajClean version under the repository's package index.

Verify Installation

Run:

command -v rajclean

Then:

rajclean --version

Finally:

rajclean --help

If all three commands work, RajClean is installed correctly.
