# GitHub Development Workflow Guidelines

**Author**: Daeyoung Jeong (@daeyoung-jeong-lge)

This guide defines the issue, branch, commit, and pull request workflow for the VEL project. It is adapted from the Eclipse Pullpiri contribution guide for VEL's own scope and governance.

## Table of Contents
1. [Issue Registration Rules](#1-issue-registration-rules)
2. [Branch Creation Rules](#2-branch-creation-rules)
3. [Commit Rules](#3-commit-rules)
4. [Labeling Rules by Stage](#4-labeling-rules-by-stage)
5. [Step-by-Step Workflow Guide](#5-step-by-step-workflow-guide)
6. [Automation Setup Guide](#6-automation-setup-guide)

---

## 1. Issue Registration Rules

### Issue Type Classification
- **EPIC**: Large initiative Issue that groups related FEATURE issues (top-level)
- **FEATURE**: Requirement Issue (child of an EPIC, parent of TASK issues)
- **TASK**: Development Task Issue (child of a FEATURE issue)
- **BUG**: Bug Fix Issue

### Issue Hierarchy

```
EPIC
 └── FEATURE
      └── TASK
```

`BUG` issues are tracked independently and are not required to belong to an EPIC or FEATURE.

### Issue Title Format
```
[Type] Title
```

Example:
- `[EPIC] Vehicle Evidence Output Interface`
- `[FEATURE] Normalized Vehicle Evidence Format`
- `[TASK] Define Evidence Header Schema`
- `[BUG] Correlation Identifier Missing on Retry`

### Issue Body Template

#### Epic (EPIC) Issue Template
```markdown
---
name: Epic
about: Large initiative that groups related feature requirements
title: '[EPIC] '
labels: type:epic, status:backlog
assignees: ''
---

## 🎯 Goal
<!-- What outcome this epic delivers and why it matters -->

## 📋 Scope
<!-- What is included and explicitly excluded -->

## 📌 Related Features
<!-- Automatically updated -->
- [ ] #

## 📎 Related Documents/References
<!-- Links to related documents -->

## 📊 Progress Summary
<!-- Automatically updated -->
```

#### Requirement (FEATURE) Issue Template
```markdown
---
name: Requirement
about: New feature requirement
title: '[FEATURE] '
labels: type:requirement, status:backlog
assignees: ''
---

## 🔗 Related Epic
<!-- Link to parent epic in "Relates to #epic_number" format -->
Relates to #

## 📝 Requirement Description
<!-- Detailed description of the requirement -->

## 📋 Acceptance Criteria
- [ ] Criterion 1
- [ ] Criterion 2

## 📎 Related Documents/References
<!-- Links to related documents -->

## 📌 Subtasks
<!-- Automatically updated -->

## 🧪 Testing Plan
- [ ] Unit Test:
- [ ] Integration Test:
- [ ] Performance Test:

## 📊 Test Results
<!-- Automatically updated after issue closure -->
```

#### Development Task (TASK) Issue Template
```markdown
---
name: Development Task
about: Development task to be implemented
title: '[TASK] '
labels: type:task, status:todo
assignees: ''
---

## 📝 Task Description
<!-- Description of the task to be performed -->

## 📋 Checklist
- [ ] Item 1
- [ ] Item 2

## 🔗 Related Requirement
<!-- Link to parent requirement in "Relates to #issue_number" format -->
Relates to #

## 📐 Implementation Guidelines
<!-- Reference material for implementation -->

## 🧪 Testing Method
<!-- Testing method after implementation -->
```

### Issue Relationship Setup

- Connect Epic (EPIC) and Requirement (FEATURE): Specify `Relates to #epic_number` in the FEATURE issue description.
- Connect Requirement (FEATURE) and Development Task (TASK): Specify `Relates to #requirement_number` in the TASK issue description.
- Track related features in the epic issue:

```markdown
## 📌 Related Features
- [ ] #123 Normalized Vehicle Evidence Format
- [ ] #124 Evidence Quality Metadata
```

- Track subtasks in the requirement issue:

```markdown
## 📌 Subtasks
- [ ] #125 Define Evidence Header Schema
- [ ] #126 Implement Quality Attachment Logic
```

---

## 2. Branch Creation Rules

### Branch Naming Convention
```
<type>/<issue_number>-<short-description>
```

### Branch Types

- **feat**: New feature development
- **fix**: Bug fix
- **refactor**: Code refactoring
- **docs**: Documentation work
- **test**: Test code work
- **chore**: Other maintenance work

### Examples

- `feat/123-normalized-evidence-format`
- `fix/145-correlation-id-retry-bug`
- `docs/167-contribution-guide`

### Branch Creation Procedure

1. Use "Development" > "Create a branch" on the issue page, or
2. From the command line:
```bash
git checkout -b feat/123-normalized-evidence-format main
```

---

## 3. Commit Rules

## Commit Message Format
```
<type>(<scope>): <description> [#issue-number]
```

## Commit Types

- **feat**: New feature
- **fix**: Bug fix
- **docs**: Documentation changes
- **style**: Code formatting, missing semicolons, etc.
- **refactor**: Code refactoring
- **test**: Test-related code
- **chore**: Build tasks, package manager configuration, etc.

## Examples

- `feat(evidence): Add correlation identifier propagation [#123]`
- `fix(collector): Fix NPU status enum mapping [#145]`
- `docs(contribution): Update PR body template [#167]`

## Detailed Commit Description (Optional)
```
<type>(<scope>): <description> [#issue-number]

<Detailed explanation>

<Caveats or Breaking Changes>

<Related Issues (Closes, Fixes, Resolves)>
```

## PR Body Format

```markdown
## 📝 PR Description
<!-- Description of the changes -->

## 🔗 Related Issue
<!-- Link to the issue this PR resolves (Use Closes, Fixes, Resolves keywords) -->
Closes #

## 🧪 Test Method
<!-- Description of the test method -->

## 📸 Screenshots
<!-- Attach screenshots if there are UI changes -->

## ✅ Checklist
- [ ] Code conventions are followed
- [ ] Tests are added/modified
- [ ] Documentation is updated (if necessary)
- [ ] `sphinx-build -W -b html docs docs/_build/html` passes with no warnings (if `docs/` changed)
- [ ] English and Korean documentation are kept in sync (if requirements/architecture/contribution docs changed)
```

---

## 4. Labeling Rules By Stage

### Label System

#### 1. Status Labels (status:*)
- `status:backlog` - Issue in the backlog
- `status:todo` - Issue in the to-do list
- `status:in-progress` - Issue in progress
- `status:review` - Under review
- `status:blocked` - Blocked
- `status:done` - Completed

#### 2. Type Labels (type:*)
- `type:epic` - Epic issue
- `type:requirement` - Requirement issue
- `type:task` - Development task issue
- `type:bug` - Bug issue
- `type:enhancement` - Feature enhancement
- `type:documentation` - Documentation task

#### 3. Priority Labels (priority:*)
- `priority:critical` - Highest priority
- `priority:high` - High priority
- `priority:medium` - Medium priority
- `priority:low` - Low priority

#### 4. Test Status Labels (test:*)
- `test:pending` - Test pending
- `test:running` - Test running
- `test:passed` - Test passed
- `test:failed` - Test failed

### Label Color Guide
```
Status labels: Blue shades
Type labels: Green shades
Priority labels: Red/Yellow shades
Complexity labels: Purple shades
Test status labels: Gray/Black shades
```

---

## 5. Step-by-Step Workflow Guide

### 1. Create Epic Issue
- Title: `[EPIC] Epic Title`
- Labels: `type:epic`, `status:backlog`
- Describe the goal and scope

### 2. Create Requirement Issue
- Title: `[FEATURE] Requirement Title`
- Labels: `type:requirement`, `status:backlog`
- Link to parent issue: `Relates to #epic_number`
- Write detailed description

### 3. Create Development Task Issue
- Title: `[TASK] Task Title`
- Labels: `type:task`, `status:todo`
- Link to parent issue: `Relates to #requirement_number`

### 4. Create Branch and Develop
- Branch name: `feat/issue_number-task_name`
- Change issue status: `status:in-progress`

### 5. Commit and Push
- Commit message: `feat(scope): Implementation details [#issue_number]`

### 6. Create Pull Request
- Title: `[Issue Type] Issue Title (#issue_number)`
- Include `Closes #issue_number` in the body
- Label: `status:review`

### 7. Code Review and Merge
- Assign reviewers
- Merge after approval
- Issue automatically closes

### 8. Run Tests
- Trigger test execution
- Update labels based on test results: `test:passed` or `test:failed`
- Update the requirement issue with test results

---

## 6. Automation Setup Guide

### Branch Protection Rules
1. Repository > Settings > Branches > Branch protection rules
2. Configure protection rules for the main/master branch:
  - Require pull request reviews
  - Require status checks to pass
  - Require linear history

### Label Automation Workflow
Implement the following automation using GitHub Actions:
  - Set initial labels when creating issues/PRs
  - Update issue status when creating a branch
  - Run tests and update labels when merging a PR

---

## Workflow Diagram

```
Create Epic Issue (assignee)
      ↓
  Create Requirement Issue (assignee)
       ↓
  Create Sub-tasks (assignee)
       ↓
  Create Branch (assignee)
       ↓
    Development Work (assignee)
       ↓
    Commit and Push (assignee)
       ↓
    Create PR (assignee)
       ↓
  Code Review (reviewer)
       ↓
  Approve and Merge PR (reviewer)
       ↓
  Run Automated Tests (assignee)
       ↓
  Close Issue and Update Results (assignee)
```
