# Security Policy

## Supported Versions

The current `main` branch receives security fixes.

## Reporting a Vulnerability

Please report suspected vulnerabilities privately to the project maintainers.
Include a clear description, reproduction steps, affected files or endpoints,
and any relevant logs or screenshots.

Do not open a public issue for sensitive security reports. Maintainers should
acknowledge reports promptly, investigate impact, and coordinate a fix before
public disclosure.

## Local Security Notes

- Demo credentials (`admin/admin123` and `teacher/teacher123`) are provided for
  local development only. Change or remove seeded accounts before production use.
- Passwords are stored as PBKDF2-SHA256 hashes with per-password salts.
- Runtime SQLite databases, face images, and CSV exports are ignored by Git.
- Run `bandit`, `pip-audit`, `semgrep`, and `gitleaks` before releases.

