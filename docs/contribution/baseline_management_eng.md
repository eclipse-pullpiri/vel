# Baseline Management Rules

**Author**: Daeyoung Jeong (@daeyoung-jeong-lge)

## Table of Contents

1. [Overview](#1-overview)
2. [Baseline Tag Naming Convention](#2-baseline-tag-naming-convention)
3. [Baseline Types](#3-baseline-types)
4. [Baseline Criteria](#4-baseline-criteria)
5. [Baseline Procedure](#5-baseline-procedure)
6. [Change Management After Baseline](#6-change-management-after-baseline)
7. [Roles and Stakeholders](#7-roles-and-stakeholders)
8. [Baseline Management Diagrams](#8-baseline-management-diagrams)

---

## 1. Overview

A baseline is a reference point that represents a specific point in the project development lifecycle, and it is established by the CM (Configuration Management) manager.

If any code changes occur after a baseline is established, those changes must go through the stakeholder **approval and notification** process.

---

## 2. Baseline Tag Naming Convention

VEL follows its own convention based on [Semantic Versioning 2.0.0](https://semver.org/).

```text
v<MAJOR>.<MINOR>.<PATCH>[-<identifier>]
```

| Element      | Description                                                                 |
| ------------ | --------------------------------------------------------------------------- |
| `MAJOR`      | Incremented for incompatible changes intended for external organization delivery |
| `MINOR`      | Incremented when backward-compatible features are added                     |
| `PATCH`      | Incremented for backward-compatible bug fixes                               |
| `identifier` | Additional unofficial baseline qualifier (alpha, beta, rc1, milestone1, etc.) |

### Examples

| Tag                 | Meaning                                                |
| ------------------- | ---------------------------------------------------- |
| `v1.0.0`            | First official release                                |
| `v1.1.0`            | Official release with backward-compatible new features |
| `v1.1.1`            | Official patch release for bug fixes                  |
| `v2.0.0`            | Official major release with incompatible changes      |
| `v1.2.0-alpha`      | Unofficial baseline for internal alpha testing        |
| `v1.2.0-rc1`        | Unofficial baseline for release candidate             |
| `v1.2.0-milestone1` | Unofficial baseline for internal milestone            |

---

## 3. Baseline Types

### 3.1 Major Baseline

- **Definition**: A baseline for releasing to external organizations (customers, partners, etc.)
- **Target Branch**: `main`
- **Created By**: CM manager
- **Approval Requirement**: Approval from all stakeholders is required
- **GitHub Tag Format**: `v<MAJOR>.<MINOR>.<PATCH>` (e.g., `v1.0.0`)
- **GitHub Release**: When establishing an official baseline, release notes must be created on the GitHub Release page

### 3.2 Minor Baseline

- **Definition**: A baseline for internal review, pre-release validation, or incorporating minor, non-functional code updates, or for marking a development milestone
- **Target Branch**: `main` or a specific feature branch
- **Created By**: CM manager or development lead
- **Approval Requirement**: Approval from relevant team members
- **GitHub Tag Format**: `v<MAJOR>.<MINOR>.<PATCH>` (e.g., `v1.1.0`, `v1.2.1`)

### 3.3 Unofficial Baseline

- **Definition**: A baseline to urgently reflect fixes for purposes unrelated to functional safety, within a scope that handles non-safety domains. As a principle, it should be discarded after the objective is achieved.
- **Target Branch**: A specific feature branch
- **Created By**: CM manager
- **Approval Requirement**: CM manager approval
- **GitHub Tag Format**: `v<MAJOR>.<MINOR>.<PATCH>-<identifier>` (e.g., `v1.0.0-alpha`, `v1.1.0-milestone1`)

---

## 4. Baseline Criteria

### 4.1 Criteria for Major Baseline

An official baseline is established only when all of the following conditions are met.

| Condition | Detail |
| --------------- | ------------------------------------------------------------ |
| Feature implementation complete | All required features (FEATURE issues) for the release are implemented and their PRs are merged |
| Tests passed | Both unit and integration tests pass (confirm the `test:passed` label) |
| Code review complete | At least 1 reviewer has approved all changes |
| Build succeeded | The CI pipeline build succeeds |
| Documentation updated | `CHANGELOG`, `README`, API documentation, and other related documents are up to date |
| Stakeholder approval | All stakeholders approve in writing (or via issue) before the external release |

### 4.2 Criteria for Minor Baseline

An unofficial baseline is established when one or more of the following conditions are met.

- Non-functional code changes and minor routine updates
- Snapshot needed for internal review or demo
- Pre-validation (RC, alpha, beta) required before external release
- Internal milestone reached (end of sprint, transition of development phase, etc.)
- Development and integration of a major feature branch completed

---

## 5. Baseline Procedure

### 5.1 Major Baseline Procedure

1. **Pre-check**: The CM manager verifies all items in [4.1 Criteria for Major Baseline](#41-criteria-for-major-baseline)
2. **Issue Registration**: Register a baseline setup issue on GitHub
   - Title: `[TASK] Set up official baseline v<version>`
   - Labels: `type:task`, `priority:critical`
3. **Stakeholder Approval**: Obtain stakeholder approval through the issue or another channel
4. **Create and Push Tag**:
   ```bash
   git tag v<MAJOR>.<MINOR>.<PATCH>
   git push origin v<MAJOR>.<MINOR>.<PATCH>
   ```
5. **Write GitHub Release**: Write release notes on the GitHub Release page for the tag
6. **Notify**: Notify stakeholders and the development team that the baseline has been established
7. **Close Issue**: Close the baseline setup issue

### 5.2 Unofficial Baseline Procedure

1. **Pre-check**: Confirm approval from the relevant team lead
2. **Create and Push Tag**:
   ```bash
   git tag v<MAJOR>.<MINOR>.<PATCH>-<identifier>
   git push origin v<MAJOR>.<MINOR>.<PATCH>-<identifier>
   ```
3. **Notify**: Notify the relevant team members that the baseline has been set (issue comment or messenger)

---

## 6. Change Management After Baseline

After a baseline is established, any subsequent change to work products based on that baseline **must follow the procedure below**.

### 6.1 Change Request Procedure

1. **Register Change Issue**: Register the required change as a GitHub issue
   - Title: register as `[BUG]` or `[FEATURE]` type
   - Body: state the reason for the change, its impact scope, and its risk level
2. **Impact Analysis**: The CM manager and relevant developers analyze the impact scope of the change
3. **Stakeholder Approval**:
   - Change against a major baseline: approval from all stakeholders is required
   - Change against a minor baseline: approval from the relevant team lead
4. **Implement Change**: Develop on a function branch based on the approved issue, and create a PR
5. **Review and Merge**: Merge after code review and CI pass
6. **Set New Baseline** (if needed): Set a new baseline by incrementing the patch version

### 6.2 Prohibited Actions

- Deleting or rewriting (force-pushing) an official baseline tag without approval is prohibited
- Changing the history of the commit a baseline tag points to is prohibited
- Distributing official baseline artifacts without stakeholder approval is prohibited

---

## 7. Roles and Stakeholders

| Role             | Responsibility                                                               |
| ---------------- | -------------------------------------------------------------------------- |
| **CM Manager**   | Establish baseline, create tags, send notifications, lead intake and impact analysis of change requests |
| **Dev Lead**     | Verify feature completion and quality criteria, approve unofficial baselines |
| **Stakeholders** | Approve official baseline setup and changes                                |
| **Developers**   | Register change issues, implement changes, and create PRs                  |

---

## 8. Baseline Management Diagrams

### Baseline Setup Flow

```text
Development complete and tests passed
        ↓
CM pre-check (verify criteria items)
        ↓
Open baseline setup issue
        ↓
Obtain stakeholder approval
        ↓
Create and push Git tag
   - Official: v<MAJOR>.<MINOR>.<PATCH>
   - Unofficial: v<MAJOR>.<MINOR>.<PATCH>-<identifier>
        ↓
Write GitHub Release (official baseline only)
        ↓
Notify stakeholders
        ↓
Close baseline setup issue
```

### Post-baseline Change Flow

```text
Change requirement identified
        ↓
Create change issue (BUG/FEATURE)
        ↓
Impact analysis (CM manager + developers)
        ↓
Stakeholder approval
        ↓
Implement change in feature branch
        ↓
Create PR → Review → CI pass
        ↓
Merge into main branch
        ↓
Set new baseline (if needed)
        ↓
Notify stakeholders
```

### Version History Example

```text
main ──●──────●────────────────────────────────────►
       │      │
     v1.0.0  v1.1.0
  (Official BL) (Official BL)
       │
       └──► model/vehicle-x1 (model branch)
```
