
from typing import Union
from model import pgsql_test
from fastapi import APIRouter

router = APIRouter(
    prefix="/admins",
    tags=["admins"],
    responses={404: {"description":"Not fountd"}}
)

@router.get("/list")
def list_admins():
    results = pgsql_test.list_admin()
    
    return results

#  uvicorn main:app --reload => main.py에 app이라는 객체를 사용한다. --reload를 씀 