# import services.yt_dlp_services as yt_dlp_services # This line is no longer needed
from yt_dlp import YoutubeDL # Import YoutubeDL directly

import tempfile
import os

# YouTube에서 오디오(mp3)만 다운로드하여 로컬 파일로 저장하고 경로 반환
def download_audio_from_youtube(url: str) -> str:
    # 임시 디렉토리 생성
    temp_dir = tempfile.mkdtemp()
    output_path = os.path.join(temp_dir, "audio.%(ext)s")

    # yt_dlp 옵션 정의: 최상의 오디오 포맷 다운로드 후 mp3로 변환
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_path,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': True,
        'no_warnings': True,
    }

    # yt_dlp 실행: YouTube에서 오디오 다운로드
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    # mp3 파일이 있는지 확인 후 경로 반환
    expected_file = os.path.join(temp_dir, "audio.mp3")
    if os.path.exists(expected_file):
         return expected_file
    
    for file in os.listdir(temp_dir):
        if file.endswith(".mp3"):
            return os.path.join(temp_dir, file)
    
    # 실패 시 오류 발생
    raise FileNotFoundError(f"Audio MP3 file not found in {temp_dir}.")