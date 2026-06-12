# Compliance Checklist

## Project Files

- `.editorconfig`
- `CHANGELOG.md`
- `SECURITY.md`
- `CODE_OF_CONDUCT.md`
- `.env.example`
- `Dockerfile`
- `.dockerignore`

## Quality Tools

- Ruff: `.ruff.toml`, `pyproject.toml`, `.pre-commit-config.yaml`, `Makefile`, CI
- Mypy: `mypy.ini`, `pyproject.toml`, `.pre-commit-config.yaml`, `Makefile`, CI
- Vulture: `pyproject.toml`, `.pre-commit-config.yaml`, `Makefile`, CI
- Bandit: `pyproject.toml`, `.pre-commit-config.yaml`, `Makefile`, CI
- Pylint: `.pylintrc`, `pyproject.toml`, `.pre-commit-config.yaml`, `Makefile`, CI
- Flake8: `.flake8`, `.pre-commit-config.yaml`, `Makefile`, CI
- Semgrep: `.semgrep.yml`, `.semgrepignore`, `Makefile`, CI
- Pyupgrade: `.pre-commit-config.yaml`, `Makefile`, CI

## Security

- Secret scanning: `.gitleaks.toml`, `.pre-commit-config.yaml`, CI
- Dependency audit: `pip-audit` in `requirements-dev.txt`, `Makefile`, CI
- Static analysis: Bandit in `pyproject.toml`, `.pre-commit-config.yaml`, CI

## Testing

- Test framework: pytest configured in `pyproject.toml`
- Coverage reporting: pytest-cov configured in `pyproject.toml`
- Coverage command: `pytest --cov=.`
- Fail-under threshold: `--cov-fail-under=20`

## Automation and CI

- GitLab CI: `.gitlab-ci.yml`
- GitHub Actions: `.github/workflows/ci.yml`
- Pre-commit hooks: `.pre-commit-config.yaml`
- Automated changelog: `.git-cliff.toml`, `automated_changelog` CI job, `git-cliff` pre-commit hook

## Spec Kit

- `constitution.md`
- `.specify/`
- `.specify/templates/`
- `.specify/memory/constitution.md`
- `specify/`
- `specify/templates/`
- `specs/`
