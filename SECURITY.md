# Security Policy

## Supported Versions

Security fixes are applied to the active development version of Attendance Tracker.

## Reporting a Vulnerability

Please do not open public issues for suspected vulnerabilities. Report security concerns privately to the project maintainer with:

- A clear description of the issue.
- Steps to reproduce.
- Affected files, routes, or workflows.
- Any suggested remediation.

The maintainer should acknowledge the report, investigate impact, and publish a fix or advisory when appropriate.

## Security Expectations

- Do not commit real credentials, tokens, database dumps, face images, or production attendance exports.
- Keep dependency audit, static analysis, and secret scanning enabled in CI.
- Use `.env.example` for documentation only; real values belong in local environment configuration.
