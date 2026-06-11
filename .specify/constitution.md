# Attendance Tracker Constitution

## Core Principles

### 1. Student Data Integrity
Student records, attendance logs, and generated reports must preserve accurate identifiers, dates, statuses, and audit metadata.

### 2. Privacy and Security
The application must avoid committing secrets, protect local data stores, and document responsible disclosure through `SECURITY.md`.

### 3. Testable Changes
Functional changes must include focused tests for attendance, reporting, authentication, or data handling behavior as appropriate.

### 4. Operational Readiness
The project must keep Docker, CI, pre-commit, dependency audit, static analysis, and coverage checks available for repeatable validation.

### 5. Spec-First Delivery
New features should begin with a concise specification, acceptance criteria, implementation plan, and task list under `.specify/` or `specs/`.

## Quality Gates

- Linting: Ruff, Flake8, and Pylint.
- Typing: Mypy.
- Dead code: Vulture.
- Security: Bandit, Semgrep, Gitleaks, and dependency audit.
- Tests: Pytest with coverage fail-under configured in `pyproject.toml`.

## Governance

This constitution applies to the Attendance Tracker repository. Updates require a documented rationale in the relevant spec or changelog entry.
