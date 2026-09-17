VEL Requirements (English)
==========================

Overview
--------

This document defines the baseline requirements for the Vehicle Evidence Layer (VEL) for S-CORE-based vehicle systems.

The intended functional scope is:

- provide a normalized Vehicle Evidence interface
- collect configured runtime, hardware, and S-CORE module state information
- normalize heterogeneous source data into traceable Vehicle Evidence
- expose normalized evidence through an external interface for designated consumers

The out-of-scope items are:

- multi-node coordination and boot-sequence orchestration
- final OEM safety, state, or vehicle-behavior decisions
- lifecycle, process, container, CPU, GPU, or NPU control

Traceability Rule
-----------------

Each requirement shall express one requirement only. If a statement needs more than one independent verification, it shall be split into separate requirement IDs.

Each stakeholder requirement in this document is linked to one or more feature requirements. Security and safety requirements are tracked in their own sections and shall not be counted as feature requirements.

Stakeholder Requirements
------------------------

STKH-VEL-001: Normalized Vehicle Evidence Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The platform shall define a normalized Vehicle Evidence data format.

Mapped Feature Requirements: FR-VEL-004

STKH-VEL-002: Metric Collection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The platform shall collect configured runtime and hardware metrics.

Mapped Feature Requirements: FR-VEL-001

STKH-VEL-003: Accessible Metric Source Mechanism
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The platform shall use accessible source mechanisms for metric collection.

Mapped Feature Requirements: FR-VEL-002

STKH-VEL-004: S-CORE Module State Collection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The platform shall collect configured S-CORE module state information.

Mapped Feature Requirements: FR-VEL-003

STKH-VEL-005: Source Normalization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The platform shall normalize source-specific data representations.

Mapped Feature Requirements: FR-VEL-005

STKH-VEL-006: Source Identity Traceability
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The platform shall preserve source identity for collected evidence.

Mapped Feature Requirements: FR-VEL-006

STKH-VEL-007: Observation Time Traceability
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The platform shall preserve observation time for collected evidence.

Mapped Feature Requirements: FR-VEL-007

STKH-VEL-008: Correlation Traceability
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The platform shall preserve correlation information when source context provides it.

Mapped Feature Requirements: FR-VEL-008

STKH-VEL-009: Evidence Quality
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The platform shall expose evidence quality information.

Mapped Feature Requirements: FR-VEL-009

STKH-VEL-010: VEL Health
~~~~~~~~~~~~~~~~~~~~~~~~

The platform shall expose VEL health information.

Mapped Feature Requirements: FR-VEL-010

STKH-VEL-011: External Evidence Access
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The platform shall expose normalized evidence to designated consumers.

Mapped Feature Requirements: FR-VEL-011

STKH-VEL-012: Platform Collector Separation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The platform shall separate platform-specific collectors from the common Evidence Layer.

Mapped Feature Requirements: FR-VEL-012

STKH-VEL-013: Input Interface Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The platform shall define source input interfaces through configuration.

Mapped Feature Requirements: FR-VEL-013

STKH-VEL-014: Output Evidence Interface Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The platform shall define normalized evidence output interfaces through configuration.

Mapped Feature Requirements: FR-VEL-014

STKH-VEL-015: Normalization Mapping Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The platform shall define source-to-evidence normalization mappings through configuration.

Mapped Feature Requirements: FR-VEL-015

STKH-VEL-016: Aggregation Data Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The platform shall support a consistent aggregation data format.

Mapped Feature Requirements: FR-VEL-016

Feature Requirements
--------------------

FR-VEL-001: Metric Collection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The system shall collect configured runtime and hardware metrics.

Satisfies: STKH-VEL-002

FR-VEL-002: Accessible Metric Source Mechanism
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The system shall collect metric data through files, commands, or supported operating-system interfaces.

Satisfies: STKH-VEL-003

FR-VEL-003: S-CORE Module State Collection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The system shall collect configured S-CORE module state information through S-CORE APIs exposed by the deployed environment.

Satisfies: STKH-VEL-004

FR-VEL-004: Normalized Vehicle Evidence Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The system shall transform collected source data into a normalized Vehicle Evidence data format.

Satisfies: STKH-VEL-001

FR-VEL-005: Source Normalization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The system shall normalize source-specific units and representations according to the configured normalization mapping.

Satisfies: STKH-VEL-005

FR-VEL-006: Source Identity Metadata
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The system shall include source identity in each evidence record.

Satisfies: STKH-VEL-006

FR-VEL-007: Observation Time Metadata
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The system shall include observation timestamp in each evidence record.

Satisfies: STKH-VEL-007

FR-VEL-008: Correlation Metadata
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The system shall include a correlation identifier in each evidence record when source context provides it.

Satisfies: STKH-VEL-008

FR-VEL-009: Evidence Quality Metadata
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The system shall attach quality information to each evidence record or evidence batch.

Satisfies: STKH-VEL-009

FR-VEL-010: VEL Health Exposure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The system shall expose VEL health information.

Satisfies: STKH-VEL-010

FR-VEL-011: External Evidence Interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The system shall expose normalized evidence through an external interface for designated consumers.

Satisfies: STKH-VEL-011

FR-VEL-012: Platform Collector Separation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The system shall isolate OS-specific and platform-specific collectors from the common Evidence Layer.

Satisfies: STKH-VEL-012

FR-VEL-013: Input Interface Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The system shall load source input interface definitions from configuration.

Satisfies: STKH-VEL-013

FR-VEL-014: Output Evidence Interface Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The system shall load normalized evidence output interface definitions from configuration.

Satisfies: STKH-VEL-014

FR-VEL-015: Normalization Mapping Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The system shall load source-to-evidence normalization mapping rules from configuration.

Satisfies: STKH-VEL-015

FR-VEL-016: Aggregation Data Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The system shall support an aggregation data format agreed with responsible data-format stakeholders.

Satisfies: STKH-VEL-016

Security Requirements
---------------------

SEC-VEL-001: Security Mechanism Integration Boundary
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

VEL shall apply security mechanisms selected by the deployed environment to the external evidence interface.

SEC-VEL-002: Authentication Authority Boundary
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

VEL shall not define or operate an independent authentication authority.

SEC-VEL-003: Evidence Interface Authentication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When caller authentication is required by the deployed environment, VEL shall rely on caller identity information supplied by the deployed environment.

SEC-VEL-004: Evidence Interface Access Control
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

VEL shall restrict external evidence access according to consumer access rules configured by the deployed environment.

SEC-VEL-005: Evidence Interface Integrity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

VEL shall support the integrity protection method selected by the deployed environment for evidence exchanged through the external evidence interface.

Safety Requirements
-------------------

SAF-VEL-001: Lifecycle Execution Boundary
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

VEL shall not execute workload lifecycle operations.

SAF-VEL-002: Process Control Boundary
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

VEL shall not execute process control operations.

SAF-VEL-003: Container Control Boundary
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

VEL shall not execute container control operations.

SAF-VEL-004: Hardware Control Boundary
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

VEL shall not execute hardware control operations.

SAF-VEL-005: Multi-Node Coordination Boundary
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

VEL shall not execute multi-node coordination.

SAF-VEL-006: OEM Decision Boundary
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

VEL shall not execute final OEM vehicle decision logic.

Assumptions of Use (AoU)
------------------------

AOU-VEL-001
~~~~~~~~~~~

The Vehicle Evidence interface field semantics are finalized by designated stakeholders. This open-source repository contains only publicly approved interface definitions.

AOU-VEL-002
~~~~~~~~~~~

Each deployment environment provides the S-CORE APIs and operating-system access required by its configured collectors.

AOU-VEL-003
~~~~~~~~~~~

A designated external consumer does not make VEL part of an OEM decision or control path.

AOU-VEL-004
~~~~~~~~~~~

The normalized aggregation data format is finalized through continuing agreement with the responsible data-format stakeholders.
