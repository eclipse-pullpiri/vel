.. _vel_score_requirements:

VEL Requirements (S-CORE Style)
===============================

This Sphinx-Needs view mirrors the current VEL requirements. Functional, security, and safety requirements are intentionally separated.

Stakeholder Requirements
------------------------

.. stkh_req:: Normalized Vehicle Evidence Format
   :id: STKH-VEL-001

   The platform shall define a normalized Vehicle Evidence data format.

.. stkh_req:: Metric Collection
   :id: STKH-VEL-002

   The platform shall collect configured runtime and hardware metrics.

.. stkh_req:: Accessible Metric Source Mechanism
   :id: STKH-VEL-003

   The platform shall use accessible source mechanisms for metric collection.

.. stkh_req:: S-CORE Module State Collection
   :id: STKH-VEL-004

   The platform shall collect configured S-CORE module state information.

.. stkh_req:: Source Normalization
   :id: STKH-VEL-005

   The platform shall normalize source-specific data representations.

.. stkh_req:: Source Identity Traceability
   :id: STKH-VEL-006

   The platform shall preserve source identity for collected evidence.

.. stkh_req:: Observation Time Traceability
   :id: STKH-VEL-007

   The platform shall preserve observation time for collected evidence.

.. stkh_req:: Correlation Traceability
   :id: STKH-VEL-008

   The platform shall preserve correlation information when source context provides it.

.. stkh_req:: Evidence Quality
   :id: STKH-VEL-009

   The platform shall expose evidence quality information.

.. stkh_req:: VEL Health
   :id: STKH-VEL-010

   The platform shall expose VEL health information.

.. stkh_req:: External Evidence Access
   :id: STKH-VEL-011

   The platform shall expose normalized evidence to designated consumers.

.. stkh_req:: Platform Collector Separation
   :id: STKH-VEL-012

   The platform shall separate platform-specific collectors from the common Evidence Layer.

.. stkh_req:: Input Interface Configuration
   :id: STKH-VEL-013

   The platform shall define source input interfaces through configuration.

.. stkh_req:: Output Evidence Interface Configuration
   :id: STKH-VEL-014

   The platform shall define normalized evidence output interfaces through configuration.

.. stkh_req:: Normalization Mapping Configuration
   :id: STKH-VEL-015

   The platform shall define source-to-evidence normalization mappings through configuration.

.. stkh_req:: Aggregation Data Format
   :id: STKH-VEL-016

   The platform shall support a consistent aggregation data format.

Feature Requirements
--------------------

.. feat_req:: Metric Collection
   :id: FR-VEL-001
   :satisfies: STKH-VEL-002

   The system shall collect configured runtime and hardware metrics.

.. feat_req:: Accessible Metric Source Mechanism
   :id: FR-VEL-002
   :satisfies: STKH-VEL-003

   The system shall collect metric data through files, commands, or supported operating-system interfaces.

.. feat_req:: S-CORE Module State Collection
   :id: FR-VEL-003
   :satisfies: STKH-VEL-004

   The system shall collect configured S-CORE module state information through S-CORE APIs exposed by the deployed environment.

.. feat_req:: Normalized Vehicle Evidence Format
   :id: FR-VEL-004
   :satisfies: STKH-VEL-001

   The system shall transform collected source data into a normalized Vehicle Evidence data format.

.. feat_req:: Source Normalization
   :id: FR-VEL-005
   :satisfies: STKH-VEL-005

   The system shall normalize source-specific units and representations according to the configured normalization mapping.

.. feat_req:: Source Identity Metadata
   :id: FR-VEL-006
   :satisfies: STKH-VEL-006

   The system shall include source identity in each evidence record.

.. feat_req:: Observation Time Metadata
   :id: FR-VEL-007
   :satisfies: STKH-VEL-007

   The system shall include observation timestamp in each evidence record.

.. feat_req:: Correlation Metadata
   :id: FR-VEL-008
   :satisfies: STKH-VEL-008

   The system shall include a correlation identifier in each evidence record when source context provides it.

.. feat_req:: Evidence Quality Metadata
   :id: FR-VEL-009
   :satisfies: STKH-VEL-009

   The system shall attach quality information to each evidence record or evidence batch.

.. feat_req:: VEL Health Exposure
   :id: FR-VEL-010
   :satisfies: STKH-VEL-010

   The system shall expose VEL health information.

.. feat_req:: External Evidence Interface
   :id: FR-VEL-011
   :satisfies: STKH-VEL-011

   The system shall expose normalized evidence through an external interface for designated consumers.

.. feat_req:: Platform Collector Separation
   :id: FR-VEL-012
   :satisfies: STKH-VEL-012

   The system shall isolate OS-specific and platform-specific collectors from the common Evidence Layer.

.. feat_req:: Input Interface Configuration
   :id: FR-VEL-013
   :satisfies: STKH-VEL-013

   The system shall load source input interface definitions from configuration.

.. feat_req:: Output Evidence Interface Configuration
   :id: FR-VEL-014
   :satisfies: STKH-VEL-014

   The system shall load normalized evidence output interface definitions from configuration.

.. feat_req:: Normalization Mapping Configuration
   :id: FR-VEL-015
   :satisfies: STKH-VEL-015

   The system shall load source-to-evidence normalization mapping rules from configuration.

.. feat_req:: Aggregation Data Format
   :id: FR-VEL-016
   :satisfies: STKH-VEL-016

   The system shall support an aggregation data format agreed with responsible data-format stakeholders.

Security Requirements
---------------------

.. sec_req:: Security Mechanism Integration Boundary
   :id: SEC-VEL-001

   VEL shall apply security mechanisms selected by the deployed environment to the external evidence interface.

.. sec_req:: Authentication Authority Boundary
   :id: SEC-VEL-002

   VEL shall not define or operate an independent authentication authority.

.. sec_req:: Evidence Interface Authentication
   :id: SEC-VEL-003

   When caller authentication is required by the deployed environment, VEL shall rely on caller identity information supplied by the deployed environment.

.. sec_req:: Evidence Interface Access Control
   :id: SEC-VEL-004

   VEL shall restrict external evidence access according to consumer access rules configured by the deployed environment.

.. sec_req:: Evidence Interface Integrity
   :id: SEC-VEL-005

   VEL shall support the integrity protection method selected by the deployed environment for evidence exchanged through the external evidence interface.

Safety Requirements
-------------------

.. saf_req:: Lifecycle Execution Boundary
   :id: SAF-VEL-001

   VEL shall not execute workload lifecycle operations.

.. saf_req:: Process Control Boundary
   :id: SAF-VEL-002

   VEL shall not execute process control operations.

.. saf_req:: Container Control Boundary
   :id: SAF-VEL-003

   VEL shall not execute container control operations.

.. saf_req:: Hardware Control Boundary
   :id: SAF-VEL-004

   VEL shall not execute hardware control operations.

.. saf_req:: Multi-Node Coordination Boundary
   :id: SAF-VEL-005

   VEL shall not execute multi-node coordination.

.. saf_req:: OEM Decision Boundary
   :id: SAF-VEL-006

   VEL shall not execute final OEM vehicle decision logic.
