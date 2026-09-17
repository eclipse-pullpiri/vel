# Security Policy

## Reporting a Vulnerability

If you discover a security vulnerability in VEL, please **do not** open a public GitHub issue. Instead, report it privately using GitHub's [private security advisory](../../security/advisories/new) feature for this repository, or contact the maintainers listed in [CODEOWNERS](CODEOWNERS).

Please include:

- A description of the vulnerability and its potential impact
- Steps to reproduce, including affected configuration artifacts, interface definitions, or collector code
- Any suggested mitigation, if known

## Scope

VEL is an Evidence Layer: it collects, normalizes, and exposes Vehicle Evidence, but it does not implement its own authentication authority (see `SEC-VEL-002`). Security-relevant reports commonly fall into one of these areas:

- Handling of the external evidence interface (`SEC-VEL-001`, `SEC-VEL-003`, `SEC-VEL-004`, `SEC-VEL-005`)
- Normalization/mapping logic that could be used to inject malformed or malicious evidence
- Configuration artifacts (input interface definitions, normalization mappings, output evidence definitions) that could be manipulated to bypass validation

Vulnerabilities in the deployment environment's own authentication, authorization, or transport security mechanisms are out of scope for VEL itself, since VEL relies on the deployed environment for these (see `SEC-VEL-002`, `SEC-VEL-003`).

## Response

Maintainers will acknowledge reports and coordinate a disclosure timeline before any public discussion of the issue.
