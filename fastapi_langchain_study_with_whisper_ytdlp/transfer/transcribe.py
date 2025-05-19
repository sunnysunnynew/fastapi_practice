from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.yt_dlp_services import download_audio_from_youtube
from services.whisper_service import transcribe_audio
from services.langchain_service import summarize_text

# 라우터 생성
router = APIRouter(prefix="/api")

# 요청 본문 스키마 정의: JSON으로 {"url": "https://..."} 형태
class YouTubeRequest(BaseModel):
    url: str

# POST /api/transcribe-youtube 엔드포인트 정의
@router.post("/transcribe-youtube")
async def transcribe_youtube(req: YouTubeRequest):
    try:
        # 1. YouTube에서 mp3 다운로드
        audio_path = download_audio_from_youtube(req.url)
        
        # 2. Whisper로 텍스트 추출
        text = transcribe_audio(audio_path)
        
        # 3. LangChain으로 텍스트 요약
        summary = summarize_text(text)

        # 결과 반환
        return {"transcription": text, "summary": summary}
    except Exception as e:
        # 에러 발생 시 500 반환
        raise HTTPException(status_code=500, detail=str(e))
