Support

Welcome to RajClean Turbo Pro support.

Before requesting help, please make sure you are using the latest version of RajClean.

Check Your Version

Run:

rajclean --version

You can also check the installed package:

dpkg -s rajclean | grep -E '^(Package|Version|Architecture):'

Installation Problems

If RajClean cannot be installed, first refresh the Termux package lists:

pkg clean
pkg update

Then try:

pkg install rajclean

Check package availability:

apt policy rajclean

Command Problems

If the "rajclean" command is not found:

command -v rajclean

Then verify the package:

dpkg -s rajclean

If necessary, reinstall it:

pkg reinstall rajclean

Before Reporting a Bug

Please provide:

- RajClean version
- Android version
- Termux version
- Device architecture
- The command you used
- The complete error message
- Steps required to reproduce the problem

Do not include passwords, private keys, API keys, authentication tokens, or other sensitive information.

Feature Requests

Feature requests should clearly explain:

- What feature you want
- Why it would be useful
- How you expect it to work
- Any relevant technical limitations

Security Issues

Do not report security vulnerabilities through normal public issues.

Follow the instructions in "SECURITY.md" for security-related reports.

Repository

Official repository:

https://github.com/mdhhraj/rajclean-repo

Community Contributions

Bug reports, documentation improvements, testing, and code contributions are welcome.

Please read "CONTRIBUTING.md" before submitting a contribution.

Important

RajClean performs file scanning and cleaning operations.

Always review detected files before deleting anything important. Android storage permissions and filesystem behavior may vary between devices and Android versions.

The project is provided under the MIT License.
