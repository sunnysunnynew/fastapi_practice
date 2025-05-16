from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Literal
from pathlib import Path
from llama_cpp import Llama

# 현재 파일 기준 모델 경로 설정
MODEL_PATH = Path(__file__).parent / "models" / "llama-4-scout-17b-16e-instruct.Q4_K_M.gguf"

if not MODEL_PATH.exists():
    raise FileNotFoundError(f"모델 파일을 찾을 수 없습니다: {MODEL_PATH}")

app = FastAPI()

llm = Llama(
    model_path=str(MODEL_PATH),
    n_ctx=8192,
    n_threads=8,
    n_gpu_layers=32,
    n_batch=512
)

class Message(BaseModel):
    role: Literal["system", "user", "assistant"]
    content: str

class ChatRequest(BaseModel):
    messages: List[Message]
    max_tokens: int = 256

def build_prompt(messages: List[Message]) -> str:
    system_prompt = ""
    dialog = ""

    for msg in messages:
        if msg.role == "system":
            system_prompt = msg.content
        elif msg.role == "user":
            dialog += f"User: {msg.content}\n"
        elif msg.role == "assistant":
            dialog += f"Assistant: {msg.content}\n"

    return f"[INST] {system_prompt}\n{dialog}Assistant:"

@app.post("/chat")
def chat(request: ChatRequest):
    prompt = build_prompt(request.messages)
    res = llm(prompt, max_tokens=request.max_tokens, stop=["</s>"])
    answer = res["choices"][0]["text"].strip()
    return {"response": answer}
