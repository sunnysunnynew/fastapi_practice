# OpenAI LLM을 LangChain Community에서 import
# from langchain_community.llms import OpenAI
from langchain_openai import ChatOpenAI 
from langchain.chains.summarize import load_summarize_chain
from langchain.docstore.document import Document
import os
from dotenv import load_dotenv

# .env 파일에서 환경변수 로드 (OPENAI_API_KEY 등)
load_dotenv()

# OpenAI 언어모델 초기화 (기본 model은 text-davinci-003, 변경 가능)
llm = ChatOpenAI(model_name="gpt-4.1-mini", temperature=0.3) 
# 기존엔 openAI로 썼었으나 davinci가 아니라 4.1 미니 버전을 사용하기 위해 바꿈


# 입력된 텍스트를 요약하는 함수
def summarize_text(text: str) -> str:
    # LangChain 문서 포맷으로 변환
    docs = [Document(page_content=text)]
    
    # map_reduce 체인을 사용한 요약 처리
    chain = load_summarize_chain(llm, chain_type="map_reduce")
    # Map 단계: 긴 텍스트를 여러 조각으로 나누고, 각 조각을 개별적으로 요약
    # Reduce 단계: Map 단계에서 나온 여러 개의 요약문을 다시 하나로 합쳐 최종 요약을 생성
    # 요약 결과 반환
    return chain.run(docs)
