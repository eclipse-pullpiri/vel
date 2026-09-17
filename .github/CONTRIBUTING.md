# Contributing to VEL

Thank you for your interest in contributing to VEL (Vehicle Evidence Layer). This document is a short entry point; the full rules live under [docs/contribution/](../docs/contribution/) in both English and Korean.

## Before You Start

- Read [AGENTS.md](../AGENTS.md) for the product scope, architecture boundaries, and requirement conventions that every change must respect.
- VEL is an Evidence Layer only. Changes that add lifecycle execution, process/container/hardware control, multi-node coordination, or OEM decision logic are out of scope (see `SAF-VEL-*` in the requirements).

## Workflow Summary

1. **Find or create an issue.** Work is tracked as `EPIC` (initiative) > `FEATURE` (requirement) > `TASK` (development work), plus independent `BUG` issues. See [guidelines_eng.md](../docs/contribution/guidelines_eng.md) / [guidelines_kor.md](../docs/contribution/guidelines_kor.md).
2. **Create a branch** from `main` named `<type>/<issue-number>-<short-description>` (e.g. `feat/123-normalized-evidence-format`). See [branch_management_eng.md](../docs/contribution/branch_management_eng.md).
3. **Develop and commit** using `<type>(<scope>): <description> [#issue-number]` commit messages.
4. **Open a Pull Request** that includes `Closes #issue_number`, using the PR template. Direct pushes to `main` are not allowed.
5. **Request review.** At least one reviewer approval and a passing CI run are required before merge.

## Coding Conventions

VEL is developed in Rust. Follow [coding_rule_eng.md](../docs/contribution/coding_rule_eng.md) / [coding_rule_kor.md](../docs/contribution/coding_rule_kor.md) for naming, comments, error handling, and testing conventions.

## Requirements and Documentation Changes

- Requirements changes must update both [docs/en/requirements_eng.rst](../docs/en/requirements_eng.rst) and [docs/ko/requirements_kor.rst](../docs/ko/requirements_kor.rst) together, and keep [docs/score/requirements_score.rst](../docs/score/requirements_score.rst) consistent with them.
- Before submitting a PR that touches `docs/`, run:
  ```bash
  python -m pip install -r docs/requirements.txt
  sphinx-build -W -b html docs docs/_build/html
  ```
  The build must complete with no warnings or errors.

## Reporting Bugs or Security Issues

- Functional bugs: open a `[BUG]` issue as described in the guidelines above.
- Security vulnerabilities: follow [SECURITY.md](SECURITY.md) instead of filing a public issue.

## Code of Conduct

Participation in this project is governed by our [Code of Conduct](CODE_OF_CONDUCT.md).
