from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import subprocess
import whisper
import yt_dlp
from openai import OpenAI
import os
import uuid
from dotenv import load_dotenv
import time





load_dotenv()

# OpenAI API 키 설정
client = OpenAI(api_key=os.getenv("OPEN_API_KEY"))

# Fastapi 선언
app = FastAPI()

# 위스퍼 모델 로드
model = whisper.load_model("small")

# video_url model 선언 (url은 str)
class VideoRequest(BaseModel):
    url: str


# 오디오 다운로드
def download_audio(url: str, output_path: str) -> str:
    # 파일 생성
    os.makedirs(output_path, exist_ok=True)

    #임의의 uid 설정
    uid = str(uuid.uuid4())
    
    # 확장자 조인
    output_template = os.path.join(output_path, f"{uid}.%(ext)s")  # 확장자 자동 감지

    # mp3 파일로 만들기 위한 거
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_template,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': True,
    }

    # url을 다운 받음
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception as e:
        raise RuntimeError(f"유튜브 다운로드 실패: {e}")

    # 확실히 어떤 확장자가 만들어졌는지 찾기
    real_path = os.path.join(output_path, f"{uid}.mp3")
    abs_path = os.path.abspath(real_path)

    # 생성될 때까지 기다리기 (최대 3초)
    for _ in range(50):
        if os.path.exists(abs_path) and os.path.getsize(abs_path) > 0:
            break
        time.sleep(0.1)
    else:
        raise FileNotFoundError(f"다운로드된 파일을 찾을 수 없습니다: {abs_path}")

    print(f"✅ 다운로드 완료됨: {abs_path}")
    return abs_path


# 위스퍼로 바꾸기 위한 작업
def transcribe_audio(file_path: str) -> str:
    abs_path = os.path.abspath(file_path) 
    print(f"📢 Whisper로 전사 중: {abs_path}")
    try:
        # 위치에 파일에서 whisper로 뽑아냄.
        result = model.transcribe(abs_path)
        return result['text']
    except Exception as e:
        raise RuntimeError(f"오디오 전사 실패: {e}")

# whisper로 만든 text를 gpt로 뽑아냄
def summarize_text(text: str) -> str:
    print(text)
    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",  # 또는 gpt-3.5-turbo
            messages=[
                {"role": "system", "content": "다음 텍스트를 간결하게 요약해주세요. 영어로 된 내용이라면 한글로 번역해 도해주세요"},
                {"role": "user", "content": text}
            ],
            temperature=0.5
        )
        return response.choices[0].message.content
    except Exception as e:
        raise RuntimeError(f"요약 실패: {e}")
    
    
@app.post("/summarize")
async def summarize_video(request: VideoRequest):
    try:
        audio_path = download_audio(request.url, "./downloads")
        print("🔎 반환된 경로:", audio_path)
        print("📁 파일 존재:", os.path.exists(audio_path))
        print("📁 크기:", os.path.getsize(audio_path))
        
        transcript = transcribe_audio(audio_path)
        print("transcript")
        summary = summarize_text(transcript)
        os.remove(audio_path)
        # post로 리턴해줌
        return {"summary": summary}
    except Exception as e:
        print("❌ 오류 발생:", str(e))
        raise HTTPException(status_code=500, detail=str(e))