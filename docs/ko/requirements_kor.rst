VEL 요구사항 (한국어)
======================

개요
----

본 문서는 Vehicle Evidence Layer(VEL)를 S-CORE 기반 차량 시스템용 evidence layer로 정의하기 위한 기준 요구사항을 기술한다.

의도된 기능 범위는 다음과 같다.

- normalized Vehicle Evidence interface 제공
- 구성된 runtime, hardware 및 S-CORE 모듈 상태 정보 수집
- 이기종 source 데이터를 추적 가능한 Vehicle Evidence로 정규화
- 지정된 소비자를 위한 external interface로 정규화 증거 노출

범위 밖 항목은 다음과 같다.

- multi-node coordination 및 boot-sequence orchestration
- OEM의 최종 안전, 상태, 차량 행동 의사결정
- lifecycle, process, container, CPU, GPU, NPU 제어

추적성 규칙
-----------

각 요구사항은 하나의 요구사항만 표현해야 한다. 독립적인 검증이 둘 이상 필요한 문장은 별도 요구사항 ID로 분리해야 한다.

본 문서의 각 이해관계자 요구사항은 하나 이상의 기능 요구사항에 연결된다. 보안 요구사항과 안전 요구사항은 별도 섹션에서 추적하며 기능 요구사항으로 간주하지 않는다.

이해관계자 요구사항
-------------------

STKH-VEL-001: Normalized Vehicle Evidence Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

플랫폼은 normalized Vehicle Evidence data format을 정의해야 한다.

연결 기능 요구사항: FR-VEL-004

STKH-VEL-002: Metric Collection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

플랫폼은 구성된 runtime 및 hardware metric을 수집해야 한다.

연결 기능 요구사항: FR-VEL-001

STKH-VEL-003: Accessible Metric Source Mechanism
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

플랫폼은 metric 수집에 접근 가능한 source mechanism을 사용해야 한다.

연결 기능 요구사항: FR-VEL-002

STKH-VEL-004: S-CORE Module State Collection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

플랫폼은 구성된 S-CORE 모듈 상태 정보를 수집해야 한다.

연결 기능 요구사항: FR-VEL-003

STKH-VEL-005: Source Normalization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

플랫폼은 source별 data representation을 정규화해야 한다.

연결 기능 요구사항: FR-VEL-005

STKH-VEL-006: Source Identity Traceability
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

플랫폼은 수집된 evidence의 source identity를 보존해야 한다.

연결 기능 요구사항: FR-VEL-006

STKH-VEL-007: Observation Time Traceability
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

플랫폼은 수집된 evidence의 observation time을 보존해야 한다.

연결 기능 요구사항: FR-VEL-007

STKH-VEL-008: Correlation Traceability
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

플랫폼은 source context가 제공하는 correlation information을 보존해야 한다.

연결 기능 요구사항: FR-VEL-008

STKH-VEL-009: Evidence Quality
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

플랫폼은 evidence quality 정보를 노출해야 한다.

연결 기능 요구사항: FR-VEL-009

STKH-VEL-010: VEL Health
~~~~~~~~~~~~~~~~~~~~~~~~

플랫폼은 VEL health 정보를 노출해야 한다.

연결 기능 요구사항: FR-VEL-010

STKH-VEL-011: External Evidence Access
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

플랫폼은 지정된 소비자에게 normalized evidence를 노출해야 한다.

연결 기능 요구사항: FR-VEL-011

STKH-VEL-012: Platform Collector Separation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

플랫폼은 platform-specific collector를 common Evidence Layer에서 분리해야 한다.

연결 기능 요구사항: FR-VEL-012

STKH-VEL-013: Input Interface Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

플랫폼은 source input interface를 configuration으로 정의해야 한다.

연결 기능 요구사항: FR-VEL-013

STKH-VEL-014: Output Evidence Interface Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

플랫폼은 normalized evidence output interface를 configuration으로 정의해야 한다.

연결 기능 요구사항: FR-VEL-014

STKH-VEL-015: Normalization Mapping Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

플랫폼은 source-to-evidence normalization mapping을 configuration으로 정의해야 한다.

연결 기능 요구사항: FR-VEL-015

STKH-VEL-016: Aggregation Data Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

플랫폼은 일관된 aggregation data format을 지원해야 한다.

연결 기능 요구사항: FR-VEL-016

기능 요구사항
-------------

FR-VEL-001: Metric Collection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

시스템은 구성된 runtime 및 hardware metric을 수집해야 한다.

만족 대상: STKH-VEL-002

FR-VEL-002: Accessible Metric Source Mechanism
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

시스템은 file, command 또는 지원 OS interface를 통해 metric data를 수집해야 한다.

만족 대상: STKH-VEL-003

FR-VEL-003: S-CORE Module State Collection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

시스템은 배포 환경에서 노출되는 S-CORE API를 통해 구성된 S-CORE 모듈 상태 정보를 수집해야 한다.

만족 대상: STKH-VEL-004

FR-VEL-004: Normalized Vehicle Evidence Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

시스템은 수집한 source data를 normalized Vehicle Evidence data format으로 변환해야 한다.

만족 대상: STKH-VEL-001

FR-VEL-005: Source Normalization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

시스템은 configured normalization mapping에 따라 source별 unit과 representation을 정규화해야 한다.

만족 대상: STKH-VEL-005

FR-VEL-006: Source Identity Metadata
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

시스템은 각 evidence record에 source identity를 포함해야 한다.

만족 대상: STKH-VEL-006

FR-VEL-007: Observation Time Metadata
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

시스템은 각 evidence record에 observation timestamp를 포함해야 한다.

만족 대상: STKH-VEL-007

FR-VEL-008: Correlation Metadata
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

시스템은 source context가 제공하는 경우 각 evidence record에 correlation identifier를 포함해야 한다.

만족 대상: STKH-VEL-008

FR-VEL-009: Evidence Quality Metadata
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

시스템은 각 evidence record 또는 evidence batch에 quality information을 부여해야 한다.

만족 대상: STKH-VEL-009

FR-VEL-010: VEL Health Exposure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

시스템은 VEL health 정보를 노출해야 한다.

만족 대상: STKH-VEL-010

FR-VEL-011: External Evidence Interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

시스템은 지정된 소비자에게 external interface를 통해 normalized evidence를 노출해야 한다.

만족 대상: STKH-VEL-011

FR-VEL-012: Platform Collector Separation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

시스템은 OS-specific 및 platform-specific collector를 common Evidence Layer에서 분리해야 한다.

만족 대상: STKH-VEL-012

FR-VEL-013: Input Interface Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

시스템은 source input interface definition을 configuration에서 load해야 한다.

만족 대상: STKH-VEL-013

FR-VEL-014: Output Evidence Interface Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

시스템은 normalized evidence output interface definition을 configuration에서 load해야 한다.

만족 대상: STKH-VEL-014

FR-VEL-015: Normalization Mapping Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

시스템은 source-to-evidence normalization mapping rule을 configuration에서 load해야 한다.

만족 대상: STKH-VEL-015

FR-VEL-016: Aggregation Data Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

시스템은 담당 data-format 이해관계자와 합의한 aggregation data format을 지원해야 한다.

만족 대상: STKH-VEL-016

보안 요구사항
-------------

SEC-VEL-001: Security Mechanism Integration Boundary
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

VEL은 external evidence interface에 배포 환경이 선택한 security mechanism을 적용해야 한다.

SEC-VEL-002: Authentication Authority Boundary
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

VEL은 독립적인 authentication authority를 정의하거나 운영해서는 안 된다.

SEC-VEL-003: Evidence Interface Authentication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

배포 환경이 caller authentication을 요구하는 경우, VEL은 배포 환경이 제공한 caller identity information을 사용해야 한다.

SEC-VEL-004: Evidence Interface Access Control
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

VEL은 배포 환경이 구성한 consumer access rule에 따라 external evidence access를 제한해야 한다.

SEC-VEL-005: Evidence Interface Integrity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

VEL은 external evidence interface를 통해 교환되는 evidence에 배포 환경이 선택한 integrity protection method를 지원해야 한다.

안전 요구사항
-------------

SAF-VEL-001: Lifecycle Execution Boundary
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

VEL은 workload lifecycle operation을 실행해서는 안 된다.

SAF-VEL-002: Process Control Boundary
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

VEL은 process control operation을 실행해서는 안 된다.

SAF-VEL-003: Container Control Boundary
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

VEL은 container control operation을 실행해서는 안 된다.

SAF-VEL-004: Hardware Control Boundary
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

VEL은 hardware control operation을 실행해서는 안 된다.

SAF-VEL-005: Multi-Node Coordination Boundary
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

VEL은 multi-node coordination을 실행해서는 안 된다.

SAF-VEL-006: OEM Decision Boundary
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

VEL은 OEM 최종 차량 의사결정 로직을 실행해서는 안 된다.

사용 가정(AoU)
--------------

AOU-VEL-001
~~~~~~~~~~~

Vehicle Evidence interface field semantic은 지정된 이해관계자가 확정한다. 이 open-source repository에는 공개 승인된 interface definition만 포함한다.

AOU-VEL-002
~~~~~~~~~~~

각 배포 환경은 구성된 collector가 요구하는 S-CORE API와 OS 접근을 제공한다.

AOU-VEL-003
~~~~~~~~~~~

지정된 외부 consumer는 VEL을 OEM 의사결정 또는 제어 경로의 일부로 만들지 않는다.

AOU-VEL-004
~~~~~~~~~~~

정규화된 aggregation data format은 담당 data-format 이해관계자와의 지속적인 합의를 통해 확정한다.
