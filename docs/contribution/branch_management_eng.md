# Branch Management Rules

**Author**: Daeyoung Jeong (@daeyoung-jeong-lge)

## Table of Contents
1. [Overview](#1-overview)
2. [Branch Types](#2-branch-types)
3. [Branch Naming Convention](#3-branch-naming-convention)
4. [Branch Creation Criteria and Procedure](#4-branch-creation-criteria-and-procedure)
5. [Branch Integration Rules](#5-branch-integration-rules)
6. [Branch Owners](#6-branch-owners)
7. [Branch Protection Rules](#7-branch-protection-rules)
8. [Branch Management Diagrams](#8-branch-management-diagrams)

---

## 1. Overview

This document defines the branch management strategy to preserve source code integrity and the single-module concept.
Branches are broadly divided into **long-lived branches** and **supporting branches**, with clear creation criteria, procedures, and ownership for each.

---

## 2. Branch Types

### 2.1 Long-lived Branch

| Branch | Description |
|--------|------|
| `main` | The latest release-ready stable code. Corresponds to the official baseline; direct commits are prohibited |

### 2.2 Model Branch

- **Definition**: A branch created for target-specific customization after an official baseline has been established
- **Created When**: After the official baseline (`main`) tag has been set
- **Purpose**: Add target-specific features, incorporate target-specific requirements, and keep target code independent
- **Naming Convention**: `model/<target-name>` (e.g., `model/vehicle-x1`)
- **Integration Policy**: Common improvements from a model branch can be back-merged into `main` through a separate PR

### 2.3 Function Branch

- **Definition**: A branch created for a major feature change or new feature development
- **Created When**: When the related issue is registered and development begins
- **Purpose**: Enable parallel feature-level development, and independent code review and testing
- **Naming Convention**: `<type>/<issue-number>-<short-description>`
- **Integration Policy**: Merged into `main` through a PR after development is complete

#### Function Branch Type Details

| Type | Description | Example |
|------|------|------|
| `feat` | New feature development | `feat/123-vehicle-evidence-output-api` |
| `fix` | Bug fix | `fix/145-correlation-id-retry-bug` |
| `refactor` | Code refactoring | `refactor/167-nodeagent-cleanup` |
| `docs` | Documentation work | `docs/189-contribution-guide` |
| `test` | Test code work | `test/201-normalization-integration-test` |
| `chore` | Build/configuration maintenance | `chore/210-ci-pipeline-update` |

---

## 3. Branch Naming Convention

### 3.1 Function Branch
```
<type>/<issue-number>-<short-description>
```
- Use lowercase letters and hyphens (`-`)
- Must include the issue number
- Keep the description within 3 words; lowercase English recommended

**Examples**
- `feat/123-normalized-evidence-format`
- `fix/145-correlation-id-retry-bug`
- `docs/167-contribution-guide`

### 3.2 Model Branch
```
model/<target-name>
```
- Use an identifier agreed upon with the deployment target or project

**Examples**
- `model/vehicle-x1`
- `model/ivi-platform-v2`

---

## 4. Branch Creation Criteria and Procedure

### 4.1 Function Branch Creation Procedure

1. Register the related issue on GitHub (confirm the issue number)
2. Use "Development" > "Create a branch" on the issue page, or create it from the command line:
   ```bash
   git checkout -b feat/<issue-number>-<description> main
   ```
3. Change the issue status label to `status:in-progress`
4. Create a PR and request review after development is complete

### 4.2 Model Branch Creation Procedure

1. The CM manager confirms the official baseline tag
2. Register a model branch creation request issue (type: `[TASK]`, label: `type:task`)
3. The CM manager creates the branch at that tag:
   ```bash
   git checkout -b model/<target-name> <baseline-tag>
   git push origin model/<target-name>
   ```
4. Notify stakeholders that the branch has been created

---

## 5. Branch Integration Rules

### 5.1 Function Branch → main Integration

| Item | Criteria |
|------|------|
| Integration Method | Pull Request (PR) |
| Reviewer | At least 1 approval required |
| CI Pass | Required (build, test, and lint must all pass) |
| Commit Strategy | Squash merge or merge commit (per team agreement) |
| Branch Deletion | Delete the function branch after the merge is complete |

### 5.2 Model Branch Back-merge

- Common bug fixes or feature improvements from a model branch can be back-merged into `main`
- A separate PR must be created for the back-merge, and review by the CM manager and relevant stakeholders is required
- Confirm that the change is separated from target-specific code before back-merging

### 5.3 Prohibited Actions

- Direct `push` to the `main` branch is prohibited
- Merging without a completed review is prohibited
- Merging while CI is failing is prohibited

---

## 6. Branch Owners

| Branch Type | Creation Owner | Integration (Merge) Approval |
|-------------|-----------|----------------|
| `main` | CM manager | CM manager |
| `model/*` | CM manager | CM manager + stakeholders |
| `feat/*`, `fix/*`, etc. | Developer | Reviewer (at least 1) |

---

## 7. Branch Protection Rules

The following GitHub branch protection rules apply to the `main` branch.

1. **GitHub Settings Path**: Repository > Settings > Branches > Branch protection rules
2. **Applied Rules**:
   - `Require a pull request before merging` (direct push prohibited)
   - `Require approvals`: at least 1 approval required
   - `Require status checks to pass before merging` (CI pass required)
   - `Require linear history` (keep a linear history)
   - `Do not allow bypassing the above settings` (no exceptions, including administrators)

---

## 8. Branch Management Diagrams

```
main
──────────────────────────────────────────────────────►
  │                    ▲              ▲
  │ (baseline tag)      │ PR merge      │ PR merge
  │                    │              │
  ├──► model/vehicle-x1 (model branch) │
  │       └── target-specific dev      │
  │                                   │
  ├──► feat/123-normalized-evidence-format ────────┘
  │       └── new feature development
  │
  └──► fix/145-correlation-id-retry-bug ──────────► (deleted after PR merge)
          └── bug fix
```

### Branch Lifecycle

```
Register issue
    ↓
Create branch (developer/CM)
    ↓
Development and commits
    ↓
Create PR and request review
    ↓
CI verification (build/test/lint)
    ↓
Reviewer approval
    ↓
Merge into main
    ↓
Delete function branch
    ↓
Issue automatically closed
```
