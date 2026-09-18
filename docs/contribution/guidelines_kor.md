# GitHub 개발 워크플로우 규칙 가이드

**작성자**: Daeyoung Jeong (@daeyoung-jeong-lge)

본 문서는 VEL 프로젝트의 이슈, 브랜치, 커밋, Pull Request 워크플로우를 정의한다. Eclipse Pullpiri의 contribution 가이드를 VEL 범위와 거버넌스에 맞게 조정하여 작성하였다.

## 목차
1. [이슈 등록 룰](#1-이슈-등록-룰)
2. [브랜치 생성 룰](#2-브랜치-생성-룰)
3. [커밋 룰](#3-커밋-룰)
4. [단계별 라벨 작성 룰](#4-단계별-라벨-작성-룰)
5. [워크플로우 단계별 가이드](#5-워크플로우-단계별-가이드)
6. [자동화 설정 가이드](#6-자동화-설정-가이드)

---

## 1. 이슈 등록 룰

### 이슈 유형 분류
- **EPIC**: 관련 FEATURE 이슈를 묶는 대규모 이니셔티브 이슈 (최상위)
- **FEATURE**: 요구사항 이슈 (EPIC의 하위, TASK의 부모)
- **TASK**: 개발 작업 이슈 (FEATURE의 하위)
- **BUG**: 버그 수정 이슈

### 이슈 계층 구조

```
EPIC
 └── FEATURE
      └── TASK
```

`BUG` 이슈는 독립적으로 추적하며 반드시 EPIC이나 FEATURE에 속할 필요는 없다.

### 이슈 제목 형식
```
[유형] 제목
```

예시:
- `[EPIC] Vehicle Evidence 출력 인터페이스`
- `[FEATURE] 정규화 Vehicle Evidence 포맷`
- `[TASK] Evidence 헤더 스키마 정의`
- `[BUG] 재시도 시 Correlation Identifier 누락`

### 이슈 본문 템플릿

#### 이니셔티브(EPIC) 이슈 템플릿
```markdown
---
name: Epic
about: 관련 요구사항을 묶는 대규모 이니셔티브
title: '[EPIC] '
labels: type:epic, status:backlog
assignees: ''
---

## 🎯 목표
<!-- 이 Epic이 달성하려는 결과와 그 이유 -->

## 📋 범위
<!-- 포함되는 것과 명시적으로 제외되는 것 -->

## 📌 연관 Feature
<!-- 자동 업데이트됨 -->
- [ ] #

## 📎 관련 문서/참조
<!-- 관련 문서 링크 -->

## 📊 진행 현황
<!-- 자동 업데이트됨 -->
```

#### 요구사항(FEATURE) 이슈 템플릿
```markdown
---
name: 요구사항
about: 새로운 기능 요구사항
title: '[FEATURE] '
labels: type:requirement, status:backlog
assignees: ''
---

## 🔗 연관 Epic
<!-- "Relates to #epic번호" 형식으로 부모 Epic 연결 -->
Relates to #

## 📝 요구사항 설명
<!-- 요구사항에 대한 상세 설명 -->

## 📋 수용 기준
- [ ] 기준 1
- [ ] 기준 2

## 📎 관련 문서/참조
<!-- 관련 문서 링크 -->

## 📌 하위 작업
<!-- 자동 업데이트됨 -->

## 🧪 테스트 계획
- [ ] 단위 테스트:
- [ ] 통합 테스트:
- [ ] 성능 테스트:

## 📊 테스트 결과
<!-- 이슈 종료 후 자동으로 업데이트됨 -->
```

#### 개발 작업(TASK) 이슈 템플릿
```markdown
---
name: 개발 작업
about: 구현해야 할 개발 작업
title: '[TASK] '
labels: type:task, status:todo
assignees: ''
---

## 📝 작업 설명
<!-- 수행해야 할 작업 설명 -->

## 📋 체크리스트
- [ ] 항목 1
- [ ] 항목 2

## 🔗 연관 요구사항
<!-- "Relates to #이슈번호" 형식으로 부모 요구사항 연결 -->
Relates to #

## 📐 구현 가이드라인
<!-- 구현 시 참고할 내용 -->

## 🧪 테스트 방법
<!-- 구현 후 테스트 방법 -->
```

### 이슈 관계 설정

- 이니셔티브(EPIC)와 요구사항(FEATURE) 연결: FEATURE 이슈 설명에 `Relates to #epic번호` 명시
- 요구사항(FEATURE)과 개발 작업(TASK) 연결: TASK 이슈 설명에 `Relates to #요구사항번호` 명시
- Epic 이슈에서 연관 Feature 추적:

```markdown
## 📌 연관 Feature
- [ ] #123 정규화 Vehicle Evidence 포맷
- [ ] #124 Evidence Quality 메타데이터
```

- 요구사항 이슈에서 태스크 리스트로 하위 작업 추적:

```markdown
## 📌 하위 작업
- [ ] #125 Evidence 헤더 스키마 정의
- [ ] #126 Quality 부여 로직 구현
```

---

## 2. 브랜치 생성 룰

### 브랜치 명명 규칙
```
<유형>/<이슈번호>-<간략한-설명>
```

### 브랜치 유형
- **feat**: 새로운 기능 개발
- **fix**: 버그 수정
- **refactor**: 코드 리팩토링
- **docs**: 문서 작업
- **test**: 테스트 코드 작업
- **chore**: 기타 유지보수 작업

### 예시
- `feat/123-normalized-evidence-format`
- `fix/145-correlation-id-retry-bug`
- `docs/167-contribution-guide`

### 브랜치 생성 절차

1. 이슈 페이지에서 "Development" > "Create a branch" 이용하거나
2. 명령행에서:
```bash
git checkout -b feat/123-normalized-evidence-format main
```

---

## 3. 커밋 룰

### 커밋 메시지 형식
```
<유형>(<범위>): <설명> [#이슈번호]
```

### 커밋 유형
- **feat**: 새로운 기능
- **fix**: 버그 수정
- **docs**: 문서 변경
- **style**: 코드 포맷팅, 세미콜론 누락 등
- **refactor**: 코드 리팩토링
- **test**: 테스트 관련 코드
- **chore**: 빌드 작업, 패키지 매니저 설정 등

### 예시
- `feat(evidence): Correlation identifier 전파 추가 [#123]`
- `fix(collector): NPU status enum 매핑 수정 [#145]`
- `docs(contribution): PR 본문 템플릿 업데이트 [#167]`

### 커밋 상세 설명 (선택사항)
```
<유형>(<범위>): <설명> [#이슈번호]

<상세 설명>

<주의 사항 또는 Breaking Changes>

<관련 이슈 (Closes, Fixes, Resolves)>
```

### PR 본문 형식
```markdown
## 📝 PR 설명
<!-- 변경 사항에 대한 설명 -->

## 🔗 관련 이슈
<!-- PR이 해결하는 이슈 링크 (Closes, Fixes, Resolves 키워드 사용) -->
Closes #

## 🧪 테스트 방법
<!-- 테스트 방법 설명 -->

## 📸 스크린샷
<!-- UI 변경이 있는 경우 스크린샷 첨부 -->

## ✅ 체크리스트
- [ ] 코드 컨벤션을 준수했습니다
- [ ] 테스트를 추가/수정했습니다
- [ ] 문서를 업데이트했습니다 (필요한 경우)
- [ ] `sphinx-build -W -b html docs docs/_build/html` 경고 없이 통과했습니다 (`docs/` 변경 시)
- [ ] 요구사항/아키텍처/기여 문서 변경 시 영문과 국문 문서를 함께 반영했습니다
```

---

## 4. 단계별 라벨 작성 룰

### 라벨 체계

#### 1. 상태 라벨 (status:*)
- `status:backlog` - 백로그에 있는 이슈
- `status:todo` - 할 일 목록에 있는 이슈
- `status:in-progress` - 진행 중인 이슈
- `status:review` - 리뷰 중인 상태
- `status:blocked` - 차단된 상태
- `status:done` - 완료된 이슈

#### 2. 유형 라벨 (type:*)
- `type:epic` - 이니셔티브 이슈
- `type:requirement` - 요구사항 이슈
- `type:task` - 개발 작업 이슈
- `type:bug` - 버그 이슈
- `type:enhancement` - 기능 개선
- `type:documentation` - 문서화 작업

#### 3. 우선순위 라벨 (priority:*)
- `priority:critical` - 최우선 처리
- `priority:high` - 높은 우선순위
- `priority:medium` - 중간 우선순위
- `priority:low` - 낮은 우선순위

#### 4. 테스트 상태 라벨 (test:*)
- `test:pending` - 테스트 대기 중
- `test:running` - 테스트 실행 중
- `test:passed` - 테스트 통과
- `test:failed` - 테스트 실패

### 라벨 색상 가이드
```
상태 라벨: 파란색 계열
유형 라벨: 녹색 계열
우선순위 라벨: 빨간색/노란색 계열
복잡도 라벨: 보라색 계열
테스트 상태 라벨: 회색/검정색 계열
```

---

## 5. 워크플로우 단계별 가이드

### 1. 이니셔티브 이슈 등록
- 제목: `[EPIC] 이니셔티브 제목`
- 라벨: `type:epic`, `status:backlog`
- 목표와 범위 작성

### 2. 요구사항 이슈 등록
- 제목: `[FEATURE] 요구사항 제목`
- 라벨: `type:requirement`, `status:backlog`
- 부모 이슈 연결: `Relates to #epic번호`
- 상세 내용 작성

### 3. 개발 작업 이슈 등록
- 제목: `[TASK] 작업 제목`
- 라벨: `type:task`, `status:todo`
- 부모 이슈 연결: `Relates to #요구사항번호`

### 4. 브랜치 생성 및 개발
- 브랜치명: `feat/이슈번호-작업명`
- 이슈 상태 변경: `status:in-progress`

### 5. 커밋 및 푸시
- 커밋 메시지: `feat(범위): 구현 내용 [#이슈번호]`

### 6. PR 생성
- 제목: `[이슈유형] 이슈 제목 (#이슈번호)`
- 본문에 `Closes #이슈번호` 포함
- 라벨: `status:review`

### 7. 코드 리뷰 및 머지
- 리뷰어 지정
- 승인 후 머지
- 이슈 자동 종료

### 8. 테스트 실행
- 테스트 실행 트리거
- 테스트 결과에 따라 라벨 업데이트: `test:passed` 또는 `test:failed`
- 요구사항 이슈에 테스트 결과 업데이트

---

## 6. 자동화 설정 가이드

### 브랜치 보호 규칙
1. 저장소 > Settings > Branches > Branch protection rules
2. main/master 브랜치 보호 규칙 설정:
   - Require pull request reviews
   - Require status checks to pass
   - Require linear history

### 라벨 자동화 워크플로우
GitHub Actions으로 다음 자동화 구현:
- 이슈/PR 생성 시 초기 라벨 설정
- 브랜치 생성 시 이슈 상태 업데이트
- PR 머지 시 테스트 실행 및 라벨 업데이트

---

## 워크플로우 다이어그램

```
이니셔티브 이슈 생성 (담당자)
       ↓
  요구사항 이슈 생성 (담당자)
       ↓
  하위 작업 생성 (담당자)
       ↓
  브랜치 생성 (담당자)
       ↓
   개발 작업 (담당자)
       ↓
  커밋 및 푸시 (담당자)
       ↓
    PR 생성 (담당자)
       ↓
  코드 리뷰 (리뷰어)
       ↓
  PR 승인 및 머지 (리뷰어)
       ↓
  자동 테스트 실행 (담당자)
       ↓
  이슈 종료 및 결과 업데이트 (담당자)
```
