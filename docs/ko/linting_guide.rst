요구사항 Linting Guide
=======================

목적
----

본 가이드는 VEL 요구사항과 Sphinx 문서의 필수 품질 검사를 정의한다.

필수 검사
---------

1. Build integrity

- ``sphinx-build -W -b html docs docs/_build/html``\ 은 warning과 error 없이 완료되어야 한다.
- Sphinx build는 요구사항 ID가 중복되거나, 잘못된 요구사항 분류에 위치하거나, ``STKH-VEL-*``, ``FR-VEL-*``, ``SEC-VEL-*``, ``SAF-VEL-*`` 형식을 따르지 않으면 실패해야 한다.
- Sphinx build는 이해관계자-기능 요구사항 추적성이 누락되거나, 상호 불일치하거나, 영문/국문/S-CORE 요구사항 문서 사이에서 드리프트가 발생하면 실패해야 한다.

2. Atomicity

- 각 요구사항 ID는 독립적으로 검증 가능한 하나의 의무만 포함해야 한다.
- 복합 문장은 별도 ID로 분리해야 한다.

3. Requirement classification

- ``STKH-VEL-*``\ 은 stakeholder requirement를 식별한다.
- ``FR-VEL-*``\ 은 functional requirement를 식별한다.
- ``SEC-VEL-*``\ 은 security requirement를 식별한다.
- ``SAF-VEL-*``\ 은 safety requirement를 식별한다.
- security requirement와 safety requirement를 functional requirement로 작성해서는 안 된다.

4. Traceability

- 모든 ``STKH-VEL-*`` requirement는 이를 구현하는 ``FR-VEL-*`` requirement를 참조해야 한다.
- 각 ``FR-VEL-*`` requirement는 만족하는 stakeholder requirement를 식별해야 한다.
- ID는 repository에서 unique하고 stable해야 한다.

5. Scope consistency

- VEL은 collection, normalization, evidence exposure를 담당하는 Evidence Layer로 유지해야 한다.
- VEL은 multi-node coordination, boot orchestration, lifecycle execution, process/container control, hardware control 또는 OEM final decision logic을 구현해서는 안 된다.
- 공개 문서에는 비공개 내부 프로젝트명 또는 private interface detail을 포함해서는 안 된다.

6. Configuration-driven interfaces

- input interface definition, output evidence definition, normalization mapping은 configuration artifact로 관리해야 한다.
- 새로운 source는 common evidence format 변경이 필요한 경우를 제외하고, common normalization behavior 변경 없이 configuration과 collector extension으로 추가해야 한다.

7. Language consistency

- 영문과 국문 요구사항은 동등한 normative meaning을 유지해야 한다.
- 영문에는 ``shall``\ 을 사용하고 국문에는 ``해야 한다`` 또는 ``해서는 안 된다``\ 를 사용해야 한다.

권장 명령
---------

.. code-block:: bash

   python -m pip install -r docs/requirements.txt
   rm -rf docs/_build
   sphinx-build -W -b html docs docs/_build/html
