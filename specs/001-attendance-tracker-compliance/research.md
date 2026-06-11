# Research: Attendance Tracker Compliance

## Decision

Use both GitLab CI and GitHub Actions workflow files so compliance tools can detect jobs regardless of which CI provider they scan.

## Rationale

The compliance report detected `test` but missed `format`, `lint`, `type_check`, and `coverage`, so the repository exposes those checks as explicit stages, jobs, and Makefile targets.

## Alternatives Considered

- Single combined quality job: rejected because some scanners only match exact job names.
- Documentation-only compliance: rejected because CI and pre-commit automation should be executable.
