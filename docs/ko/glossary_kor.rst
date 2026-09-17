VEL 용어집 (한국어)
======================

본 용어집은 VEL 요구사항, 아키텍처, interface 문서 전반에서 일관되게 사용하는 용어를 정의한다. 새로운 동의어를 만들지 말고 아래 용어를 사용해야 한다.

Vehicle Evidence
-----------------

VEL이 수집한 source 데이터로부터 생성하는 정규화되고 추적 가능한 출력. Vehicle Evidence에는 관측값 또는 상태, source identity, observation time, (제공되는 경우) correlation identifier가 포함된다.

Evidence Layer
---------------

전체 시스템에서 VEL이 수행하는 역할: Vehicle Evidence를 수집, 정규화하여 지정된 consumer에게 노출한다. VEL은 multi-node coordination, lifecycle 실행, process/container/hardware 제어, 최종 OEM 의사결정을 수행하지 않는다.

Source
------

Source Collector를 통해 VEL에 raw 데이터를 제공하는 runtime, hardware, 또는 S-CORE 모듈.

Source Collector
------------------

Input Interface Definition에 따라 file, command, 지원 OS interface, 또는 S-CORE API를 통해 source의 raw 데이터를 읽는 컴포넌트.

Input Interface Definition
----------------------------

VEL이 특정 source로부터 수용하는 raw 데이터의 field, type, requiredness를 정의하는 configuration artifact.

Normalization Mapping
------------------------

source별 데이터를 normalized Vehicle Evidence로 변환하는 방법(단위 변환, enum/상태 매핑, 변환 시 적용되는 quality rule)을 정의하는 configuration artifact.

Output Evidence Definition
-----------------------------

VEL이 external interface를 통해 노출하는 normalized Vehicle Evidence의 field를 정의하는 configuration artifact.

Evidence Quality
-----------------

evidence record 또는 evidence batch에 부여되는 metadata로, validity, freshness, completeness, mapping quality(값이 정확히 매핑되었는지, 근사 매핑되었는지, 매핑되지 않았는지)를 나타낸다.

Correlation Identifier
-------------------------

source context가 제공하는 경우, 동일한 source event 또는 execution instance에서 발생한 여러 evidence record를 연결하는 식별자.

VEL Health
-----------

VEL이 자신의 수집 파이프라인에 대해 노출하는 상태 정보(예: collector가 정상 동작하며 evidence를 생성하고 있는지 여부)로, Vehicle Evidence 내용 자체와는 구분된다.

Designated Consumer
----------------------

배포 환경에 의해 external evidence interface를 통해 normalized Vehicle Evidence를 수신하도록 승인된, VEL 외부의 컴포넌트 또는 시스템.

S-CORE Module
--------------

배포 환경이 노출하는 S-CORE API를 통해 VEL이 source로서 상태를 관측하고 수집할 수 있는 S-CORE 플랫폼의 모듈.

NodeAgent
----------

VEL의 collector host로 재사용되는 Pullpiri 유래 컴포넌트. Source Collector를 호스팅하고 normalized Vehicle Evidence를 발행하며, lifecycle, process, container, hardware action은 실행하지 않는다.

Baseline
--------

CM 담당자가 설정하는, VEL 저장소 이력상의 태그된 기준점으로 공식/비공식 릴리즈를 추적하는 데 사용한다. `docs/contribution/baseline_management_kor.md` 참조.
