# VEL Project Instructions

> This file mirrors [AGENTS.md](../AGENTS.md) at the repository root, which is the tool-neutral version consumed by non-Copilot AI coding agents. Keep both in sync when either changes.

## Product Scope

- VEL means Vehicle Evidence Layer.
- VEL collects configured runtime, hardware, and S-CORE module state information; normalizes the data into Vehicle Evidence; and exposes the result to designated consumers.
- VEL does not perform multi-node coordination, boot-sequence orchestration, lifecycle execution, process or container control, hardware control, or final OEM vehicle decisions.
- Keep VEL as an Evidence Layer. Do not use internal project names or describe VEL as an adapter.

## Architecture

- Reuse Pullpiri modules only where they fit the VEL scope. NodeAgent is the collector host; ActionController, FilterGateway, StateManager, and PolicyManager are outside the active VEL execution path unless a later scope decision explicitly changes this.
- Use S-CORE Logging instead of Pullpiri logservice/common::logd.
- Use S-CORE Persistency instead of Pullpiri rocksdbservice/common::etcd when persistence is configured.
- Use S-CORE Communication and its applicable profile for S-CORE communication. Do not describe the communication library as a business communication target.
- Configuration, not hard-coded logic, defines input interfaces, output evidence interfaces, and source-to-evidence normalization mappings. Keep platform-specific collectors separate from the common Evidence Layer.

## Requirements

- Keep each requirement atomic: one independently verifiable obligation per ID.
- Use `STKH-VEL-*` for stakeholder requirements, `FR-VEL-*` for functional requirements, `SEC-VEL-*` for security requirements, and `SAF-VEL-*` for safety requirements.
- Do not put security or safety requirements in the functional requirements section.
- Maintain explicit traceability between stakeholder and functional requirements. Avoid ambiguous many-to-many mappings.
- Use mandatory wording: `shall` in English and `해야 한다` or `해서는 안 된다` in Korean. Avoid `should` and `바람직하다`.

## Public Documentation

- Do not mention non-public internal projects, internal interface names, or private implementation details.
- Do not present demonstration environments, platforms, boards, operating systems, dashboards, or transports as inherent VEL design requirements unless they are explicitly adopted as product scope.
- Maintain matching English and Korean documentation when updating requirements or architecture.
- Use PlantUML for architecture diagrams.

## Project Management

- VEL follows an issue-driven GitHub workflow adapted from Eclipse Pullpiri's contribution guide; see `docs/contribution/` (`guidelines_eng.md`/`guidelines_kor.md`, `branch_management_*`, `baseline_management_*`, `coding_rule_*`).
- Issues are classified as `EPIC` (top-level initiative) > `FEATURE` (requirement, child of an EPIC) > `TASK` (development work, child of a FEATURE); `BUG` is tracked independently.
- Development happens on `<type>/<issue-number>-<short-description>` branches created from an issue; direct commits/pushes to `main` are prohibited.
- Every change lands through a Pull Request linked to its issue (`Closes #issue_number`); at least one reviewer approval and passing CI are required before merge.
- Keep the English and Korean contribution documents in sync when updating the workflow, branch, baseline, or coding rules.

