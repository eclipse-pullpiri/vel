Requirements Linting Guide
==========================

Purpose
-------

This guide defines mandatory quality checks for VEL requirements and their Sphinx documentation.

Mandatory Checks
----------------

1. Build integrity

- ``sphinx-build -W -b html docs docs/_build/html`` shall complete without warnings or errors.
- The Sphinx build shall fail when requirement IDs are duplicated, placed in the wrong requirement class, or use invalid ``STKH-VEL-*``, ``FR-VEL-*``, ``SEC-VEL-*``, or ``SAF-VEL-*`` formats.
- The Sphinx build shall fail when stakeholder-to-feature traceability is missing, inconsistent, or drifts between the English, Korean, and S-CORE requirements documents.
- The S-CORE Sphinx-Needs view shall preserve the same requirement titles and feature traceability as the authoritative English requirements for matching IDs.

2. Atomicity

- Each requirement ID shall contain one independently verifiable obligation.
- Split compound statements into separate IDs.

3. Requirement classification

- ``STKH-VEL-*`` identifies stakeholder requirements.
- ``FR-VEL-*`` identifies functional requirements.
- ``SEC-VEL-*`` identifies security requirements.
- ``SAF-VEL-*`` identifies safety requirements.
- Security and safety requirements shall not be written as functional requirements.

4. Traceability

- Every ``STKH-VEL-*`` requirement shall reference its implementing ``FR-VEL-*`` requirement.
- Each ``FR-VEL-*`` requirement shall identify the stakeholder requirement it satisfies.
- IDs shall be unique and stable.

5. Scope consistency

- VEL shall remain an Evidence Layer for collection, normalization, and evidence exposure.
- VEL shall not implement multi-node coordination, boot orchestration, lifecycle execution, process or container control, hardware control, or OEM final decision logic.
- Public documents shall not include non-public internal project names or private interface details.

6. Configuration-driven interfaces

- Input interface definitions, output evidence definitions, and normalization mappings shall be maintained as configuration artifacts.
- A new source shall be added through configuration and collector extension, without modifying common normalization behavior unless the common evidence format changes.

7. Language consistency

- English and Korean requirements shall preserve equivalent normative meaning.
- Use ``shall`` in English and ``해야 한다`` or ``해서는 안 된다`` in Korean.

Recommended Commands
--------------------

.. code-block:: bash

   python -m pip install -r docs/requirements.txt
   rm -rf docs/_build
   sphinx-build -W -b html docs docs/_build/html
