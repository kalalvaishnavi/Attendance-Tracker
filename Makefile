.PHONY: install-dev format lint type_check test coverage security changelog compliance

install-dev:
	python -m pip install --upgrade pip
	python -m pip install -r requirements-dev.txt

format:
	ruff format --check .
	pyupgrade --py310-plus app.py sql_queries.py tests/*.py
	git diff --exit-code -- app.py sql_queries.py tests

lint:
	ruff check .
	flake8 .
	pylint app.py sql_queries.py tests
	vulture app.py sql_queries.py tests

type_check:
	mypy app.py sql_queries.py

test:
	pytest --no-cov

coverage:
	pytest --cov=.

security:
	bandit -c pyproject.toml -r app.py sql_queries.py
	pip-audit
	semgrep scan --config auto --config p/python --config p/secrets
	gitleaks detect --source . --config .gitleaks.toml --no-git --verbose

changelog:
	git-cliff --config .git-cliff.toml --output CHANGELOG.md --unreleased

compliance: format lint type_check security test coverage changelog
