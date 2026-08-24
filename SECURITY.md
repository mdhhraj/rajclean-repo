Security Policy

Supported Versions

Security fixes are currently provided for the latest stable release of RajClean Turbo Pro.

Version| Supported
8.2| Yes
8.1| No

Reporting a Security Vulnerability

If you discover a security vulnerability in RajClean Turbo Pro or its repository infrastructure, please report it privately before creating a public issue.

Please include

- RajClean version
- Termux version
- Android version
- Device architecture
- A clear description of the vulnerability
- Steps to reproduce the issue
- Relevant terminal output or logs
- Potential security impact

Do not include passwords, private keys, authentication tokens, personal data, or other sensitive information in your report.

Repository Security

RajClean packages are distributed through the project's APT repository.

Repository metadata is cryptographically signed using GPG.

Users should verify that the repository signing key matches the officially published RajClean repository key before trusting packages.

Never commit the following to this repository:

- GPG private keys
- Passwords
- API keys
- Access tokens
- SSH private keys
- Personal credentials

Responsible Disclosure

Please allow reasonable time for a security issue to be investigated and fixed before publicly disclosing the vulnerability.

Security reports will be reviewed and addressed as appropriate.

Scope

This policy covers:

- RajClean application code
- RajClean Debian packages
- APT repository metadata
- Repository signing configuration
- Installation and update mechanisms

Issues caused solely by third-party software, Termux itself, Android, or unrelated external services may be outside the project's direct control.
