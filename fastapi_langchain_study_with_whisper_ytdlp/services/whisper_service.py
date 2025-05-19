import whisper

# Whisper 모델 로드 (base model, tiny/base/small/medium/large 가능) 
model = whisper.load_model("small")

# mp3 파일 경로를 받아서 텍스트로 변환
def transcribe_audio(file_path: str) -> str:
    result = model.transcribe(file_path)
    return result["text"]
