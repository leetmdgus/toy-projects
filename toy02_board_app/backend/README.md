# 게시판 CRUD API

FastAPI 기반 클린 아키텍처 게시판 CRUD API

## 설치

```bash
cd toy02_board_app/backend
pip install -r requirements.txt
```

## 실행

```bash
cd toy02_board_app/backend/app
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## API 문서

서버 실행 후 다음 URL에서 확인:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 엔드포인트

### 게시물 CRUD

- `POST /posts/` - 게시물 작성
- `GET /posts/` - 게시물 목록 조회
- `GET /posts/{post_id}` - 게시물 단건 조회
- `PUT /posts/{post_id}` - 게시물 수정
- `DELETE /posts/{post_id}` - 게시물 삭제

## 테스트

```bash
cd toy02_board_app/backend
python -m pytest tests/test_posts/ -v
```

## 구조

```
app/
├── application/          # Use Cases
│   └── use_cases/
├── domain/              # Domain Entities & Repositories (Interface)
│   └── posts/
├── infrastructure/      # Repository Implementations & ORM Models
│   ├── orm/
│   └── repositories/
└── presentation/        # API Routers & Schemas
    ├── routers/
    └── schemas/
```
