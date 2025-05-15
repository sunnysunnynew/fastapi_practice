# qna.py
from transformers import pipeline
import torch

# GPU 사용 여부 설정
device = 0 if torch.cuda.is_available() else -1

qa_pipeline = pipeline(
    "question-answering",
    model="distilbert-base-cased-distilled-squad",
    device=device
)

# 워밍업 (초기 로딩 지연 방지)
_ = qa_pipeline(question="What is AI?", context="AI stands for Artificial Intelligence.")

def get_answer(question: str, context: str) -> str:
    result = qa_pipeline(question=question, context=context)
    return result['answer']
