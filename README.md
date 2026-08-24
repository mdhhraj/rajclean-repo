🅁🄰🄹🄲🄻🄴🄰🄽 🅃🅄🅁🄱🄾 🄿🅁🄾

RajClean Turbo Pro is a lightweight command-line cleaner for Termux on Android.

It scans Android storage for duplicate, temporary, cache-related and potentially unnecessary files, then provides a preview before cleaning.

Current Version: 8.2
Developer: Hasibul Hasan Rajib
Package: "rajclean"

✨ Features

- 🧹 Internal storage scanning
- 💾 External/SD-card scanning
- 🔍 Duplicate file detection using file size and MD5 hashing
- 🗑️ Junk and temporary file detection
- 👀 Preview detected files before cleaning
- ⚡ Parallel file hashing for faster duplicate detection
- 🖥️ Simple Termux-based interface
- 🔐 GPG-signed APT repository
- 📦 Install and update through "pkg"

📦 Installation

1. Install required packages

pkg update
pkg install curl gnupg python

2. Download the RajClean repository public key

Download the repository public key from the GitHub repository and save it as:

$HOME/rajclean-repo-public.asc

Then create the APT keyring:

mkdir -p "$PREFIX/etc/apt/keyrings"

gpg --dearmor \
  -o "$PREFIX/etc/apt/keyrings/rajclean.gpg" \
  "$HOME/rajclean-repo-public.asc"

chmod 644 "$PREFIX/etc/apt/keyrings/rajclean.gpg"

3. Add the RajClean repository

echo "deb [signed-by=$PREFIX/etc/apt/keyrings/rajclean.gpg] https://raw.githubusercontent.com/mdhhraj/rajclean-repo/main stable main" \
  > "$PREFIX/etc/apt/sources.list.d/rajclean.list"

4. Update package lists

pkg update

5. Install RajClean

pkg install rajclean

Verify:

rajclean --version

Expected:

RajClean Turbo Pro 8.2

🚀 Usage

Start RajClean:

rajclean

Main menu:

1 Internal Scan
2 External Scan
3 Both Scan
4 Exit

Help

rajclean --help

Version

rajclean --version

or:

rajclean -v

🔐 Storage Permission

Before scanning Android shared storage, grant Termux storage permission:

termux-setup-storage

Allow the permission when Android asks.

Verify:

ls ~/storage

🧹 Cleaning Workflow

RajClean follows this workflow:

Select Scan
Scan Files
Find Duplicates
Find Junk
Preview Results
Clean Now / Go Back

When cleaning is selected, detected files are moved into:

/storage/emulated/0/.rajclean_trash

⚠️ Important Notes

External Storage

The current RajClean configuration contains:

/storage/5F34-6C6B

Android may assign a different mount path to an SD card on another device.

If External Scan does not detect an SD card, the configured external-storage path in "rajclean.py" must be changed.

Review Before Cleaning

Always review detected files before selecting:

2 Clean now

No automated cleaner can perfectly determine whether every file is safe to remove. Human beings have created both cache directories and files named "final_final_REAL_final2.pdf", so a preview is still a useful invention.

Root Access

RajClean does not require root access for normal operation.

Android may prevent Termux from accessing certain protected application directories.

🔄 Update

After a new version is published:

pkg update
pkg install rajclean

Check the installed version:

rajclean --version

🗑️ Uninstall

Remove RajClean:

pkg uninstall rajclean

Remove the repository configuration:

rm -f "$PREFIX/etc/apt/sources.list.d/rajclean.list"
rm -f "$PREFIX/etc/apt/keyrings/rajclean.gpg"

Then update package lists:

pkg update

🛠️ Repository

Official repository:

https://github.com/mdhhraj/rajclean-repo

Repository structure:

rajclean-repo/
├── dists/
│   └── stable/
│       ├── Release
│       ├── Release.gpg
│       └── main/
│           ├── binary-all/
│           │   ├── Packages
│           │   └── Packages.gz
│           └── binary-aarch64/
│               ├── Packages
│               └── Packages.gz
├── pool/
│   └── main/
│       └── r/
│           └── rajclean/
│               └── rajclean_8.2_all.deb
└── source/
    └── rajclean/
        └── rajclean.py

📋 Package Information

Package:      rajclean
Version:      8.2
Architecture: all
Maintainer:   Hasibul Hasan Rajib
Depends:      python
Section:      utils

💻 Development

Clone the repository:

git clone https://github.com/mdhhraj/rajclean-repo.git
cd rajclean-repo

Main source:

source/rajclean/rajclean.py

Package:

pool/main/r/rajclean/rajclean_8.2_all.deb

❤️ Developer

Hasibul Hasan Rajib

GitHub:

https://github.com/mdhhraj

Repository:

https://github.com/mdhhraj/rajclean-repo

⭐ Support

If RajClean is useful:

- ⭐ Star the repository
- 🐛 Report bugs
- 💡 Suggest improvements
- 🔧 Contribute code
- 📢 Share the project

📜 Disclaimer

RajClean is provided as an open-source utility.

Always review files before cleaning or moving them. Keep backups of important files.

The developer is not responsible for data loss caused by misuse, incorrect storage configuration, or manually modified source code.

🚀 Quick Start

For users who have already configured the RajClean repository:

pkg update
pkg install rajclean
rajclean

Check the installed version:

rajclean --version

RajClean Turbo Pro 8.2
