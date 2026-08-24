Contributing to RajClean Turbo Pro

Thank you for your interest in contributing to RajClean Turbo Pro.

RajClean is an open-source Termux-based Android storage cleaning tool. Contributions, bug reports, improvements, and suggestions are welcome.

Getting Started

Clone the repository:

git clone git@github.com:mdhhraj/rajclean-repo.git
cd rajclean-repo

Or use HTTPS:

git clone https://github.com/mdhhraj/rajclean-repo.git
cd rajclean-repo

Source Code

The main RajClean source code is located at:

source/rajclean/rajclean.py

Testing Changes

Before committing changes, test the application directly:

python source/rajclean/rajclean.py --version

Then:

python source/rajclean/rajclean.py --help

For the interactive cleaner:

python source/rajclean/rajclean.py

Package Testing

When modifying the Debian package, verify its metadata:

dpkg-deb -f pool/main/r/rajclean/rajclean_*.deb \
Package Version Architecture Maintainer Depends

Verify the package contents:

dpkg-deb -c pool/main/r/rajclean/rajclean_*.deb

Repository Changes

When changing a package version, make sure the following are updated consistently:

- Application version
- Debian package version
- APT "Packages" index
- APT "Packages.gz"
- APT "Release" metadata
- "Release.gpg" signature
- "CHANGELOG.md"

Do not manually edit generated package indexes when they can be regenerated with "dpkg-scanpackages".

Pull Requests

Before submitting a pull request:

1. Test your changes.
2. Check that the package builds successfully.
3. Verify the package metadata.
4. Verify the APT repository indexes.
5. Verify the repository signature when applicable.
6. Update "CHANGELOG.md" when appropriate.
7. Keep commits focused and descriptive.

Code Guidelines

- Keep the code simple and readable.
- Prefer Python standard-library functionality where practical.
- Avoid unnecessary dependencies.
- Do not include private keys, passwords, tokens, or personal credentials.
- Do not commit local build directories.
- Preserve compatibility with Termux.

Reporting Bugs

When reporting a bug, include:

- RajClean version
- Termux version
- Android version
- Device architecture
- Exact command used
- Error message or terminal output
- Steps to reproduce the problem

Never include private keys, passwords, authentication tokens, or other sensitive information.

License

By contributing to RajClean Turbo Pro, you agree that your contributions may be distributed under the project's MIT License.
