# Attendance Tracker Constitution

## Core Principles

### 1. Student Data Integrity
Student records, attendance logs, generated reports, dates, statuses, and audit metadata must remain accurate and traceable.

### 2. Privacy and Security
The project must avoid committed secrets, protect local databases and face data, and keep responsible disclosure documented.

### 3. Testable Changes
Changes to student management, attendance, reporting, authentication, or data handling must be covered by focused tests.

### 4. Operational Readiness
Docker, CI, pre-commit, dependency audit, static analysis, secret scanning, and coverage checks must remain available.

### 5. Spec-First Delivery
New features should begin with a specification, acceptance criteria, implementation plan, and task list.

## Quality Gates

- Ruff, Flake8, and Pylint for linting.
- Mypy for typing.
- Vulture for dead-code detection.
- Bandit, Semgrep, and Gitleaks for security scanning.
- pip-audit for dependency auditing.
- Pytest with coverage fail-under for tests.

## Governance

This constitution applies to the Attendance Tracker repository. Updates should be documented in the related spec or changelog.
