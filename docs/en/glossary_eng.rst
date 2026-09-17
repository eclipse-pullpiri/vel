VEL Glossary (English)
=======================

This glossary defines terms used consistently across VEL requirements, architecture, and interface documents. Use these terms instead of inventing new synonyms.

Vehicle Evidence
-----------------

The normalized, traceable output that VEL produces from collected source data. Vehicle Evidence includes the observed value or state, source identity, observation time, and (when supplied) a correlation identifier.

Vehicle Evidence Layer (VEL)
-----------------------------

The canonical name of the product. VEL is an Evidence Layer that collects, normalizes, and exposes Vehicle Evidence to designated consumers.

Evidence Layer
---------------

The role VEL plays in the overall system: collecting, normalizing, and exposing Vehicle Evidence to designated consumers. VEL does not perform multi-node coordination, lifecycle execution, process/container/hardware control, or final OEM decisions.

Source
------

Any runtime, hardware, or S-CORE module that provides raw data to VEL through a Source Collector.

Source Collector
------------------

The component that reads raw data from a source (via files, commands, supported OS interfaces, or S-CORE APIs) according to an Input Interface Definition.

Input Interface Definition
----------------------------

A configuration artifact that defines the fields, types, and requiredness of the raw data VEL accepts from a given source.

Normalization Mapping
------------------------

A configuration artifact that defines how source-specific data is transformed into normalized Vehicle Evidence: unit conversion, enum/state mapping, and the quality rules applied during the transformation.

Output Evidence Definition
-----------------------------

A configuration artifact that defines the fields of the normalized Vehicle Evidence VEL exposes through its external interface.

Evidence Quality
-----------------

Metadata attached to an evidence record or evidence batch describing its validity, freshness, completeness, and mapping quality (for example, whether the value was mapped exactly, approximately, or left unmapped).

Correlation Identifier
-------------------------

An identifier that links multiple evidence records originating from the same source event or execution instance, when the source context supplies one.

VEL Health
-----------

Status information VEL exposes about its own collection pipeline (for example, whether a collector is running and producing evidence), distinct from the Vehicle Evidence content itself.

Designated Consumer
----------------------

An external component or system, outside VEL, that is authorized by the deployed environment to receive normalized Vehicle Evidence through the external evidence interface.

S-CORE Module
--------------

A module of the S-CORE platform whose state can be observed and collected by VEL as a source, through S-CORE APIs exposed by the deployed environment.

Evidence Runtime
-----------------

The deployment-specific host for VEL components (for example, Pullpiri's NodeAgent). It may host Source Collectors, Evidence Processing, and publication components, but it is not a VEL product boundary and does not execute lifecycle, process, container, or hardware actions.

Baseline
--------

A tagged reference point in the VEL repository history, established by the CM manager, used to track official and unofficial releases. See `docs/contribution/baseline_management_eng.md`.
