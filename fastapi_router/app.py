
from fastapi import FastAPI
from controller import test

app = FastAPI()

app.include_router(test.router)
# router를 포함시킴


@app.get("/")
def read_root():
    return {"hello": "world"}

