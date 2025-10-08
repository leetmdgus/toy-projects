from fastapi import FastAPI, Request
import time
import logging

app = FastAPI()

# 로거 설정
logging.basicConfig(filename="user_activity.log", level=logging.INFO)

@app.middleware("http")
async def log_user_activity(request: Request, call_next):
    start_time = time.time()

    # 요청 정보 수집
    user_ip = request.client.host
    path = request.url.path
    method = request.method

    # 실제 요청 처리
    response = await call_next(request)

    # 응답 후 기록
    process_time = time.time() - start_time
    log_message = f"{method} {path} from {user_ip} - {response.status_code} ({process_time:.2f}s)"
    logging.info(log_message)

    return response