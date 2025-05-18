from fastapi import APIRouter

router = APIRouter()
# APIRouter는 FastAPI에서 경로(endpoint) 들을 그룹화하고 다른 모듈에서 정의해서 메인 앱에 등록할 수 있게 도와주는 도구입니다.
# router는 일반적으로 APIRouter()로 생성한 인스턴스 변수
@router.get("/hello")
def hello_user():
    return {"message": "hello sunny"}