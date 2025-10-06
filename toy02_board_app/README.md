🧭 목표

도메인 단위로 레이어를 분리한 FastAPI 클린 아키텍처 설계

🧩 핵심 설계 철학

클린 아키텍처에서는 “의존성 방향이 도메인 중심으로만 흐른다”
즉,

presentation (routers) → service → domain → infrastructure

반대로는 절대 참조하지 않음 (DB, FastAPI, ORM에 종속되지 않음)

클린 아키텍쳐
“FastAPI + DDD + Clean Architecture 학습 플랜”

목표:
FastAPI 기반으로

User → Post → Comment
세 도메인을 클린 아키텍처 구조로 구축하며
계층 간 의존성·DTO 흐름·UseCase 분리 감각을 익히는 것.