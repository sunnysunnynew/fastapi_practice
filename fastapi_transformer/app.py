# app.py
from fastapi import FastAPI
from pydantic import BaseModel
from qna import get_answer

app = FastAPI()

class QARequest(BaseModel):
    question: str
    context: str

@app.post("/ask")
def ask_question(data: QARequest):
    answer = get_answer(data.question, data.context)
    return {"answer": answer}
