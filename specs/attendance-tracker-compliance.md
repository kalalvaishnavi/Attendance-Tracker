# Attendance Tracker Compliance Spec

## Summary

Provide repository files and automation needed for a 100% project compliance scan.

## Requirements

- REQ-001: The repository must include project governance, security, changelog, Docker, and environment example files.
- REQ-002: The repository must configure Ruff, Mypy, Vulture, Bandit, Pylint, Flake8, Semgrep, and Pyupgrade.
- REQ-003: The repository must include secret scanning, dependency audit, static analysis, test, coverage, and fail-under checks.
- REQ-004: The GitLab pipeline must expose explicit `format`, `lint`, `type_check`, `test`, `coverage`, `security`, and `changelog` stages.
- REQ-005: The repository must include Spec Kit directories, templates, and constitution files.

## Acceptance Criteria

- AC-001: Compliance checks can detect `.editorconfig`, `CHANGELOG.md`, `SECURITY.md`, `CODE_OF_CONDUCT.md`, `.env.example`, `Dockerfile`, and `.dockerignore`.
- AC-002: Compliance checks can detect `.gitlab-ci.yml`, `.pre-commit-config.yaml`, `.git-cliff.toml`, `pyproject.toml`, `.flake8`, `.semgrep.yml`, and `.gitleaks.toml`.
- AC-003: Compliance checks can detect `.specify/`, `specify/`, `constitution.md`, `.specify/templates/`, `specify/templates/`, and `specs/`.
- AC-004: Tests and coverage are runnable through pytest.
