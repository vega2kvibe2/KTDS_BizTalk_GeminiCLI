from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from backend.routers import convert
import os

app = FastAPI(title="업무 말투 변환기 API")

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 실무 환경에서는 실제 도메인으로 제한 필요
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API 라우터 등록
app.include_router(convert.router, prefix="/api")

# Health Check
@app.get("/health")
async def health_check():
    return {"status": "ok"}

# 정적 파일 서버 설정 (프론트엔드)
# frontend 디렉토리가 존재하는 경우에만 마운트
frontend_path = os.path.join(os.getcwd(), "frontend")
if os.path.exists(frontend_path):
    app.mount("/static", StaticFiles(directory=frontend_path), name="static")

    # 루트 경로 접속 시 index.html 반환
    @app.get("/")
    async def read_index():
        index_file = os.path.join(frontend_path, "index.html")
        if os.path.exists(index_file):
            return FileResponse(index_file)
        return {"message": "Frontend index.html not found"}
