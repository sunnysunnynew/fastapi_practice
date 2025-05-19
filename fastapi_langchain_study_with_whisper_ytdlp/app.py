from fastapi import FastAPI
from transfer import transcribe  # 위에서 만든 transcribe.py 라우터 import

# FastAPI 인스턴스 생성
app = FastAPI()

# API 라우터 등록: /api 경로에 transcribe-youtube 붙음
app.include_router(transcribe.router)
